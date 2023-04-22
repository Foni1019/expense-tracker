import streamlit as st
from datetime import datetime
import database as db

st.title("Data Visualization")


dateOfTransaction = st.date_input("Period", key="period", value=())
st.write(dateOfTransaction[0])
submitted = st.button("Get period")
if submitted:
    st.write(db.fetch_period(dateOfTransaction).items)
