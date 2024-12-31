import zarr
import numpy as np
import math
import os
import rclone
import glob 


def specify_datasets(zarr_obj, elec_row, elec_col, global_pixel_vs, global_pixel_hs, coords,dates):
    zarr_obj.create_dataset("Pixel_V",
                            data=elec_row,
                            shape=(1, len(elec_row)),
                            dtype="uint16")
    zarr_obj.create_dataset("Pixel_H",
                            data=elec_col,
                            shape=(1, len(elec_col)),
                            dtype="uint16")
    zarr_obj.create_dataset("Global_Pixel_V",
                            data=global_pixel_vs,
                            shape=(1, len(global_pixel_vs)),
                            dtype="uint16")
    zarr_obj.create_dataset("Global_Pixel_H",
                            data=global_pixel_hs,
                            shape=(1, len(global_pixel_hs)),
                            dtype="uint16")
    zarr_obj.create_dataset("Gap_Filled_DNB_BRDF-Corrected_NTL",
                            data=coords,
                            shape=(coords.shape[0], coords.shape[1]),
                            dtype="float")
    zarr_obj.create_dataset("Dates",
                            data=dates,
                            shape=(1, len(dates)),
                            dtype="M8[ns]")

def create_zarr(storage_path):
    store = zarr.DirectoryStore(storage_path)
    root = zarr.group(store=store, overwrite=True)
    return root


with open("/app/s3/access.txt", 'r') as f:
    for line in f:
        s3_access_key = str(line.strip()[4:-1])
        break

with open("/app/s3/secret.txt", 'r') as f:
    for line in f:
        s3_secret_key = str(line.strip()[4:-1])
        break

cfg = """[ceph]
type = s3
provider = Ceph 
endpoint = http://rook-ceph-rgw-nautiluss3.rook
access_key_id = {0}
secret_access_key = {1}
nounc = true
"""

cfg = cfg.format(s3_access_key, s3_secret_key)

rclone.with_config(cfg).run_cmd(command='copy', extra_args=['ceph:zarrs/wsf/wsf', '/wsf'])


for k in glob.glob("/wsf/wsf_*.zarr"):

    # Open the zarr file in read mode
    poly_zarr = zarr.open(k, mode='r')

    split_path = k.split('/')
    split_name = split_path[-1].split('_')
    tile_name = split_name[-1].strip('.zarr')
    print(tile_name)

    dates = np.array(poly_zarr["Dates"])

    # Get the Night Time Lights
    ntl = np.array(poly_zarr["DNB_BRDF-Corrected_NTL"])

    # Get the Gap-Filled Night Time Lights
    gapfilled_ntl = np.array(poly_zarr["Gap_Filled_DNB_BRDF-Corrected_NTL"])

    #Filter fill number, quality flag 2, quality flag 255
    filtered_gapfilled_ntl = np.where(gapfilled_ntl != 65535, gapfilled_ntl, np.nan)
    flag = np.array(poly_zarr["Mandatory_Quality_Flag"])
    final_gapfilled_ntl = np.where((flag != 2) & (flag != 255), filtered_gapfilled_ntl, np.nan)

    #scale factor
    final_gapfilled_ntl = final_gapfilled_ntl * 0.1
    final_gapfilled_ntl

    sample_h = np.array(poly_zarr['Pixel H'])
    sample_v = np.array(poly_zarr['Pixel V'])


    coords = {}
    for i,j in enumerate(zip(sample_h,sample_v)):
        if str([math.floor(j[0]/2),math.floor(j[1]/2)]) not in coords:
            coords[str([math.floor(j[0]/2),math.floor(j[1]/2)])]=[i]
        else:
            coords[str([math.floor(j[0]/2),math.floor(j[1]/2)])].append(i)

    for i in coords:
        if len(coords[i]) == 1:
            coords[i] = int("".join([str(integer) for integer in coords[i]]))
            coords[i] = final_gapfilled_ntl[:,coords[i]]
        elif len(coords[i]) == 2:
            coords[i] = np.nanmean((final_gapfilled_ntl[:,coords[i][0]],final_gapfilled_ntl[:,coords[i][1]]), axis=0)
        elif len(coords[i]) == 3:
            coords[i] = np.nanmean((final_gapfilled_ntl[:,coords[i][0]],final_gapfilled_ntl[:,coords[i][1]],final_gapfilled_ntl[:,coords[i][2]]), axis=0)
        elif len(coords[i]) == 4:
            coords[i] = np.nanmean((final_gapfilled_ntl[:,coords[i][0]],final_gapfilled_ntl[:,coords[i][1]],final_gapfilled_ntl[:,coords[i][2]],final_gapfilled_ntl[:,coords[i][3]]), axis=0)


    elec_col = []
    elec_row = []

    for j in coords:
        x = j.split(",")
        elec_col.append(int(x[0][1:]))
        elec_row.append(int(x[1][:-1]))

    coords=list(coords.values())
    coords = np.array(coords)
    coords = np.transpose(coords)

    tile_v = int(tile_name.split('v')[-1])
    tile_h = int(tile_name.split('v')[0][1:])

    global_pixel_vs = []
    global_pixel_hs = []

    for m in range(coords.shape[1]):
        pixel_row = elec_row[m]
        pixel_col = elec_col[m]
        global_pixel_vs.append((tile_v * 1200) + pixel_row)
        global_pixel_hs.append((tile_h * 1200) + pixel_col)

    tile_zarr = create_zarr(f"/wsf_1km/wsf_{split_name[-1]}")

    # Instantiate the datasets for the polygon's zarr
    specify_datasets(tile_zarr, elec_row, elec_col, global_pixel_vs, global_pixel_hs, coords,dates)

    rclone.with_config(cfg).run_cmd(command="copy", extra_args=[f"/wsf_1km/wsf_{split_name[-1]}", f"ceph:zarrs/wsf/wsf_1km/wsf_{split_name[-1]}"])

    print(f"done {k}")