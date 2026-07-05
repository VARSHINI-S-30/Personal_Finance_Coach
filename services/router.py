from agents.budget_agent import budget_agent
from agents.goal_agent import goal_agent
from agents.knowledge_agent import knowledge_agent
from agents.risk_agent import risk_agent
from agents.report_agent import report_agent


def route(user_input, memory=None):

    message = user_input.lower()

    # ==========================================
    # Keywords
    # ==========================================

    budget_keywords = [
        "budget",
        "income",
        "expense",
        "expenses",
        "salary",
        "cash flow",
        "saving rate"
    ]

    goal_keywords = [
        "goal",
        "save",
        "saving",
        "savings",
        "target",
        "future",
        "plan",
        "bike",
        "car",
        "house",
        "vacation",
        "trip",
        "phone",
        "laptop",
        "education",
        "marriage",
        "months",
        "month",
        "achieve",
        "feasible",
        "progress"
    ]

    risk_keywords = [
        "risk",
        "warning",
        "alert",
        "overspending",
        "overspend",
        "debt",
        "emi",
        "financial health",
        "health score",
        "emergency fund",
        "poor savings",
        "high expenses",
        "high spending",
        "danger"
    ]

    report_keywords = [
        "report",
        "summary",
        "financial summary",
        "monthly report",
        "analysis report",
        "overview",
        "financial report"
    ]

    knowledge_keywords = [
        "what is",
        "difference",
        "define",
        "meaning",
        "sip",
        "mutual fund",
        "stock",
        "inflation",
        "fd",
        "loan",
        "insurance",
        "tax",
        "bank",
        "credit card",
        "interest",
        "investment"
    ]

    # ==========================================
    # Route Request
    # ==========================================

    if any(word in message for word in report_keywords):
        return report_agent(user_input, memory)

    elif any(word in message for word in risk_keywords):
        return risk_agent(user_input, memory)

    elif any(word in message for word in goal_keywords):
        return goal_agent(user_input, memory)

    elif any(word in message for word in budget_keywords):
        return budget_agent(user_input, memory)

    elif any(word in message for word in knowledge_keywords):
        return knowledge_agent(user_input, memory)

    # Default
    return knowledge_agent(user_input, memory)