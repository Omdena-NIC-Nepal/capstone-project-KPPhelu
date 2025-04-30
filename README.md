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

- github link: : https://github.com/Omdena-NIC-Nepal/capstone-project-KPPhelu 
- streamlit app link: https://omdena-nic-nepal-capstone-project-kpphelu-app-2xrh3e.streamlit.app/ 

## App description
### Data Exploration page
This page is for exploration of the Climate data and Shape file of Nepal wth district boundary. This page includes 3 Tabs:
- Overview
**Overview** tab gives overview of the dataset along with climate data visualization
- Map
**Map** tab shows map of nepal with district boundaries. It also visualize choropleth maps for selected climate variable with checkbox.
- Trends
**Trends** tab shows time-series plot and monthwise boxplot for selected climate variable and selected district.

### EDA with climate events Page
This page shows some EDA with the added climate events and Extreme-Event in the given raw dataset

### Feature Engineering Page
This page perform Feature Engineering. Click "Apply Feature Engineering" button for applying the feature engineering in the dataset.

### Model Training and Evaluation Page
This page is for Model training and evaluation of the models. Select test data size from slider and click "Train All Model" button to train 3 models in sequence:
- Regression model
- Multi class classification model
- Binary classification model
Purpose of each model is described in the page. After training model is evaluated and its result is displayed in the table

### Prediction Page
This is prediction page. Choose the date and district for prediction as required. Prediction also uses three models in sequence.
- **Regression model** predict day-by-day climate data for a district up to target_date.
- **Multi class classification model** predicts climate envet type and their corresponding probability based on output of Regression model and feature engineered features.
- **Binary classification model** predicts extreme event and its probability based on output of Regression model and feature engineered features.