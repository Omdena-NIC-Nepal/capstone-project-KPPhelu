<!---
# The Project Structure:

Extreme Weather Event Detection and Prediction ML Project-Nepal App /
|
|-- app.py                  # Main Streamlit app
| 
|-- data/
|   |-- Shape_Data_district/          # Shape file of Nepal District boundary
|   |-- dailyclimate-2.csv        # Daily climate data of Nepal
|
|-- models/    # Saved trained models and scalers
|
|-- utils/
|   |-- data_utils.py       # Data Laoding
|   |-- preprocessing.py    # Data pre-processing
|   |-- visualizations.py   # data visualization
|   |-- feature_engineering.py  # Feature engineering
|   |-- label_generation.py     # Label generation (Extreme event labeling)
|   |-- models.py           # model loading, training and evaluation
|   |-- prediction.py       # Prediction
|
|-- pages_streamlit/
|   |-- home_pg.py
|   |-- data_exploration_pg.py
|   |-- eda_with_climate_event_pg.py
|   |-- feature_engineering_pg.py
|   |-- model_training_pg.py
|   |-- prediction_pg.py 
|   |-- about_pg.py
| 
|-- requirements.txt        # Project dependencies
|-- README.md
|-- .gitignore
-->

# 🌩️ Extreme Weather Event Detection and Prediction in Nepal

This Streamlit application helps explore historical weather patterns and predict future extreme weather events in Nepal. It uses geospatial and climate data along with machine learning models to provide real-time analytics and visualizations.

---
# 📁 The Project Structure:
```
Extreme Weather Event Detection and Prediction ML Project-Nepal App /
|
|-- app.py                  # Main Streamlit app
| 
|-- data/
|   |-- Shape_Data_district/          # Shape file of Nepal District boundary
|   |-- dailyclimate-2.csv        # Daily climate data of Nepal
|
|-- models/    # Saved trained models and scalers
|
|-- utils/
|   |-- data_utils.py       # Data Laoding
|   |-- preprocessing.py    # Data pre-processing
|   |-- visualizations.py   # data visualization
|   |-- feature_engineering.py  # Feature engineering
|   |-- label_generation.py     # Label generation (Extreme event labeling)
|   |-- models.py           # model loading, training and evaluation
|   |-- prediction.py       # Prediction
|
|-- pages_streamlit/
|   |-- home_pg.py
|   |-- data_exploration_pg.py
|   |-- eda_with_climate_event_pg.py
|   |-- feature_engineering_pg.py
|   |-- model_training_pg.py
|   |-- prediction_pg.py 
|   |-- about_pg.py
| 
|-- requirements.txt        # Project dependencies
|-- README.md
|-- .gitignore
```
## 📌 Features

- Interactive **Data Exploration** by district and date
- Forecasting of **temperature**, **precipitation**, and **wind speed**
- Classification of **extreme weather events**
- **Geospatial visualizations** of climate variables

---

## App links 

github link: : https://github.com/Omdena-NIC-Nepal/capstone-project-KPPhelu 
streamlit app link: https://omdena-nic-nepal-capstone-project-kpphelu-app-2xrh3e.streamlit.app/ 