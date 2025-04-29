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
