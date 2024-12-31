from pathlib import Path
import zarr
import numpy as np
from datetime import datetime, timedelta
import rclone
import os 
import math
import glob 
import warnings
import argparse

# Save as Zarr function - Save Tile x and y, Global x and y, and Electrification Date (First time 30 day rolling window has 6 days >= 3 for radiance units ~20% of window)
def specify_datasets(zarr_obj, global_pixel_hs, global_pixel_vs, pixel_hs, pixel_vs, elec_dates_start, elec_dates_middle, elec_dates_end,length):
    zarr_obj.create_dataset("Pixel_V",
                            data=pixel_vs,
                            shape=(1, len(pixel_vs)),
                            dtype="uint16")
    zarr_obj.create_dataset("Pixel_H",
                            data=pixel_hs,
                            shape=(1, len(pixel_hs)),
                            dtype="uint16")
    zarr_obj.create_dataset("Global_Pixel_V",
                            data=global_pixel_vs,
                            shape=(1, len(global_pixel_vs)),
                            dtype="uint16")
    zarr_obj.create_dataset("Global_Pixel_H",
                            data=global_pixel_hs,
                            shape=(1, len(global_pixel_hs)),
                            dtype="uint16")
    zarr_obj.create_dataset("Electrification_Date_Start",
                            data=elec_dates_start,
                            shape=(1, len(elec_dates_start)),
                            dtype="M8[ns]")
    zarr_obj.create_dataset("Electrification_Date_Middle",
                            data=elec_dates_middle,
                            shape=(1, len(elec_dates_middle)),
                            dtype="M8[ns]")
    zarr_obj.create_dataset("Electrification_Date_End",
                            data=elec_dates_end,
                            shape=(1, len(elec_dates_end)),
                            dtype="M8[ns]")
    zarr_obj.create_dataset("Date_Range",
                            data=length,
                            shape=(1, len(length)),
                            dtype="uint16")

def create_zarr(storage_path):
    store = zarr.DirectoryStore(storage_path)
    root = zarr.group(store=store, overwrite=True)
    return root

if __name__ == '__main__':
    # Parse arguments:
    parser = argparse.ArgumentParser(
        description='range')
    parser.add_argument('-r',
                        '--rangee',
                        type=str,
                        dest='rangee',
                        required=True,
                        help='Range files for analysis')
    args = parser.parse_args()
    rangee = args.rangee

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

    strr = rangee.split(" ")

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        for tile in strr[1:]:
            rclone.with_config(cfg).run_cmd(command='copy', extra_args=[f'ceph:zarrs/wsf/wsf_1km/wsf_{tile}', f'/wsf_1km/{tile}'])

            # Specify a path to a zarr file (root of the directory-like structure)
            zarr_path = f"/wsf_1km/{tile}"

            # Open the zarr file in read mode
            poly_zarr = zarr.open(zarr_path, mode='r')

            # Get the tile and polygon name (just stripping down the path, nothing to learn here!)
            split_path = str(zarr_path).split('/')
            tile_name = split_path[-1].strip('.zarr')

            # Get the Gap-Filled Night Time Lights
            final_gapfilled_ntl = np.array(poly_zarr["Gap_Filled_DNB_BRDF-Corrected_NTL"])

            # ## Rolling Window Electrification Date
            # This one uses a forward window only (the operational date is the first date in the window)
            # Window size (in days)
            window_size = 30

            rw_ntls_start, rw_ntls_middle, rw_ntls_end, date_range, px_num = [],[],[],[],[]

            for i in range(final_gapfilled_ntl.shape[1]):
                # List for rolling average NTLs
                ntl = [item for item in final_gapfilled_ntl[:,i] if str(item) != 'nan']
                dates = [item[1] for item in enumerate(poly_zarr["Dates"]) if str(final_gapfilled_ntl[:,i][item[0]]) != 'nan']
                for j in range(int(len(ntl)/window_size)):
                    # Get the window values (filtering fill values, reverting scale factor)
                    window_values = ntl[j*window_size:(j*window_size)+window_size]
                    # Append the electrified state - count of observations above min radiance (ignoring nans) is 20% or greater of window
                    count = 0
                    for k in window_values:
                        if k >= 1:
                            count += 1
                    if (count/window_size) >= 0.20:
                        #rw_ntls.append(count/window_size)
                        rw_ntls_start.append(dates[j*window_size])
                        rw_ntls_middle.append(dates[(j*window_size)+14])
                        rw_ntls_end.append(dates[(j*window_size)+29])
                        date_range.append(int((abs(dates[j*window_size]-dates[(j*window_size)+29])+1) / np.timedelta64(1, 'D')))
                        px_num.append(i)
                        break


            elec_dates_start = [np.datetime64("NaT") for i in range(final_gapfilled_ntl.shape[1])]
            elec_dates_middle = [np.datetime64("NaT") for i in range(final_gapfilled_ntl.shape[1])]
            elec_dates_end = [np.datetime64("NaT") for i in range(final_gapfilled_ntl.shape[1])]
            length = [np.nan for i in range(final_gapfilled_ntl.shape[1])]

            for i,j in zip(rw_ntls_start, px_num):
                elec_dates_start[j] = i
            for i,j in zip(rw_ntls_middle, px_num):
                elec_dates_middle[j] = i
            for i,j in zip(rw_ntls_end, px_num):
                elec_dates_end[j] = i
            for i,j in zip(date_range, px_num):
                length[j] = i

            pixel_vs = poly_zarr["Pixel_V"]
            pixel_hs = poly_zarr["Pixel_H"]

            global_pixel_vs = poly_zarr["Global_Pixel_V"]
            global_pixel_hs = poly_zarr["Global_Pixel_H"]

            tile_zarr = create_zarr(f"/electrification_{tile}")

            # Instantiate the datasets for the polygon's zarr
            specify_datasets(tile_zarr, global_pixel_hs, global_pixel_vs, pixel_hs, pixel_vs,elec_dates_start, elec_dates_middle, elec_dates_end,length)

            rclone.with_config(cfg).run_cmd(command="copy", extra_args=[f"/electrification_{tile}", f"ceph:zarrs/wsf/elec_1km_1lmin_20percent_30valid/electrification_wsf_{tile}"])