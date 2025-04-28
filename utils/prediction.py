import numpy as np
import pandas as pd

def prepare_features_for_date(latest_data, target_date, district_encoded):
    """
    Prepare input features for regression model for a given target_date and district.
    latest_data: dataframe containing the latest known (real+predicted) climate data
    """

    # Extract temporal features
    year = target_date.year
    month = target_date.month
    dayofweek = target_date.dayofweek
    dayofyear = target_date.dayofyear
    season = month % 12 // 3 + 1  # Rough way to calculate season (1: Winter, 2: Spring, 3: Summer, 4: Fall)

    # Cyclical features
    dayofyear_sin = np.sin(2 * np.pi * dayofyear / 365.0)
    month_cos = np.cos(2 * np.pi * month / 12.0)

    # For lag/rolling features, get last 7 days' data for that district
    recent_data = latest_data[latest_data['district_encoded'] == district_encoded].sort_values('Date').tail(7)

    precip_7d_avg = recent_data['Precip'].mean()
    humidity_7d_avg = recent_data['Humidity_2m'].mean()
    temp_7d_avg = recent_data['Temp_2m'].mean()
    maxtemp_7d_avg = recent_data['MaxTemp_2m'].mean()
    mintemp_7d_avg = recent_data['MinTemp_2m'].mean()

    # Lag 7 (value 7 days ago, if available)
    if len(recent_data) >= 7:
        precip_lag7 = recent_data.iloc[0]['Precip']
        humidity_lag7 = recent_data.iloc[0]['Humidity_2m']
        temp_lag7 = recent_data.iloc[0]['Temp_2m']
        maxtemp_lag7 = recent_data.iloc[0]['MaxTemp_2m']
        mintemp_lag7 = recent_data.iloc[0]['MinTemp_2m']
    else:
        precip_lag7 = humidity_lag7 = temp_lag7 = maxtemp_lag7 = mintemp_lag7 = 0  # fallback

    # temp_range = recent_data['MaxTemp_2m'].iloc[-1] - recent_data['MinTemp_2m'].iloc[-1] if not recent_data.empty else 0

    # Create final input dataframe
    features = pd.DataFrame({
        'year': [year],
        'month': [month],
        'dayofweek': [dayofweek],
        'dayofyear': [dayofyear],
        'season': [season],
        'dayofyear_sin': [dayofyear_sin],
        'month_cos': [month_cos],
        'Precip_7d_avg': [precip_7d_avg],
        'Humidity_2m_7d_avg': [humidity_7d_avg],
        'Temp_2m_7d_avg': [temp_7d_avg],
        'MaxTemp_2m_7d_avg': [maxtemp_7d_avg],
        'MinTemp_2m_7d_avg': [mintemp_7d_avg],
        'Precip_lag7': [precip_lag7],
        'Humidity_2m_lag7': [humidity_lag7],
        'Temp_2m_lag7': [temp_lag7],
        'MaxTemp_2m_lag7': [maxtemp_lag7],
        'MinTemp_2m_lag7': [mintemp_lag7],
        # 'temp_range': [temp_range],
        'district_encoded': [district_encoded]
    })

    return features

def predict_until_date(regression_model, full_data_df, target_date, district_encoded):
    """
    Predict day-by-day climate data for a district up to target_date.
    """
    current_date = full_data_df['Date'].max() + pd.Timedelta(days=1)
    latest_data = full_data_df.copy()

    while current_date <= target_date:
        input_features = prepare_features_for_date(latest_data, current_date, district_encoded)

        predicted_values = regression_model.predict(input_features)[0]

        new_row = {
            'Date': current_date,
            'district_encoded': district_encoded,
            'Precip': predicted_values[0],
            'Humidity_2m': predicted_values[1],
            'Temp_2m': predicted_values[2],
            'MaxTemp_2m': predicted_values[3],
            'MinTemp_2m': predicted_values[4],
        }

        latest_data = pd.concat([latest_data, pd.DataFrame([new_row])], ignore_index=True)

        current_date += pd.Timedelta(days=1)

    # Return final predicted row
    final_row = latest_data[(latest_data['Date'] == target_date) & (latest_data['district_encoded'] == district_encoded)]
    return final_row