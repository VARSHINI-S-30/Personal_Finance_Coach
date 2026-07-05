from services.openrouter import chat_with_tools

# ==========================================================
# Report Agent Prompt
# ==========================================================

REPORT_PROMPT = """
You are an AI Personal Finance Report Assistant.

Your responsibilities are:

1. Generate financial summaries.
2. Analyze the user's monthly financial health.
3. Calculate monthly savings and savings rate.
4. Assign a financial health score.
5. Provide personalized financial recommendations.
6. Generate a complete financial report in plain text.

Rules:
- Always use the appropriate tool for calculations.
- Never calculate values yourself.
- Never generate PDFs or downloadable reports.
- Always present the report directly in the chat.
- If required information is missing, politely ask the user.
- Explain everything in simple beginner-friendly language.
- Keep recommendations practical and actionable.
"""

# ==========================================================
# Tool Schemas
# ==========================================================

REPORT_TOOLS = [

    # ------------------------------------------------------
    # Financial Summary
    # ------------------------------------------------------

    {
        "type": "function",
        "function": {
            "name": "financial_summary",
            "description": "Generate a financial summary including income, expenses, savings and saving rate.",
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

    # ------------------------------------------------------
    # Financial Health
    # ------------------------------------------------------

    {
        "type": "function",
        "function": {
            "name": "financial_health_score",
            "description": "Calculate the user's financial health score.",
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
                        "type": "number",
                        "default": 0
                    },
                    "monthly_emi": {
                        "type": "number",
                        "default": 0
                    }
                },
                "required": [
                    "monthly_income",
                    "monthly_expenses"
                ]
            }
        }
    },

    # ------------------------------------------------------
    # Recommendations
    # ------------------------------------------------------

    {
        "type": "function",
        "function": {
            "name": "generate_recommendations",
            "description": "Generate personalized financial recommendations.",
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

    # ------------------------------------------------------
    # Complete Monthly Report
    # ------------------------------------------------------

    {
        "type": "function",
        "function": {
            "name": "monthly_report",
            "description": "Generate a complete monthly financial report in text format.",
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
    }

]

# ==========================================================
# Report Agent
# ==========================================================

def report_agent(user_input, memory=None):
    """
    Financial Report Agent
    """

    return chat_with_tools(
        system_prompt=REPORT_PROMPT,
        user_message=user_input,
        tools=REPORT_TOOLS,
        memory=memory
    )