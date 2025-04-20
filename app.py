import streamlit as st
from pathlib import Path
import sys
import os

utils_dir = os.path.join(Path(__file__).parent, "utils")
sys.path.append(utils_dir)
from data_utils import DataLoader

pages_dir = os.path.join(Path(__file__).parent, "pages_streamlit")
sys.path.append(pages_dir)
from pages_streamlit import data_exploration_pg, model_training_pg, prediction_pg, about_pg

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


# Give the sidebar for the app navigation
st.sidebar.title("Navigation")
st.sidebar.info("Navigate through the pages.")
page = st.sidebar.radio("Go to:", ["Data Exploration", "Model Training", "Prediction", "About"])


# Display the selected page
if page == "Data Exploration":    
    data_exploration_pg.show()
elif page == "Model Training":
    model_training_pg.show()
elif page == "Prediction":
    prediction_pg.show()
elif page == "About":
    about_pg.show()


# Footer
st.markdown("---")
st.markdown("--- Krishna Prasad Phelu ---")