import streamlit as st
import pandas as pd
from pathlib import Path
import sys
import os

utils_dir = os.path.join(Path(__file__).parent, "utils")
sys.path.append(utils_dir)
from data_utils import DataLoader

from data_utils import DataLoader
from preprocessing import DataPreprocessor
from visualizations import plot_district_map, choropleth_map

def show(gdf, df):
    """
    Display the data exploration page
    """
    st.title("Data Exploration")

        ## multiple tabs
    tab1, tab2, tab3 = st.tabs(["Overview", "Map", "Trends"])

    with tab1:
        st.subheader("Climate Data Summary")
        # Show the raw data
        st.markdown("### Dataset Snapshot")
        st.dataframe(df.head())
        st.dataframe(df.tail())

        st.markdown("### Basic Info")
        st.write(f"**Total Rows:** {df.shape[0]}")
        st.write(f"**Total Columns:** {df.shape[1]}")
        st.write("**Column Names:**", list(df.columns))

        st.markdown("### Missing Values")
        missing = df.isnull().sum()
        st.dataframe(missing)

        # basic statistics
        st.subheader("Statistical Summary")
        st.write(df.describe().T)

    with tab2:
        ## map of nepal with district boundary
        st.subheader("District Map of Nepal")
        if gdf is not None:
            fig = plot_district_map(gdf)
            st.pyplot(fig)
        else:
            st.warning("District shapefile not loaded.")

        # Environment data on map
        st.subheader("District-wise climate data") 
        columns_required = {'Precip': {'aggregation': 'mean', 'unit': 'mm/day'},
                        'Pressure': {'aggregation': 'mean', 'unit': 'kPa'},
                        'Humidity_2m': {'aggregation': 'mean', 'unit': 'g/kg'},
                        'RH_2m': {'aggregation': 'mean', 'unit': '%'},
                        'Temp_2m': {'aggregation': 'mean', 'unit': '°C'},
                        'MaxTemp_2m': {'aggregation': 'max', 'unit': '°C'},
                        'MinTemp_2m': {'aggregation': 'min', 'unit': '°C'},
                        'WindSpeed_10m': {'aggregation': 'mean', 'unit': 'm/s'},
                        'MaxWindSpeed_10m': {'aggregation': 'max', 'unit': 'm/s'},
                        'MinWindSpeed_10m': {'aggregation': 'min', 'unit': 'm/s'}
                        }
        df_average_districtwise = aggregated_data_per_district(gdf, df, columns_required)
        for key, value in columns_required.items():
            print(key)
            fig = choropleth_map(df_average_districtwise, key, 
                                 title = f'Aggregated ({value["aggregation"]}) of "{key} ({value['unit']})" over 1981-Jan-01 to 2019-Dec-31.')
            st.pyplot(fig)




    with tab3:
        st.subheader("Trends Over Time")
        # if "Date" in df.columns:
        #     df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # ensure datetime
        #     st.line_chart(df.set_index("Date")["Temp_2m"])  # change "Temp_2m" to any valid column
        # else:
        #     st.warning("Date column missing in climate data.")

def aggregated_data_per_district(gdf, df, columns_required):
    """
    This method computes average values of the environmental data per district from given gdf and df
    """   
    agg_dict = {}
    for key,value in columns_required.items():
        agg_dict[key] = value['aggregation']

    df_aggregated = df.groupby(by = 'District').agg(agg_dict).reset_index()
    df_aggregated['District'] = df_aggregated['District'].str.upper()

    merged_data = gdf.merge(df_aggregated, left_on='DISTRICT',right_on='District')
    merged_data.drop(columns=['DISTRICT','Province'],inplace=True)

    return merged_data



    

