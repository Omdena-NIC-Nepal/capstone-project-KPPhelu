"""
This file is for feature engineering
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class FeatureEngineering:
    def __init__(self, df, label_encoder=None):
        self.df = df.copy() # Prevent modifying original DataFrame
        self.label_encoder = label_encoder if label_encoder else LabelEncoder()
        
    def feature_engineering_pipeline(self, rolling_window=7, lag_period=7):
        """
        This method call all feature engineering pipelines.
        Runs the full feature engineering pipeline by applying all feature engineering steps.
        """
        # Step 1: Generate generate_temporal_features
        self.generate_temporal_features()        
        # Step 2: Generate cyclical features
        self.generate_cyclical_features()        
        # Step 3: Generate rolling window features (e.g., 7-day average)
        self.generate_rolling_features(window=rolling_window)
        # Step 4: generates lagged feature
        self.generate_lagged_features(lag=lag_period)        
        # Step 5: Generate interaction/combined features (e.g., Temp * WindSpeed)
        self.generate_combined_features()        
        # Step 6: Encode 'District' using LabelEncoder
        self.encode_district()
        self.encode_climate_event_type()
        return self.df

    def generate_temporal_features(self):
        """
        Generates time-based features from the 'Date' column.
        """
        # Convert 'Date' column to datetime
        # self.df['Date'] = pd.to_datetime(self.df['Date'], errors="coerce")
        if 'Date' not in self.df:
            raise ValueError("DataFrame must contain 'Date' column")
        # Extract temporal features
        self.df['year'] = self.df['Date'].dt.year
        self.df['month'] = self.df['Date'].dt.month
        self.df['dayofweek'] = self.df['Date'].dt.dayofweek  # Monday=0, Sunday=6
        self.df['dayofyear'] = self.df['Date'].dt.dayofyear
        self.df['season'] = self.df['month'] % 12 // 3 + 1 # 1: Winter, 2: Spring, etc.

    def generate_cyclical_features(self):
        """
        Generates cyclical features for temporal data (e.g., Month and Day of the Week).
        """
        if 'dayofyear' not in self.df:
            self.generate_temporal_features()
        # Cyclical encoding for the Day of Year (1-366) and Month (1-12)
        self.df['dayofyear_sin'] = np.sin(2 * np.pi * self.df['dayofyear'] / 366)
        self.df['month_cos'] = np.cos(2 * np.pi * self.df['month'] / 12)

    def generate_rolling_features(self, window=7, 
                                  columns=['Precip', 'Temp_2m', 'WindSpeed_10m']):
        """
        Generates rolling window features like moving averages over a specified window.
        """
        # Rolling 7-day average for temperature and precipitation
        for col in columns:
            self.df[f'{col}_{window}d_avg'] = self.df[col].rolling(window=window).mean()

    def generate_lagged_features(self, lag=7, 
                                  columns=['Precip', 'Temp_2m', 'WindSpeed_10m']):
        """
        Generates lagging features which is simply lag period previous value. 
        """
        for col in columns:
            self.df[f'{col}_lag{lag}'] = self.df[col].shift(lag)

    def generate_combined_features(self):
        """
        Generates new feature with combination of more than one cliate variables
        """
        # Interaction between temperature and humidity
        self.df['temp_humidity_combined'] = self.df['Temp_2m'] * self.df['Humidity_2m']
        # Interaction between precipitation and windspeed
        self.df['precip_wind_combined'] = self.df['Precip'] * self.df['WindSpeed_10m']
        # Interaction between temperature and precipitation
        self.df['temp_precip_combined'] = self.df['Temp_2m'] * self.df['Precip']

    def encode_district(self):
        """
        Encodes the 'District' column using LabelEncoder.
        """
        if 'District' not in self.df:
            raise ValueError("DataFrame must contain 'District' column")
        self.df['district_encoded'] = self.label_encoder.fit_transform(self.df['District'])
        # Store the classes for reference
        self.district_classes = self.label_encoder.classes_

    def encode_climate_event_type(self):
        """
        Encodes the 'EventType' column using LabelEncoder.
        """
        if 'EventType' in self.df.columns:
            self.df['eventtype_encoded'] = self.label_encoder.fit_transform(self.df['EventType'])
        else:
            print("Warning: 'EventType' column not found for encoding.")

        # Store the classes for reference
        self.event_type_classes = self.label_encoder.classes_
