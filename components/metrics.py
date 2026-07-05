import streamlit as st


def financial_metrics(
        income,
        expense
):

    savings = income - expense

    rate = round(
        savings / income * 100,
        2
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Income",
        f"₹{income:,.0f}"
    )

    c2.metric(
        "Expenses",
        f"₹{expense:,.0f}"
    )

    c3.metric(
        "Savings",
        f"₹{savings:,.0f}"
    )

    c4.metric(
        "Saving Rate",
        f"{rate}%"
    )