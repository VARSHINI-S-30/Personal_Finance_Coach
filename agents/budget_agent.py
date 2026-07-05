from services.openrouter import chat_with_tools

# =====================================================
# Budget Agent Prompt
# =====================================================

BUDGET_PROMPT = """
You are an expert Budget Planning AI Agent.

Your responsibilities:

1. Analyze the user's monthly income and expenses.
2. Calculate savings.
3. Calculate savings percentage.
4. Explain whether spending is healthy.
5. Recommend budgeting improvements.
6. Suggest an emergency fund.
7. Keep explanations simple and beginner friendly.

IMPORTANT:

Whenever numerical calculations are needed,
ALWAYS use the appropriate tool.

Never calculate numbers yourself.

Available tools include:

- calculate_budget
- analyze_budget
- budget_recommendation
- expense_breakdown
- emergency_fund
- saving_goal_estimator
"""

# =====================================================
# Tool Schema
# =====================================================

BUDGET_TOOLS = [

    {
        "type": "function",

        "function": {

            "name": "calculate_budget",

            "description":
                "Calculate income, expenses, savings and savings percentage.",

            "parameters": {

                "type": "object",

                "properties": {

                    "income": {
                        "type": "number"
                    },

                    "expenses": {
                        "type": "number"
                    }

                },

                "required": [
                    "income",
                    "expenses"
                ]
            }
        }
    },

    {
        "type": "function",

        "function": {

            "name": "analyze_budget",

            "description":
                "Analyze overall financial health.",

            "parameters": {

                "type": "object",

                "properties": {

                    "income": {
                        "type": "number"
                    },

                    "expenses": {
                        "type": "number"
                    }

                },

                "required": [
                    "income",
                    "expenses"
                ]
            }
        }
    },

    {
        "type": "function",

        "function": {

            "name": "budget_recommendation",

            "description":
                "Generate budgeting recommendations.",

            "parameters": {

                "type": "object",

                "properties": {

                    "income": {
                        "type": "number"
                    },

                    "expenses": {
                        "type": "number"
                    }

                },

                "required": [
                    "income",
                    "expenses"
                ]
            }
        }
    },

    {
        "type": "function",

        "function": {

            "name": "expense_breakdown",

            "description":
                "Calculate expense percentage.",

            "parameters": {

                "type": "object",

                "properties": {

                    "income": {
                        "type": "number"
                    },

                    "expenses": {
                        "type": "number"
                    }

                },

                "required": [
                    "income",
                    "expenses"
                ]
            }
        }
    },

    {
        "type": "function",

        "function": {

            "name": "emergency_fund",

            "description":
                "Recommend an emergency fund amount.",

            "parameters": {

                "type": "object",

                "properties": {

                    "income": {
                        "type": "number"
                    }

                },

                "required": [
                    "income"
                ]
            }
        }
    },

    {
        "type": "function",

        "function": {

            "name": "saving_goal_estimator",

            "description":
                "Estimate months needed to reach a savings goal.",

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
    }

]


# =====================================================
# Budget Agent
# =====================================================

def budget_agent(user_input, memory=None):
    """
    Budget Planning Agent

    Parameters
    ----------
    user_input : str

    memory : list

    Returns
    -------
    str
    """

    return chat_with_tools(

        system_prompt=BUDGET_PROMPT,

        user_message=user_input,

        tools=BUDGET_TOOLS,

        memory=memory

    )