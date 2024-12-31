import zarr
import numpy as np 
import os
import rclone
import glob 
import json
from shapely.geometry import shape, Point
import argparse
import warnings

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

    
    #distriubte in yml run 
    strr = rangee.split(" ")

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        for tile in strr[1:]:

            rclone.with_config(cfg).run_cmd(command="copy", extra_args=[f"ceph:zarrs/wsf/landscan2020/population_{tile}", f"/landscan2020/population_{tile}"])
            rclone.with_config(cfg).run_cmd(command="copy", extra_args=[f"ceph:zarrs/wsf/elec_1km_1lmin_20percent_30valid/electrification_wsf_{tile}", f"/elec_1km/electrification_wsf_{tile}"])
            rclone.with_config(cfg).run_cmd(command="copy", extra_args=[f"ceph:zarrs/wsf/bnd_zarrs_1km/{tile}", f"/bnd/{tile}"])

            country_province = {}
            totals = {}
            final = {}

            elec_path = f"/elec_1km/electrification_wsf_{tile}"
            elec_zarr = zarr.open(elec_path, mode='r')
            pop_path = f"/landscan2020/population_{tile}"
            pop_zarr = zarr.open(pop_path, mode='r')
            bnd_path = f"bnd/{tile}"
            bnd_zarr = zarr.open(bnd_path, mode='r')

            h_valid = elec_zarr['Pixel_H'][np.where(elec_zarr['Electrification_Date_Start'] <= np.datetime64("2020-07-01"))[0]]
            v_valid = elec_zarr['Pixel_V'][np.where(elec_zarr['Electrification_Date_Start'] <= np.datetime64("2020-07-01"))[0]]

            h_valid_glob = elec_zarr['Global_Pixel_H'][np.where(elec_zarr['Electrification_Date_Start'] <= np.datetime64("2020-07-01"))[0]]
            v_valid_glob = elec_zarr['Global_Pixel_V'][np.where(elec_zarr['Electrification_Date_Start'] <= np.datetime64("2020-07-01"))[0]]

            h_not = [i for i in range(len(elec_zarr['Pixel_H'])) if i not in np.where(elec_zarr['Electrification_Date_Start'] <= np.datetime64("2020-07-01"))[0]]
            v_not = [i for i in range(len(elec_zarr['Pixel_V'])) if i not in np.where(elec_zarr['Electrification_Date_Start'] <= np.datetime64("2020-07-01"))[0]]
            h_not_glob = [i for i in range(len(elec_zarr['Global_Pixel_H'])) if i not in np.where(elec_zarr['Electrification_Date_Start'] <= np.datetime64("2020-07-01"))[0]]
            v_not_glob = [i for i in range(len(elec_zarr['Global_Pixel_V'])) if i not in np.where(elec_zarr['Electrification_Date_Start'] <= np.datetime64("2020-07-01"))[0]]
            
           
            if len(h_not)>0:
                h_not = elec_zarr['Pixel_H'][h_not]
                v_not = elec_zarr['Pixel_V'][v_not]
                h_not_glob = elec_zarr['Global_Pixel_H'][h_not_glob]
                v_not_glob = elec_zarr['Global_Pixel_V'][v_not_glob]

            if len(h_valid)>0:
                for i,j,k,l in zip(v_valid,h_valid,v_valid_glob,h_valid_glob):
                    if pop_zarr['Population'][i,j] > 0.0:
                        cnt_prov = bnd_zarr['ISO3166-2'][i,j]

                        if cnt_prov not in country_province:
                            country_province[cnt_prov] = [1*pop_zarr['Population'][i,j]]
                            totals[cnt_prov] = [pop_zarr['Population'][i,j]]
                        else:
                            country_province[cnt_prov].append(1*pop_zarr['Population'][i,j])
                            totals[cnt_prov].append(pop_zarr['Population'][i,j])



            if len(h_not)>0:
                for i,j,k,l in zip(v_not,h_not,v_not_glob,h_not_glob):
                    if pop_zarr['Population'][i,j] > 0.0:
                        cnt_prov = bnd_zarr['ISO3166-2'][i,j]

                        if cnt_prov not in country_province:
                            country_province[cnt_prov] = [0*pop_zarr['Population'][i,j]]
                            totals[cnt_prov] = [pop_zarr['Population'][i,j]]
                        else:
                            country_province[cnt_prov].append(0*pop_zarr['Population'][i,j])
                            totals[cnt_prov].append(pop_zarr['Population'][i,j])            

                        

                        
            for x in country_province:
                final[x] = [sum(country_province[x]),sum(totals[x])]
            
            tile_stripped = tile.strip(".zarr")

            with open(f"{tile_stripped}_val_2020.json", "w") as f:
                json.dump(final, f) 

            rclone.with_config(cfg).run_cmd(command="copy", extra_args=[f"{tile_stripped}_val_2020.json", f"ceph:zarrs/wsf/landscan_elec_val_2020_1lmin_20percent_30valid/"])

