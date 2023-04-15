import streamlit as st


# ------ Settings ------
page_title = "Income and Expense Tracker"
page_icon = ":money_with_wings:"
layout = "wide"
#-----------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)
st.sidebar.success("Select a page above.")
