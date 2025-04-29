import streamlit as st
from pathlib import Path
import sys
import os

utils_dir = os.path.join(Path(__file__).parent, "utils")
sys.path.append(utils_dir)
from data_utils import DataLoader
from preprocessing import DataPreprocessor
from label_generation import LabelGenerator

pages_dir = os.path.join(Path(__file__).parent, "pages_streamlit")
sys.path.append(pages_dir)
from pages_streamlit import feature_engineering_pg, home_pg, data_exploration_pg, eda_with_climate_event_pg
from pages_streamlit import model_training_pg, prediction_pg, about_pg

# Set the page configuration
st.set_page_config(
    page_title = "Extreme Weather Event Detection and Prediction",
    page_icon=' ',
    layout = 'wide',
    initial_sidebar_state="expanded",  # Sidebar shows by default
)

# Give the title
st.header("Extreme Weather Event Detection and Prediction - Nepal")
# st.markdown("**Welcome...**")

## load data
loader = DataLoader()
try:
    loader.load_shape_file()
    loader.load_climate_data()
    st.success("Files loaded successfully.")
except FileNotFoundError as e:
    st.error(str(e))

preprocessor = DataPreprocessor(loader.climate_df, loader.district_shp)
preprocessor.preprocess()

label_generator = LabelGenerator(preprocessor.df)
label_generator.label_generation_pipeline()

# Give the sidebar for the app navigation
st.sidebar.title("Navigation")
st.sidebar.info("Navigate through the pages sequentially.")
page = st.sidebar.radio("Go to:", ["Home","Data Exploration", "EDA with climate events", "Feature Engineering",
                                   "Model Training and Evaluation", "Prediction", "About"])


# Display the selected page
if page == "Home":  
    home_pg.show()
elif page == "Data Exploration":    
    data_exploration_pg.show(gdf = preprocessor.gdf, df = preprocessor.df)
elif page == "EDA with climate events":
    eda_with_climate_event_pg.show(gdf = preprocessor.gdf, df = label_generator.df, 
                                   thresholds = label_generator.thresholds)
elif page == "Feature Engineering":
    feature_engineering_pg.show(label_generator.df)
elif page == 'Model Training and Evaluation':
    model_training_pg.show()
elif page == "Prediction":
    prediction_pg.show()
elif page == "About":
    about_pg.show()


# Footer
st.markdown("---")
st.markdown("--- Krishna Prasad Phelu ---")