import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / 'data-generator' / 'bikes_data.csv'

df = pd.read_csv(file_path)

print(df.head())



#extract


print(f'Rows before cleaning: {len(df)}')

#remove duplicates
df = df.drop_duplicates()

df = df.dropna(subset=['latitude', 'longitude'])

valid_statuses=['available', 'moving', 'maintenance']

df = df[df["status"].isin(valid_statuses)]

print(f"rows after cleaning {len(df)}")

df.to_csv("cleaned_bikes_data.csv", index=False)

