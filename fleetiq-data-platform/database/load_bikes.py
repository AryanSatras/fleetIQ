import pandas as pd
from sqlalchemy import create_engine
import os
from pathlib import  Path

BASE_DIR = Path(__file__).resolve().parents[2]

file_path = BASE_DIR / 'data-generator'/'cleaned_bikes_data.csv'

df= pd.read_csv(file_path)

print('Rows to insert:', len(df))

#connect with postsql
engine = create_engine("postgresql://localhost/fleetiq")

df = df.rename(columns= {"datetime":"event_time"})

df.to_sql(
    'bikes_events',
    engine,
    if_exists='replace',
    index=False
)

print("Data loaded into PostSQL succesfully.")



