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
import NRUtil.NRObjStoreUtil
import logging

logging.basicConfig(level=logging.DEBUG)
logger=logging.debug

# Omit variables
# +-------------------------------------------------------------------------------------------------
laz_loc='laz location'




# Variables
# +-------------------------------------------------------------------------------------------------
aoi_loc=os.path.join(laz_loc,'092','092o')
aoi_loc_2018=os.path.join(aoi_loc,'2018','pointcloud')
aoi_tiles= ['92o_009','92o_018','92o_019', '92o_028', '92o_029']


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

find_laz(aoi_loc_2018, aoi_tiles)