from memory import load_memory, save_memory
from services.router import route


def chat(user_input):

    memory = load_memory()

    response = route(user_input, memory)

    memory.append({
        "role": "user",
        "content": user_input
    })

    memory.append({
        "role": "assistant",
        "content": response
    })

    save_memory(memory)

    return response