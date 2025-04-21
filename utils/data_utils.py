"""
This file handles data loading
"""

import os
import pandas as pd
import geopandas as gpd
from pathlib import Path
import streamlit as st

@st.cache_data
def load_cached_shape_file(shape_file):
    return gpd.read_file(shape_file)

@st.cache_data
def load_cached_climate_data(climate_file):
    return pd.read_csv(climate_file)

class DataLoader:
    """
    This class handle data loading for the project
    """
    def __init__(self, shape_file = r'data/Shape_Data_district/district.shp',
                 climate_file = r'data/dailyclimate.csv'):
        self.shape_file = shape_file
        self.climate_file = climate_file

        # initialization of variables
        self.district_shp = None
        self.climate_df = None
        
        self.load_shape_file()
        self.load_climate_data()

    def file_exists(self, file_name) -> bool:
        """
        Checks if file with file_name exists
        """
        file_path = Path(file_name)        
        exists = file_path.exists()
        # print(f'The file {file_name} exists: {exists}.')
        return exists
    
    def load_shape_file(self):
        """
        Loads the shapefile as a GeoDataFrame.
        """
        if self.file_exists(self.shape_file):
            self.district_shp = load_cached_shape_file(self.shape_file)
            # self.district_shp = gpd.read_file(self.shape_file)
            st.success(f'Shape data for Districts of Nepal loaded successfully.') # show the messages in the Streamlit app UI
        else:
            st.error(f'Shape file "{self.shape_file}" does not exits.')

    def load_climate_data(self):
        """
        Loads the climate CSV data into a DataFrame.
        """
        if self.file_exists(self.climate_file):
            self.climate_df = load_cached_climate_data(self.climate_file)
            # self.climate_df = pd.read_csv(self.climate_file)
            st.success(f'Climate data from 93 weather stations spanning 62 districts in Nepal loaded successfully.')
        else:
            st.error(f'Climate data file "{self.climate_file}" does not exits.')
    