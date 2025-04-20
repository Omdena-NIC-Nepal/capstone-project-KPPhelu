import streamlit as st

def show():
    st.title("About!")

    st.markdown("""
Welcome to the **Extreme Weather Event Detection and Prediction App** developed for Nepal.

This application is a part of the Omdena-NIC-Nepal collaborative AI project that focuses on analyzing and predicting extreme weather conditions using historical climate data from 93 weather stations spanning 62 districts in Nepal and machine learning models.

### 🚀 Navigation
Use the sidebar to explore the following sections:

- 📊 **Data Exploration**  
- 🧪 **Model Training and Evaluation**  
- 🔮 **Extreme Weather Prediction**  
- ℹ️ **About the Project**
""")