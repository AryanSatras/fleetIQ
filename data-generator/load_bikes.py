import pandas as pd
from sqlalchemy import create_engine
import os
from pathlib import  Path

df = pd.read_csv('cleaned_bikes_data.csv')

#connect with postsql
engine = create_engine("postgresql://localhost/fleetiq")

df = df.rename(columns= {"datetime":"event_time"})

df.to_sql(
    'bikes_events',
    engine,
    if_exists='append',
    index=False
)

print("Data loaded into PostSQL succesfully.")



