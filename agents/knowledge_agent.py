import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "openai/gpt-oss-20b:free"

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

from prompts import SYSTEM_PROMPT


def knowledge_agent(user_input, memory=None):

    if memory is None:
        memory = []

    messages = [
        {
            "role": "system",
            "content": KNOWLEDGE_PROMPT
        }
    ]

    messages.extend(memory)

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.4,
        "max_tokens": 500
    }

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=payload,
        verify=False
    )

    response.raise_for_status()
from services.openrouter import chat_with_tools

# ==========================================================
# Knowledge Agent Prompt
# ==========================================================

KNOWLEDGE_PROMPT = """
You are an AI Financial Knowledge Assistant.

Your responsibilities are:

1. Explain personal finance concepts in simple language.
2. Answer finance-related questions.
3. Educate users about budgeting, saving, investing, taxes, loans, insurance, and banking.
4. Explain financial terms using beginner-friendly examples.
5. Help users understand financial concepts before making decisions.

Topics you can explain include:

• Budgeting
• Savings
• Investments
• Mutual Funds
• SIP
• Stocks
• Bonds
• Inflation
• Fixed Deposits
• Emergency Funds
• Credit Score
• Loans
• EMI
• Insurance
• Taxes
• Retirement Planning
• Financial Planning

Rules:

- Explain concepts in simple, beginner-friendly language.
- Give examples whenever possible.
- Do not perform calculations unless calculation tools are added later.
- If the user asks for financial advice, provide general guidance.
- Keep answers clear, concise, and educational.
"""

# ==========================================================
# Knowledge Agent
# ==========================================================

def knowledge_agent(user_input, memory=None):
    """
    Financial Knowledge Agent
    """

    return chat_with_tools(
        system_prompt=KNOWLEDGE_PROMPT,
        user_message=user_input,
        tools=None,
        memory=memory
    )
    result = response.json()

    if "choices" not in result:
        return "Unable to answer your question."

    return result["choices"][0]["message"]["content"]