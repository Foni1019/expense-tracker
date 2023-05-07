import streamlit as st
from datetime import datetime
import database as db
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Data Visualization")


dateOfTransaction = st.date_input("Period", key="period", value=())
submitted = st.button("Get period")
if submitted:
    data = db.fetch_period(dateOfTransaction).items

    expense_totals = {}
    income_totals = {}

    # calculate totals for each category
    for entry in data:
        category = entry['category']
        amount = entry['amount']
        transaction_type = entry['typeOfTransaction']
        if transaction_type == 'Expense':
            if category not in expense_totals:
                expense_totals[category] = amount
            else:
                expense_totals[category] += amount
        elif transaction_type == 'Income':
            if category not in income_totals:
                income_totals[category] = amount
            else:
                income_totals[category] += amount

    # create interactive pie chart for expenses and incomes
    st.write('## Expenses and Incomes by Categories')
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4))
    expense_labels = list(expense_totals.keys())
    expense_values = list(expense_totals.values())
    ax1.pie(expense_values, labels=expense_labels, autopct=lambda pct: f"{pct:.1f}%\n({pct/100*sum(expense_values):.0f} HUF)", textprops={'color':"w"}, colors=sns.color_palette('Set2'))
    title1 = "Expenses (" + str(sum(expense_values)) + " HUF)"
    ax1.set_title(title1, fontweight="bold")
    income_labels = list(income_totals.keys())
    income_values = list(income_totals.values())
    ax2.pie(income_values, labels=income_labels, autopct=lambda pct: f"{pct:.1f}%\n({pct/100*sum(income_values):.0f} HUF)", textprops={'color':"w"}, colors=sns.color_palette('Set2'))
    title2 = "Incomes (" + str(sum(income_values)) + " HUF)"
    ax2.set_title(title2, fontweight="bold")

    # create bar plot for total expenses vs incomes
    fig2, ax3 = plt.subplots(figsize=(6, 4))
    ax3.bar(['Expenses', 'Incomes'], [sum(expense_values), sum(income_values)])
    ax3.set_title('Total Expenses vs Incomes')
    ax3.set_ylabel('Amount (HUF)')
    ax3.set_facecolor("#0e1117")

    fig.patch.set_facecolor('#123875')
    fig2.patch.set_facecolor('#123875')
    plt.rcParams['text.color'] = 'white'
    fig.tight_layout()
    st.pyplot(fig)
    
    st.pyplot(fig2)
