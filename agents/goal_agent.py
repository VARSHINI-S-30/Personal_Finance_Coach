from services.openrouter import chat_with_tools

# ==========================================================
# Goal Agent Prompt
# ==========================================================

GOAL_PROMPT = """
You are an AI Financial Goal Planning Assistant.

Your responsibilities are:

1. Help users achieve their financial goals.
2. Calculate how much they should save every month.
3. Estimate the time required to achieve a goal.
4. Check whether a goal is achievable.
5. Track goal progress.
6. Recommend ways to improve savings.

Rules:
- Always use the appropriate tool for calculations.
- Never calculate values yourself.
- If required information is missing, ask the user for it.
- Explain the results in simple and beginner-friendly language.
"""

# ==========================================================
# Tool Schemas
# ==========================================================

GOAL_TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "calculate_monthly_savings",
            "description": "Calculate the monthly savings required to achieve a financial goal.",
            "parameters": {
                "type": "object",
                "properties": {
                    "goal_amount": {
                        "type": "number",
                        "description": "Target amount to save"
                    },
                    "months": {
                        "type": "integer",
                        "description": "Number of months available"
                    }
                },
                "required": [
                    "goal_amount",
                    "months"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "estimate_goal_completion",
            "description": "Estimate how many months are needed to achieve a financial goal.",
            "parameters": {
                "type": "object",
                "properties": {
                    "goal_amount": {
                        "type": "number"
                    },
                    "monthly_saving": {
                        "type": "number"
                    }
                },
                "required": [
                    "goal_amount",
                    "monthly_saving"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "goal_feasibility",
            "description": "Check whether a financial goal is achievable.",
            "parameters": {
                "type": "object",
                "properties": {
                    "goal_amount": {
                        "type": "number"
                    },
                    "monthly_income": {
                        "type": "number"
                    },
                    "monthly_expenses": {
                        "type": "number"
                    },
                    "target_months": {
                        "type": "integer"
                    }
                },
                "required": [
                    "goal_amount",
                    "monthly_income",
                    "monthly_expenses",
                    "target_months"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "goal_recommendation",
            "description": "Generate recommendations to achieve a financial goal.",
            "parameters": {
                "type": "object",
                "properties": {
                    "goal_amount": {
                        "type": "number"
                    },
                    "monthly_income": {
                        "type": "number"
                    },
                    "monthly_expenses": {
                        "type": "number"
                    },
                    "target_months": {
                        "type": "integer"
                    }
                },
                "required": [
                    "goal_amount",
                    "monthly_income",
                    "monthly_expenses",
                    "target_months"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "goal_progress",
            "description": "Track progress towards a financial goal.",
            "parameters": {
                "type": "object",
                "properties": {
                    "goal_amount": {
                        "type": "number"
                    },
                    "amount_saved": {
                        "type": "number"
                    }
                },
                "required": [
                    "goal_amount",
                    "amount_saved"
                ]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "future_savings",
            "description": "Estimate future savings after a given number of months.",
            "parameters": {
                "type": "object",
                "properties": {
                    "monthly_saving": {
                        "type": "number"
                    },
                    "months": {
                        "type": "integer"
                    }
                },
                "required": [
                    "monthly_saving",
                    "months"
                ]
            }
        }
    }

]

# ==========================================================
# Goal Agent
# ==========================================================

def goal_agent(user_input, memory=None):
    """
    Financial Goal Planning Agent
    """

    return chat_with_tools(
        system_prompt=GOAL_PROMPT,
        user_message=user_input,
        tools=GOAL_TOOLS,
        memory=memory
    )