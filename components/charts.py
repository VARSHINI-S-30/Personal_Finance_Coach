import plotly.graph_objects as go
import streamlit as st


def expense_chart(expenses):

    labels = list(expenses.keys())
    values = list(expenses.values())

    fig = go.Figure(
        go.Pie(
            labels=labels,
            values=values,
            hole=0.45
        )
    )

    fig.update_layout(
        title="Expense Breakdown",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def income_vs_expense(income, expense):

    fig = go.Figure()

    fig.add_bar(
        x=["Income"],
        y=[income],
        name="Income"
    )

    fig.add_bar(
        x=["Expenses"],
        y=[expense],
        name="Expenses"
    )

    fig.update_layout(
        title="Income vs Expenses",
        barmode="group",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def savings_gauge(rate):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=rate,
            title={"text": "Savings Rate"},
            gauge={
                "axis": {
                    "range": [0, 100]
                }
            }
        )
    )

    fig.update_layout(height=350)

    st.plotly_chart(
        fig,
        use_container_width=True
    )