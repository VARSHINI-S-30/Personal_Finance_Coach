# ==========================================================
# Report Generation Tools
# ==========================================================

def financial_summary(monthly_income, monthly_expenses):
    """
    Generates a financial summary.
    """

    savings = monthly_income - monthly_expenses

    saving_rate = (
        (savings / monthly_income) * 100
        if monthly_income > 0 else 0
    )

    return {
        "monthly_income": round(monthly_income, 2),
        "monthly_expenses": round(monthly_expenses, 2),
        "monthly_savings": round(savings, 2),
        "saving_rate": round(saving_rate, 2)
    }


# ==========================================================
# Financial Health Score
# ==========================================================

def financial_health_score(
    monthly_income,
    monthly_expenses,
    emergency_fund=0,
    monthly_emi=0
):

    score = 100

    expense_ratio = monthly_expenses / monthly_income

    if expense_ratio > 0.90:
        score -= 35
    elif expense_ratio > 0.80:
        score -= 25
    elif expense_ratio > 0.70:
        score -= 15

    emi_ratio = monthly_emi / monthly_income

    if emi_ratio > 0.40:
        score -= 25
    elif emi_ratio > 0.30:
        score -= 15

    recommended = monthly_expenses * 6

    if emergency_fund < recommended:
        score -= 20

    score = max(0, min(score, 100))

    if score >= 80:
        health = "Excellent"
    elif score >= 60:
        health = "Good"
    elif score >= 40:
        health = "Average"
    else:
        health = "Poor"

    return {
        "financial_health_score": score,
        "health": health
    }


# ==========================================================
# Recommendations
# ==========================================================

def generate_recommendations(monthly_income, monthly_expenses):

    savings = monthly_income - monthly_expenses

    saving_rate = (
        (savings / monthly_income) * 100
        if monthly_income > 0 else 0
    )

    recommendations = []

    if saving_rate < 10:
        recommendations.append(
            "Reduce unnecessary expenses to improve your savings."
        )

    if saving_rate < 20:
        recommendations.append(
            "Try to save at least 20% of your monthly income."
        )

    if monthly_expenses > monthly_income * 0.8:
        recommendations.append(
            "Your expenses are high. Review your monthly spending."
        )

    if monthly_expenses <= monthly_income * 0.6:
        recommendations.append(
            "Great job keeping your expenses under control."
        )

    if saving_rate >= 20:
        recommendations.append(
            "Consider investing through SIPs or mutual funds."
        )

    recommendations.append(
        "Maintain an emergency fund equal to six months of expenses."
    )

    return {
        "recommendations": recommendations
    }


# ==========================================================
# Complete Monthly Report (TEXT ONLY)
# ==========================================================

def monthly_report(monthly_income, monthly_expenses):

    summary = financial_summary(
        monthly_income,
        monthly_expenses
    )

    health = financial_health_score(
        monthly_income,
        monthly_expenses
    )

    recommendations = generate_recommendations(
        monthly_income,
        monthly_expenses
    )

    report = f"""
# Monthly Financial Report

## Financial Summary

• Monthly Income : ₹{summary['monthly_income']}

• Monthly Expenses : ₹{summary['monthly_expenses']}

• Monthly Savings : ₹{summary['monthly_savings']}

• Saving Rate : {summary['saving_rate']}%

## Financial Health

Health Score : {health['financial_health_score']}/100

Overall Status : {health['health']}

## Recommendations

"""

    for rec in recommendations["recommendations"]:
        report += f"• {rec}\n"

    return {
        "report": report
    }