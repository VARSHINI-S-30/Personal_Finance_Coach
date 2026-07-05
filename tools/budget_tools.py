"""
Budget Planning Tools

This module contains utility functions used by the
Budget Planning Agent for analyzing income, expenses,
savings, and generating budgeting recommendations.
"""


def calculate_budget(income: float, expenses: float):
    """
    Calculate savings and savings percentage.
    """

    income = float(income)
    expenses = float(expenses)

    savings = income - expenses

    if income == 0:
        savings_rate = 0
    else:
        savings_rate = (savings / income) * 100

    return {
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "savings_rate": round(savings_rate, 2)
    }


def analyze_budget(income: float, expenses: float):
    """
    Analyze the user's financial health.
    """

    result = calculate_budget(income, expenses)

    rate = result["savings_rate"]

    if rate >= 30:
        status = "Excellent"

    elif rate >= 20:
        status = "Good"

    elif rate >= 10:
        status = "Average"

    elif rate >= 0:
        status = "Needs Improvement"

    else:
        status = "Overspending"

    return {
        **result,
        "status": status
    }


def budget_recommendation(income: float, expenses: float):
    """
    Generate personalized recommendations.
    """

    result = analyze_budget(income, expenses)

    status = result["status"]

    recommendations = []

    if status == "Excellent":

        recommendations.append(
            "Excellent savings! Continue investing regularly."
        )

        recommendations.append(
            "Maintain an emergency fund covering at least 6 months of expenses."
        )

        recommendations.append(
            "Consider investing in long-term financial goals."
        )

    elif status == "Good":

        recommendations.append(
            "Your savings are healthy. Try increasing them slightly."
        )

        recommendations.append(
            "Review discretionary expenses every month."
        )

    elif status == "Average":

        recommendations.append(
            "Aim to save at least 20% of your monthly income."
        )

        recommendations.append(
            "Reduce unnecessary spending."
        )

        recommendations.append(
            "Track expenses weekly."
        )

    elif status == "Needs Improvement":

        recommendations.append(
            "Your savings are quite low."
        )

        recommendations.append(
            "Reduce entertainment and shopping expenses."
        )

        recommendations.append(
            "Create a strict monthly budget."
        )

    else:

        recommendations.append(
            "Warning: You are spending more than your income."
        )

        recommendations.append(
            "Reduce non-essential expenses immediately."
        )

        recommendations.append(
            "Avoid taking unnecessary loans."
        )

        recommendations.append(
            "Prepare an emergency financial plan."
        )

    return {
        **result,
        "recommendations": recommendations
    }


def expense_breakdown(income: float, expenses: float):
    """
    Calculate expense percentage.
    """

    income = float(income)
    expenses = float(expenses)

    if income == 0:
        percent = 0
    else:
        percent = (expenses / income) * 100

    return {
        "expense_percentage": round(percent, 2)
    }


def saving_goal_estimator(goal_amount: float, monthly_saving: float):
    """
    Estimate months required to achieve a savings goal.
    """

    goal_amount = float(goal_amount)
    monthly_saving = float(monthly_saving)

    if monthly_saving <= 0:

        return {
            "months": None,
            "message": "Monthly saving must be greater than zero."
        }

    months = goal_amount / monthly_saving

    return {
        "goal_amount": goal_amount,
        "monthly_saving": monthly_saving,
        "months": round(months, 1)
    }


def emergency_fund(income: float):
    """
    Recommend an emergency fund.
    """

    income = float(income)

    recommended = income * 6

    return {
        "recommended_emergency_fund": recommended
    }


# -----------------------------------------
# Testing
# -----------------------------------------

if __name__ == "__main__":

    print(calculate_budget(60000, 42000))

    print()

    print(analyze_budget(60000, 42000))

    print()

    print(budget_recommendation(60000, 42000))

    print()

    print(expense_breakdown(60000, 42000))

    print()

    print(saving_goal_estimator(200000, 10000))

    print()

    print(emergency_fund(60000))