from services.openrouter import chat_with_tools

# ==========================================================
# Risk Agent Prompt
# ==========================================================

RISK_PROMPT = """
You are an AI Financial Risk & Alert Assistant.

Your responsibilities are:

1. Detect overspending.
2. Analyze spending habits.
3. Evaluate savings health.
4. Check emergency fund adequacy.
5. Assess debt risk using EMI.
6. Identify unusually high expense categories.
7. Calculate an overall financial health score.
8. Provide personalized financial alerts and recommendations.

Rules:

- Always use the appropriate tool for calculations.
- Never calculate values yourself.
- If required information is missing, ask the user politely.
- Explain the results in simple, beginner-friendly language.
- Give practical recommendations to improve financial health.
"""

# ==========================================================
# Tool Schemas
# ==========================================================

RISK_TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "spending_risk",
            "description": "Analyze spending risk based on monthly income and expenses.",
            "parameters": {
                "type": "object",
                "properties": {
                    "monthly_income": {
                        "type": "number",
                        "description": "User's monthly income"
                    },
                    "monthly_expenses": {
                        "type": "number",
                        "description": "User's monthly expenses"
                    }
                },
                "required": [
                    "monthly_income",
                    "monthly_expenses"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "saving_risk",
            "description": "Evaluate whether the user's monthly savings are healthy.",
            "parameters": {
                "type": "object",
                "properties": {
                    "monthly_income": {
                        "type": "number"
                    },
                    "monthly_expenses": {
                        "type": "number"
                    }
                },
                "required": [
                    "monthly_income",
                    "monthly_expenses"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "emergency_fund_risk",
            "description": "Check whether the user's emergency fund is sufficient.",
            "parameters": {
                "type": "object",
                "properties": {
                    "monthly_expenses": {
                        "type": "number"
                    },
                    "current_emergency_fund": {
                        "type": "number"
                    }
                },
                "required": [
                    "monthly_expenses",
                    "current_emergency_fund"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "debt_risk",
            "description": "Analyze debt risk based on monthly income and EMI.",
            "parameters": {
                "type": "object",
                "properties": {
                    "monthly_income": {
                        "type": "number"
                    },
                    "monthly_emi": {
                        "type": "number"
                    }
                },
                "required": [
                    "monthly_income",
                    "monthly_emi"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "expense_warning",
            "description": "Identify unusually high spending categories.",
            "parameters": {
                "type": "object",
                "properties": {
                    "food": {
                        "type": "number"
                    },
                    "rent": {
                        "type": "number"
                    },
                    "shopping": {
                        "type": "number"
                    },
                    "travel": {
                        "type": "number"
                    },
                    "others": {
                        "type": "number"
                    }
                },
                "required": [
                    "food",
                    "rent",
                    "shopping",
                    "travel",
                    "others"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "financial_health_score",
            "description": "Calculate an overall financial health score.",
            "parameters": {
                "type": "object",
                "properties": {
                    "monthly_income": {
                        "type": "number"
                    },
                    "monthly_expenses": {
                        "type": "number"
                    },
                    "emergency_fund": {
                        "type": "number"
                    },
                    "monthly_emi": {
                        "type": "number"
                    }
                },
                "required": [
                    "monthly_income",
                    "monthly_expenses",
                    "emergency_fund",
                    "monthly_emi"
                ]
            }
        }
    }

]

# ==========================================================
# Risk Agent
# ==========================================================

def risk_agent(user_input, memory=None):
    """
    Financial Risk & Alert Agent
    """

    return chat_with_tools(
        system_prompt=RISK_PROMPT,
        user_message=user_input,
        tools=RISK_TOOLS,
        memory=memory
    )