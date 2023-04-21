import streamlit as st
from datetime import datetime
from streamlit_option_menu import option_menu
import database as db

# ------ Settings ------
incomes = ["Salary", "Family", "Scholarship", "Settlement", "Investing"]
expenses = ["Food", "Travel", "Entertainment", "Clothing", "Neccessitites", "School", "Saving"]
currency = "HUF"
#-----------------------

st.set_page_config(page_title="Input Data", page_icon=":heavy_plus_sign:", layout="centered")
st.title("Input Data")
st.header(f"Data entry in {currency}")

# --- INCOME OR EXPENSE ---
selected = option_menu(
        menu_title=None,
        options=["Income","Expense"],
        icons=["wallet", "cash-coin"]
    )

# --- INPUT ---
with st.form("entry_form", clear_on_submit=True):
    if selected == "Income":
        category = st.selectbox("Category", incomes, key="category")
    else:
        category = st.selectbox("Category", expenses, key="category")
    dateOfTransaction = st.date_input("Date", key="dateOfTransaction")
    amount = st.number_input("Amount", min_value=0, format="%i", step=100, key = "amount")
    comment = st.text_area("Comment", placeholder="Enter a comment here ...")
    submitted = st.form_submit_button("Save Data")
    if submitted:
        db.insert_transaction(category, str(dateOfTransaction), amount, comment)
        st.write("Data Saved!")

    
    
    
