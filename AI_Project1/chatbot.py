print("===================================")
print("   Welcome to Smart AI Chatbot 🤖")
print("Type 'bye' to exit the chatbot")
print("===================================")

while True:

    user_input = input("\nYou: ").lower()

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    # Asking chatbot name
    elif "your name" in user_input:
        print("Bot: I am SmartBot, your AI assistant.")

    # Asking how are you
    elif "how are you" in user_input:
        print("Bot: I am doing great! Thanks for asking.")

    # Asking about AI
    elif "what is ai" in user_input:
        print("Bot: AI stands for Artificial Intelligence. It helps machines think and make decisions.")

    # Asking about Python
    elif "python" in user_input:
        print("Bot: Python is a simple and powerful programming language widely used in AI and web development.")

    # Asking time
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)

    # Asking for joke
    elif "joke" in user_input:
        print("Bot: Why did the programmer quit his job? Because he didn't get arrays!")

    # Motivation
    elif "motivate" in user_input:
        print("Bot: Every expert was once a beginner. Keep learning and practicing!")

    # Studies
    elif "study" in user_input or "exam" in user_input:
        print("Bot: Stay consistent, practice daily, and take short breaks while studying.")

    # Creator
    elif "who created you" in user_input:
        print("Bot: I was created as a Rule-Based AI project using Python.")

    # Thank you
    elif "thank" in user_input:
        print("Bot: You're welcome!")

    # Help
    elif "help" in user_input:
        print("Bot: You can ask me about AI, Python, time, jokes, motivation, studies, or greetings.")

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break

    # Unknown
    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to know what I can do.")