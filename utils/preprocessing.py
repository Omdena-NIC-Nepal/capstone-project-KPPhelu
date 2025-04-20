"""
This file pre-process data
"""
import pandas as pd

class DataPreprocessor:
    def __init__(self, climate_df: pd.DataFrame):
        self.df = climate_df.copy()

    def preprocess(self):
        """
        Data pre-processing pipeline.
        """
        self.drop_columns()
        self.convert_date()
        self.drop_missing()


    def drop_columns (self, columns=['Latitude', 'Longitude']):
        """
        Delete unnecessary columns.
        """
        self.df.drop(columns=columns, errors='ignore', inplace=True)
        print(f"'{columns}' columns deleted.")

    def convert_date(self, date_column = 'Date'):
        """
        Convert Date column into datetime format if it exists
        """
        if date_column in self.df.columns:
            self.df[date_column] = pd.to_datetime(self.df[date_column])
            print(f"'{date_column}' column converted to datetime.")

    def drop_missing(self, key_columns = ['Date', 'District']):
        """
        Drop rows with missing values in key columns.
        By default Date and District are key fields.
        """
        before = len(self.df)
        self.df.dropna(subset=key_columns, inplace=True)
        after = len(self.df)
        if after < before:
            print(f'{before - after} rows with missing vlaues in "{key_columns}" columns dropped.')
        else:
            print(f'There is no missing values in "{key_columns}" columns.')

        
