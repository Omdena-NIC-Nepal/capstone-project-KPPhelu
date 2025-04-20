import streamlit as st
from pathlib import Path
import sys
import os

utils_dir = os.path.join(Path(__file__).parent, "utils")
sys.path.append(utils_dir)
from data_utils import DataLoader

from data_utils import DataLoader
from preprocessing import DataPreprocessor
from visualizations import plot_district_map

def show():
    """
    Display the data exploration page
    """
    st.title("Data Exploration")

        ## multiple tabs
    tab1, tab2, tab3 = st.tabs(["Overview", "Map", "Trends"])

    with tab1:
        st.subheader("Climate Data Summary")
        # st.write(df.describe())
        # st.dataframe(df.head())

    with tab2:
        st.subheader("District Map of Nepal")
        # plot_district_map(geo_df)  # Your custom map function

    with tab3:
        st.subheader("Trends Over Time")
        # st.line_chart(df.set_index("Date")["Temp_2m"])  # example plot



