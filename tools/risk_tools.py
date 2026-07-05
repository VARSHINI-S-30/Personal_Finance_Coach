"""
Risk & Alert Tools

This module provides utility functions to analyze
financial risks and generate alerts.
"""


# ==========================================================
# Spending Risk
# ==========================================================

def spending_risk(monthly_income: float,
                  monthly_expenses: float):
    """
    Analyze spending risk based on expense ratio.
    """

    monthly_income = float(monthly_income)
    monthly_expenses = float(monthly_expenses)

    if monthly_income <= 0:

        return {
            "error": "Monthly income must be greater than zero."
        }

    ratio = (monthly_expenses / monthly_income) * 100

    if ratio >= 90:

        risk = "High"

        message = (
            "Your expenses consume almost all of your income."
        )

    elif ratio >= 75:

        risk = "Medium"

        message = (
            "Your expenses are relatively high."
        )

    else:

        risk = "Low"

        message = (
            "Your spending is under control."
        )

    return {

        "expense_ratio": round(ratio, 2),

        "risk_level": risk,

        "message": message

    }


# ==========================================================
# Saving Risk
# ==========================================================

def saving_risk(monthly_income: float,
                monthly_expenses: float):
    """
    Evaluate savings health.
    """

    monthly_income = float(monthly_income)
    monthly_expenses = float(monthly_expenses)

    if monthly_income <= 0:

        return {
            "error": "Monthly income must be greater than zero."
        }

    savings = monthly_income - monthly_expenses

    saving_rate = (savings / monthly_income) * 100

    if saving_rate < 10:

        risk = "High"

        advice = (
            "Increase your monthly savings."
        )

    elif saving_rate < 20:

        risk = "Medium"

        advice = (
            "Try reducing unnecessary expenses."
        )

    else:

        risk = "Low"

        advice = (
            "You have a healthy savings rate."
        )

    return {

        "monthly_savings": round(savings, 2),

        "saving_rate": round(saving_rate, 2),

        "risk_level": risk,

        "recommendation": advice

    }


# ==========================================================
# Emergency Fund Risk
# ==========================================================

def emergency_fund_risk(monthly_expenses: float,
                        current_emergency_fund: float):
    """
    Check emergency fund adequacy.
    """

    monthly_expenses = float(monthly_expenses)
    current_emergency_fund = float(current_emergency_fund)

    recommended = monthly_expenses * 6

    gap = recommended - current_emergency_fund

    if gap <= 0:

        risk = "Low"

        message = (
            "Your emergency fund is sufficient."
        )

        gap = 0

    elif gap <= monthly_expenses * 3:

        risk = "Medium"

        message = (
            "Increase your emergency fund gradually."
        )

    else:

        risk = "High"

        message = (
            "Your emergency fund is far below the recommended amount."
        )

    return {

        "recommended_fund": round(recommended, 2),

        "current_fund": round(current_emergency_fund, 2),

        "additional_amount_needed": round(gap, 2),

        "risk_level": risk,

        "message": message

    }


# ==========================================================
# Debt Risk
# ==========================================================

def debt_risk(monthly_income: float,
              monthly_emi: float):
    """
    Analyze debt burden using EMI ratio.
    """

    monthly_income = float(monthly_income)
    monthly_emi = float(monthly_emi)

    if monthly_income <= 0:

        return {
            "error": "Monthly income must be greater than zero."
        }

    ratio = (monthly_emi / monthly_income) * 100

    if ratio >= 50:

        risk = "High"

        advice = (
            "Avoid taking additional loans."
        )

    elif ratio >= 30:

        risk = "Medium"

        advice = (
            "Manage debt carefully."
        )

    else:

        risk = "Low"

        advice = (
            "Your debt level is healthy."
        )

    return {

        "emi_ratio": round(ratio, 2),

        "risk_level": risk,

        "recommendation": advice

    }


# ==========================================================
# Expense Warning
# ==========================================================

def expense_warning(food: float,
                    rent: float,
                    shopping: float,
                    travel: float,
                    others: float):
    """
    Identify unusually high spending categories.
    """

    expenses = {

        "Food": float(food),

        "Rent": float(rent),

        "Shopping": float(shopping),

        "Travel": float(travel),

        "Others": float(others)

    }

    total = sum(expenses.values())

    warnings = []

    for category, amount in expenses.items():

        percentage = (amount / total) * 100

        if percentage >= 40:

            warnings.append(

                f"{category} expenses are unusually high ({percentage:.1f}%)."

            )

    if not warnings:

        warnings.append(

            "Your expenses appear balanced."

        )

    return {

        "total_expenses": round(total, 2),

        "alerts": warnings

    }


# ==========================================================
# Financial Health Score
# ==========================================================

def financial_health_score(monthly_income: float,
                           monthly_expenses: float,
                           emergency_fund: float,
                           monthly_emi: float):
    """
    Generate an overall financial health score.
    """

    monthly_income = float(monthly_income)
    monthly_expenses = float(monthly_expenses)
    emergency_fund = float(emergency_fund)
    monthly_emi = float(monthly_emi)

    score = 100

    savings = monthly_income - monthly_expenses

    saving_rate = (savings / monthly_income) * 100

    if saving_rate < 10:
        score -= 30

    elif saving_rate < 20:
        score -= 15

    debt_ratio = (monthly_emi / monthly_income) * 100

    if debt_ratio > 50:
        score -= 25

    elif debt_ratio > 30:
        score -= 10

    recommended_fund = monthly_expenses * 6

    if emergency_fund < recommended_fund:
        score -= 20

    if score >= 85:

        status = "Excellent"

    elif score >= 70:

        status = "Good"

    elif score >= 50:

        status = "Average"

    else:

        status = "Poor"

    return {

        "financial_health_score": score,

        "status": status,

        "saving_rate": round(saving_rate, 2),

        "debt_ratio": round(debt_ratio, 2)

    }


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    print()

    print(spending_risk(60000, 50000))

    print()

    print(saving_risk(60000, 50000))

    print()

    print(emergency_fund_risk(42000, 100000))

    print()

    print(debt_risk(60000, 18000))

    print()

    print(expense_warning(
        12000,
        18000,
        15000,
        3000,
        2000
    ))

    print()

    print(financial_health_score(
        60000,
        42000,
        250000,
        8000
    ))