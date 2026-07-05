import os
import json
import requests
import urllib3
from dotenv import load_dotenv

from services.tool_executor import execute_tool

# Disable SSL warnings (remove later when SSL certificates are fixed)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

MODEL = "openai/gpt-oss-20b:free"


def chat_with_tools(
    system_prompt,
    user_message,
    tools=None,
    memory=None
):
    """
    Generic OpenRouter function with tool calling support.
    """

    if memory is None:
        memory = []

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    messages.extend(memory)

    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    max_steps = 6

    for step in range(max_steps):

        payload = {
            "model": MODEL,
            "messages": messages,
            "temperature": 0.3,
            "max_tokens": 600
        }

        if tools:
            payload["tools"] = tools

        try:

            response = requests.post(
                OPENROUTER_URL,
                headers=headers,
                json=payload,
                verify=False      # remove once SSL issue is fixed
            )

            result = response.json()

            if response.status_code != 200:
                return (
                    f"OpenRouter Error ({response.status_code})\n\n"
                    + json.dumps(result, indent=2)
                )

            if "choices" not in result:
                return (
                    "Unexpected OpenRouter Response\n\n"
                    + json.dumps(result, indent=2)
                )

            message = result["choices"][0]["message"]

            messages.append(message)

            # -------------------------
            # Tool Calling
            # -------------------------

            if message.get("tool_calls"):

                for tool_call in message["tool_calls"]:

                    tool_result = execute_tool(tool_call)

                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool_call["id"],
                            "name": tool_call["function"]["name"],
                            "content": tool_result
                        }
                    )

                continue

            # -------------------------
            # Final Answer
            # -------------------------

            content = message.get("content")

            if content:
                return content

            return "The model returned an empty response."

        except requests.exceptions.RequestException as e:
            return f"Network Error:\n{e}"

        except Exception as e:
            return f"Unexpected Error:\n{e}"

    return "Maximum tool iterations reached."