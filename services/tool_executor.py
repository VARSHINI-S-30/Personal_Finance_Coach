import json

# ==========================================================
# Budget Tools
# ==========================================================

from tools.budget_tools import (
    calculate_budget,
    analyze_budget,
    budget_recommendation,
    expense_breakdown,
    saving_goal_estimator,
    emergency_fund
)

# ==========================================================
# Goal Tools
# ==========================================================

from tools.goal_tools import (
    calculate_monthly_savings,
    estimate_goal_completion,
    goal_feasibility,
    goal_recommendation,
    goal_progress,
    future_savings
)

# ==========================================================
# Risk Tools
# ==========================================================

from tools.risk_tools import (
    spending_risk,
    saving_risk,
    emergency_fund_risk,
    debt_risk,
    expense_warning,
    financial_health_score
)

# ==========================================================
# Report Tools
# ==========================================================

from tools.report_tools import (
    financial_summary,
    financial_health_score,
    generate_recommendations,
    monthly_report
)

# ==========================================================
# Register Tool Functions
# ==========================================================

TOOL_FUNCTIONS = {

    # ---------------- Budget ----------------

    "calculate_budget": calculate_budget,
    "analyze_budget": analyze_budget,
    "budget_recommendation": budget_recommendation,
    "expense_breakdown": expense_breakdown,
    "saving_goal_estimator": saving_goal_estimator,
    "emergency_fund": emergency_fund,

    # ---------------- Goal ----------------

    "calculate_monthly_savings": calculate_monthly_savings,
    "estimate_goal_completion": estimate_goal_completion,
    "goal_feasibility": goal_feasibility,
    "goal_recommendation": goal_recommendation,
    "goal_progress": goal_progress,
    "future_savings": future_savings,

    # ---------------- Risk ----------------

    "spending_risk": spending_risk,
    "saving_risk": saving_risk,
    "emergency_fund_risk": emergency_fund_risk,
    "debt_risk": debt_risk,
    "expense_warning": expense_warning,
    "financial_health_score": financial_health_score,

    # ---------------- Report ----------------

    "financial_summary": financial_summary,
    "financial_health_score": financial_health_score,
    "generate_recommendations": generate_recommendations,
    "monthly_report": monthly_report,
}

# ==========================================================
# Format Tool Result
# ==========================================================

def format_result(result):

    if isinstance(result, dict):

        lines = []

        for key, value in result.items():

            key = key.replace("_", " ").title()

            if isinstance(value, list):

                lines.append(f"{key}:")

                for item in value:
                    lines.append(f"• {item}")

            else:
                lines.append(f"{key}: {value}")

        return "\n".join(lines)

    return str(result)


# ==========================================================
# Execute Tool
# ==========================================================

def execute_tool(tool_call):

    try:

        tool_name = tool_call["function"]["name"]

        tool_args = json.loads(
            tool_call["function"]["arguments"]
        )

        if tool_name not in TOOL_FUNCTIONS:
            return f"Tool '{tool_name}' not found."

        result = TOOL_FUNCTIONS[tool_name](**tool_args)

        return format_result(result)

    except Exception as e:
        return f"Error: {str(e)}"