from main import chat

print("========================================")
print("💰 Personal Finance Coach")
print("Type 'exit' to quit.")
print("========================================")

while True:

    user = input("You: ").strip()

    if user.lower() == "exit":
        print("\nGoodbye! 👋")
        break

    try:
        response = chat(user)
        print("\nAgent:", response)
        print()

    except Exception as e:
        print("\nError:", e)
        print()