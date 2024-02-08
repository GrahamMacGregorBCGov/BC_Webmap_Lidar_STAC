# +-------------------------------------------------------------------------------------------------
# Author: CFolkers
# Ministry, Division, Branch: WLRS, GeoBC, GSS
# Created Date: 2024-01-29
# Updated Date: 
# Description: crawl through folder and extract laz files to s3 bucket 
# +-------------------------------------------------------------------------------------------------

import os
import pathlib
import glob
import NRUtil.NRObjStoreUtil as NRObjStoreUtil
import logging
import boto3

logging.basicConfig(level=logging.DEBUG)
logger=logging.debug

# Omit variables
# +-------------------------------------------------------------------------------------------------
laz_loc=r'Pointclouds'
bucket=r''
secret_key=r''
user_id=r''


# Variables
# +-------------------------------------------------------------------------------------------------
aoi_loc=os.path.join(laz_loc,'092','092o')
aoi_loc_2018=os.path.join(aoi_loc,'2018','pointcloud')
aoi_tiles= ['92o_009','92o_018','92o_019', '92o_028', '92o_029']
ostore = NRObjStoreUtil.ObjectStoreUtil(r'nrs.objectstore.gov.bc.ca', bucket, secret_key, user_id )


# find laz files 
# +-------------------------------------------------------------------------------------------------
""" does not work might have to use bs4 to filter xml

find files within the 1:20000 map grids 92O.028, 029, 018, 019,009"""

def find_laz(file_loc, mapsheet_tiles):
    file_list=[]
    
    for tile in mapsheet_tiles:
        file_look_up=f"bc_{tile}"
        for file in os.listdir(file_loc):
            if file.startswith(file_look_up):
                logger(file)
        
        # break
    return file_list

#function to move list of files to S3 storage from local WSL
def move_to_s3 (laz_dir):
    #list file in dir
    laz_files=os.listdir(laz_dir)
    logger(laz_files)
    #create output name/path and move to s3 bucket?
    for file in laz_files:
        dest_file_path=f"/Pointclouds/{file}"
        in_path= f"{laz_dir}/{file}"
        ostore.put_object(local_path=in_path, ostore_path=dest_file_path)
    logging.info(f"{len(laz_dir)} files moved to S3 bucket")

# find_laz(aoi_loc_2018, aoi_tiles) 

move_to_s3(laz_loc)