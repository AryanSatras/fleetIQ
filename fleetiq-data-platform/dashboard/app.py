import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://localhost/fleetiq')

df=pd.read_sql('select * FROM bikes_events', engine)

st.title('Fleetiq Dashboard')

st.metric('Total records:', len(df))