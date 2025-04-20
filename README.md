# The Project Structure:

Extreme Weather Event Detection and Prediction ML Project-Nepal App /
|
|-- app.py                  # Main Streamlit app
| 
|-- data/
|   |-- Shape_Data_district/          # Shape file of Nepal District boundary
|   |-- dailyclimate.csv        # Daily climate data of Nepal
|
|-- utils/
|   |-- data_utils.py       # Data Laoding
|   |-- preprocessing.py    # Data pre-processing
|   |-- visualizations.py   # data visualization
|   |-- models.py           # model loading, training and evaluation
|   |-- prediction.py       # Prediction
|
|-- pages/
|   |-- data_exploration.py
|   |-- model_training.py
|   |-- prediction_pg.py 
|   |-- about.py
|
|-- requirements.txt        # Project dependencies
|-- README.md

