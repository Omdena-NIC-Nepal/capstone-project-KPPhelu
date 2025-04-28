import streamlit as st
import pandas as pd

from utils.models import load_model

def show():
    """
    Page to make prediction
    df: data frame containing feature_columns (List of feature names expected by the models)
    """
    st.title("Make Prediction")
    
    if 'fe_obj' not in st.session_state:
        st.error("Feature engineering not performed yet. Please first load data and perform feature engineerig from 'Feature Engineering' page .")
        return None
    
    # Load trained models
    reg_model, reg_scaler = load_model('regression')   # No .pkl needed because your load_model handles that
    multi_class_model, multi_class_scaler = load_model('multi_class_classifier')
    binary_class_model, binary_class_scaler = load_model('binary_classifier')

    if reg_model is None or multi_class_model is None or binary_class_model is None:
        st.error("Models not found. Please first train and save the models from 'Model Training and Evaluation' page .")
        return None
    
    # data loader from 
    input_data = st.session_state.fe_obj.df

    # Input for District and Date
    districts = st.session_state.fe_obj.district_classes
    selected_district = st.selectbox("Select District", districts)
    target_date = st.date_input("Select Target Date", value=pd.to_datetime("2024-01-01"))

    # Get district_encoded
    district_mapping = {district: idx for idx, district in enumerate(districts)}
    district_encoded = district_mapping[selected_district]

    # if st.button("Predict"):
    #         final_predicted_row = predict_until_date(regression_model, climate_data, pd.to_datetime(target_date), district_encoded)

    #         if final_predicted_row.empty:
    #             st.warning("Prediction failed. Please check your inputs.")
    #         else:
    #             st.subheader("Predicted Climate Variables")
    #             st.dataframe(final_predicted_row[["Precip", "Humidity_2m", "Temp_2m", "MaxTemp_2m", "MinTemp_2m"]])

    #             # Prepare input for event prediction
    #             input_for_classification = final_predicted_row[["Precip", "Humidity_2m", "Temp_2m", "MaxTemp_2m", "MinTemp_2m"]]

    #             event_type = multi_class_model.predict(input_for_classification)[0]
    #             extreme_event = binary_class_model.predict(input_for_classification)[0]

    #             st.success(f"📌 Predicted Event Type: {event_type}")
    #             st.success(f"📌 Predicted Extreme Event: {'Yes' if extreme_event==1 else 'No'}")
