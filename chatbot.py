print("=" * 40)
print("       SMART CHATBOT")
print("=" * 40)
print("Type 'bye' to exit.\n")

while True:

    user = input("You: ").lower()

    if "hello" in user or "hi" in user or "hey" in user:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user:
        print("Bot: I am doing great. Thank you!")

    elif "name" in user:
        print("Bot: My name is Smart ChatBot.")

    elif "python" in user:
        print("Bot: Python is a powerful and beginner-friendly programming language.")

    elif "java" in user:
        print("Bot: Java is an object-oriented programming language.")

    elif "internship" in user:
        print("Bot: Internships help students gain practical experience.")

    elif "placement" in user:
        print("Bot: For placements, focus on aptitude, reasoning, coding, and communication skills.")

    elif "college" in user:
        print("Bot: College is a great place to learn and build your career.")

    elif "thank" in user:
        print("Bot: You're welcome!")

    elif "bye" in user:
        print("Bot: bye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")