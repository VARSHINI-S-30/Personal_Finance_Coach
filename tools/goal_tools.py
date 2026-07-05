"""
Goal Planning Tools

This module provides utility functions for
planning and tracking financial goals.
"""


def calculate_monthly_savings(goal_amount: float, months: int):
    """
    Calculate how much the user must save
    every month to achieve a financial goal.
    """

    goal_amount = float(goal_amount)
    months = int(months)

    if months <= 0:
        return {
            "error": "Months must be greater than zero."
        }

    monthly_saving = goal_amount / months

    return {
        "goal_amount": goal_amount,
        "months": months,
        "required_monthly_saving": round(monthly_saving, 2)
    }


def estimate_goal_completion(goal_amount: float, monthly_saving: float):
    """
    Estimate the number of months required
    to achieve a financial goal.
    """

    goal_amount = float(goal_amount)
    monthly_saving = float(monthly_saving)

    if monthly_saving <= 0:
        return {
            "error": "Monthly saving must be greater than zero."
        }

    months = goal_amount / monthly_saving

    return {
        "goal_amount": goal_amount,
        "monthly_saving": monthly_saving,
        "estimated_months": round(months, 1)
    }


def goal_feasibility(goal_amount: float,
                     monthly_income: float,
                     monthly_expenses: float,
                     target_months: int):
    """
    Check whether the financial goal
    is achievable.
    """

    goal_amount = float(goal_amount)
    monthly_income = float(monthly_income)
    monthly_expenses = float(monthly_expenses)
    target_months = int(target_months)

    savings = monthly_income - monthly_expenses

    if savings <= 0:

        return {
            "status": "Not Feasible",
            "monthly_available": savings,
            "required_monthly_saving": 0,
            "message": "You currently have no monthly savings."
        }

    required = goal_amount / target_months

    feasible = savings >= required

    return {
        "status": "Feasible" if feasible else "Not Feasible",
        "monthly_available": round(savings, 2),
        "required_monthly_saving": round(required, 2)
    }


def goal_recommendation(goal_amount: float,
                        monthly_income: float,
                        monthly_expenses: float,
                        target_months: int):
    """
    Generate personalized recommendations
    for achieving a financial goal.
    """

    result = goal_feasibility(
        goal_amount,
        monthly_income,
        monthly_expenses,
        target_months
    )

    recommendations = []

    if result["status"] == "Feasible":

        recommendations.append(
            "Your financial goal is achievable."
        )

        recommendations.append(
            "Continue saving consistently every month."
        )

        recommendations.append(
            "Avoid unnecessary expenses."
        )

        recommendations.append(
            "Invest surplus savings for faster growth."
        )

    else:

        recommendations.append(
            "Your goal is difficult with your current savings."
        )

        recommendations.append(
            "Reduce discretionary spending."
        )

        recommendations.append(
            "Increase your monthly savings."
        )

        recommendations.append(
            "Consider extending the target timeline."
        )

    result["recommendations"] = recommendations

    return result


def goal_progress(goal_amount: float,
                  amount_saved: float):
    """
    Calculate current progress towards
    the financial goal.
    """

    goal_amount = float(goal_amount)
    amount_saved = float(amount_saved)

    if goal_amount <= 0:

        return {
            "error": "Goal amount must be greater than zero."
        }

    progress = (amount_saved / goal_amount) * 100

    remaining = goal_amount - amount_saved

    return {
        "goal_amount": goal_amount,
        "amount_saved": amount_saved,
        "remaining_amount": round(remaining, 2),
        "progress_percentage": round(progress, 2)
    }


def future_savings(monthly_saving: float,
                   months: int):
    """
    Estimate total savings after
    a given number of months.
    """

    monthly_saving = float(monthly_saving)
    months = int(months)

    total = monthly_saving * months

    return {
        "monthly_saving": monthly_saving,
        "months": months,
        "future_savings": round(total, 2)
    }


if __name__ == "__main__":

    print()

    print(calculate_monthly_savings(120000, 12))

    print()

    print(estimate_goal_completion(150000, 12000))

    print()

    print(goal_feasibility(
        100000,
        60000,
        42000,
        10
    ))

    print()

    print(goal_recommendation(
        100000,
        60000,
        42000,
        10
    ))

    print()

    print(goal_progress(
        100000,
        45000
    ))

    print()

    print(future_savings(
        10000,
        12
    ))