from tkinter import *
from tkinter import scrolledtext
from tkinter import simpledialog
from datetime import datetime
import random 

# ---------------------- USER MEMORY ----------------------

user_name = ""

# ---------------------- RESPONSE FUNCTION ----------------------

def get_response(user_input):

    greetings = ["hi", "hello", "hey", "hii"]
    bye_words = ["bye", "exit", "quit"]

    # Greetings
    if any(word in user_input for word in greetings):
        return random.choice([
            f"Hello {user_name}! 👋",
            f"Hi {user_name}, nice to meet you!",
            f"Hey {user_name}! How can I help you?"
        ])

    # Name
    elif "your name" in user_input:
        return "I am SmartBot 🤖, an advanced rule-based AI assistant."

    # AI
    elif "what is ai" in user_input:
        return "AI stands for Artificial Intelligence. It enables machines to simulate human intelligence."

    # Python
    elif "python" in user_input:
        return "Python is a powerful programming language widely used in AI, web development, and automation."

    # Time
    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time} ⏰"

    # Date
    elif "date" in user_input:
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date} 📅"

    # Joke
    elif "joke" in user_input:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
            "Why did the computer get cold? Because it forgot to close Windows! 🤣",
            "Why did the programmer quit? Because he didn't get arrays! 😄"
        ]
        return random.choice(jokes)

    # Motivation
    elif "motivate" in user_input or "motivation" in user_input:
        quotes = [
            "Success starts with consistency 💪",
            "Every expert was once a beginner 🚀",
            "Keep learning and never give up 🔥"
        ]
        return random.choice(quotes)

    # Study Tips
    elif "study" in user_input or "exam" in user_input:
        return "Study smart, practice daily, and take short breaks for better concentration 📚"

    # Calculator
    elif "add" in user_input:
        try:
            numbers = [int(word) for word in user_input.split() if word.isdigit()]
            result = sum(numbers)
            return f"The answer is {result} ➕"
        except:
            return "I couldn't calculate that."

    # Quiz
    elif "quiz" in user_input:
        return "Quiz Time! What is the capital of India?"

    elif "new delhi" in user_input:
        return "Correct Answer ✅"

    # Help
    elif "help" in user_input:
        return (
            "I can help with:\n"
            "• Greetings\n"
            "• AI & Python info\n"
            "• Time & Date\n"
            "• Jokes\n"
            "• Motivation\n"
            "• Study Tips\n"
            "• Simple Addition\n"
            "• Quiz\n"
            "• General Chat"
        )

    # Thanks
    elif "thank" in user_input:
        return "You're welcome 😊"

    # Exit
    elif any(word in user_input for word in bye_words):
        return "Goodbye! Have a wonderful day 👋"

    # Unknown
    else:
        return random.choice([
            "Sorry, I don't understand that.",
            "Can you try asking differently?",
            "Interesting... but I don't know that yet."
        ])


# ---------------------- SEND MESSAGE FUNCTION ----------------------

def send_message():

    user_input = entry_box.get().lower()

    if user_input == "":
        return

    # Display user message
    chat_area.config(state=NORMAL)
    chat_area.insert(END, f"\nYou 👤: {user_input}\n", "user")

    # Get bot response
    bot_reply = get_response(user_input)

    # Display bot message
    chat_area.insert(END, f"Bot 🤖: {bot_reply}\n", "bot")

    chat_area.config(state=DISABLED)
    chat_area.yview(END)

    # Clear entry box
    entry_box.delete(0, END)

    # Exit application
    if user_input in ["bye", "exit", "quit"]:
        window.after(1500, window.destroy)


# ---------------------- ENTER KEY SUPPORT ----------------------

def enter_key(event):
    send_message()


# ---------------------- MAIN WINDOW ----------------------

window = Tk()
window.title("Advanced AI Chatbot")
window.geometry("700x750")
window.configure(bg="#1e1e1e")

# ---------------------- USER NAME ----------------------

user_name = simpledialog.askstring("User Name", "Enter your name:")

if not user_name:
    user_name = "User"

# ---------------------- HEADER ----------------------

header = Label(
    window,
    text="Advanced Rule-Based AI Chatbot 🤖",
    bg="#111111",
    fg="cyan",
    font=("Arial", 20, "bold"),
    pady=15
)

header.pack(fill=X)

# ---------------------- CHAT AREA ----------------------

chat_area = scrolledtext.ScrolledText(
    window,
    wrap=WORD,
    font=("Consolas", 12),
    bg="#2b2b2b",
    fg="white",
    insertbackground="white",
    state=DISABLED
)

chat_area.pack(padx=15, pady=15, fill=BOTH, expand=True)

# Message Colors
chat_area.tag_config("user", foreground="lightgreen")
chat_area.tag_config("bot", foreground="cyan")

# Welcome Message
chat_area.config(state=NORMAL)
chat_area.insert(
    END,
    f"Bot 🤖: Welcome {user_name}!\nType 'help' to see available commands.\n",
    "bot"
)
chat_area.config(state=DISABLED)

# ---------------------- INPUT FRAME ----------------------

input_frame = Frame(window, bg="#1e1e1e")
input_frame.pack(fill=X, padx=10, pady=10)

# Entry Box
entry_box = Entry(
    input_frame,
    font=("Arial", 14),
    bg="#333333",
    fg="white",
    insertbackground="white",
    width=40
)

entry_box.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)

entry_box.bind("<Return>", enter_key)

# Send Button
send_button = Button(
    input_frame,
    text="SEND",
    font=("Arial", 12, "bold"),
    bg="cyan",
    fg="black",
    padx=20,
    command=send_message
)

send_button.pack(side=RIGHT, padx=10)

# ---------------------- RUN APPLICATION ----------------------

window.mainloop()