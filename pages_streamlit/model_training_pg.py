import streamlit as st
from pathlib import Path
import os
import sys

utils_dir = os.path.join(Path(__file__).parent, "utils")
sys.path.append(utils_dir)
from data_utils import PrepareData
from models import split_data, train_model, evaluate_model

def show():
    """
    Page for model loading and training
    """
    st.title("Model Selection and Training")  

    if 'df_feature_added' not in st.session_state:
        st.warning("First you need to perform Feature Engineering. Go to 'Feature Engineering' page for Feature engineering")
    else:
        # Train test split
        test_size = st.slider("Test data size (%)", 10, 40, 20)

        # Selection for model type
        model_type = st.selectbox("Select Model Type", ["Regression", "Multi-Class Classifier", "Binary Classifier"])

        # Prepare Data and Display description based on the selected model type
        data_preparer = PrepareData(st.session_state['df_feature_added'])

        if model_type == "Regression":
            st.markdown("""
            **Regression** is used to predict continuous numerical values. In this case, the model will be predicting 
            climate variables ['Precip', 'Humidity_2m', 'Temp_2m', 'MaxTemp_2m', 'MinTemp_2m'].
            """)
            # X_reg, y_reg = data_preparer.prepare_data_regression()
            X, y = data_preparer.prepare_data_regression()
        elif model_type == "Multi-Class Classifier":
            st.markdown("""
            **Multi-Class Classifier** is used to predict one of several categories (classes). 
            In this case, the model will be predicting the type of events ['ColdWave', 'HighTemp', 'Heatwave', 'HeavyRain'].
            """)
            # X_multi, y_multi = data_preparer.prepare_data_regression()
            X, y = data_preparer.prepare_data_regression()
        elif model_type == "Binary Classifier":
            st.markdown("""
            **Binary Classifier** is used to predict one of two possible outcomes. 
            In this case, the model will be predicting whether an extreme event occurs (yes/no).
            """)
            # X_binary, y_binary = data_preparer.prepare_data_regression()
            X, y = data_preparer.prepare_data_regression()

        X_train, X_test, y_train, y_test, = split_data(X, y, test_size/100)

        st.write(f"Training Data: {len(X_train)} Samples")
        st.write(f"Test data : {len(X_test)} samples")

        # train model Button
        if st.button('Train Model'):
            with st.spinner("Trainig in progress..."):
                # Train the model
                model, scaler = train_model(X_train, y_train, model_type)

                # Evaluate the model
                metrics = evaluate_model(model, scaler, X_train, y_train, X_test, y_test, model_type)

                # Display the metrics
                st.write(metrics)
                # col1, col2 = st.columns(2)
                # with col1:
                #     st.subheader("Training Metrics")
                #     st.write(f"RMSE: {metrics['test_rmse']:.2f} C")
                #     st.write(f"R2: {metrics['train_r2']:.4f}")

                # with col2:
                #     st.subheader("Testing Metrics")
                #     st.write(f"RMSE: {metrics['test_rmse']:.2f} C")
                #     st.write(f"R2: {metrics['test_r2']:.4f}")

    

        
    




        
