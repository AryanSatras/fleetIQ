import pandas as pd
import random
from datetime import datetime

data =[]

for bike_id in range(1, 101):
    data.append({
        'bike_id': bike_id,
        'datetime': datetime.now(),
        'latitude': random.uniform(52.470, 52.500),
        'longitude': random.uniform(-1.920, -1.850),
        'status': random.choice(['available','moving', 'maintenance'])
    })

df = pd.DataFrame(data)
df.to_csv('bikes_data.csv', index=False)

print("100 records of bikes generated")
