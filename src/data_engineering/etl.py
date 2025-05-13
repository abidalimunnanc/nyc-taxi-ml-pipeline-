# src/data_engineering/etl.py

import pandas as pd
import os

RAW_DATA_PATH = "data/raw/yellow_tripdata_2022-01.parquet"
PROCESSED_DATA_PATH = "data/processed/processed_data.parquet"

def load_data(path):
    return pd.read_parquet(path)

def clean_data(df):
    df = df.copy()
    df = df[df['passenger_count'] > 0]
    df = df[df['trip_distance'] > 0]
    df['trip_duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds()
    df = df[df['trip_duration'] > 0]
    return df

def save_data(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_parquet(path, index=False)
    print(f"Saved cleaned data to {path}")

def main():
    df = load_data(RAW_DATA_PATH)
    df_clean = clean_data(df)
    save_data(df_clean, PROCESSED_DATA_PATH)

if __name__ == "__main__":
    main()
