# ------------------------------------------------------------
# Task 4: Basic Rule-Based Chatbot (CodeAlpha Python Internship)
# The bot looks for keywords in the user's message and gives a
# predefined reply. It can remember the user's name, tell the
# time and date, tell jokes, and saves the chat in a file.
# ------------------------------------------------------------

import random
import datetime

# Each rule has: (list of keywords, list of possible replies)
# If any keyword is found in the message, the bot picks one reply.
rules = [
    (["hello", "hi", "hey"],
     ["Hi!", "Hello there!", "Hey! Nice to meet you."]),

    (["how are you", "how r u"],
     ["I'm fine, thanks!", "I'm doing great, thanks for asking!"]),

    (["your name", "who are you"],
     ["I am a simple Python chatbot made for my CodeAlpha internship."]),

    (["what can you do", "help"],
     ["I can chat, tell the time, the date and a joke. Type 'bye' to exit."]),

    (["what you understand", "what do you understand"],
     ["I understand: hello, how are you, my name is..., time, date, joke, thanks and bye."]),

    (["thanks", "thank you"],
     ["You're welcome!", "No problem!"]),

    (["python"],
     ["Python is my favourite language. It is easy to read and learn!"]),

    (["weather"],
     ["I can't check the weather, but I hope it is nice where you are."]),
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? It left its Windows open.",
    "There are 10 types of people: those who understand binary and those who don't.",
]

user_name = ""      # the bot will remember the name if the user tells it
chat_log = []       # every line of the chat is saved here


def clean_text(message):
    """Make the message lowercase and remove punctuation."""
    message = message.lower().strip()
    for symbol in "?!.,":
        message = message.replace(symbol, "")
    return message


def has_word(message, word):
    """Check if the word or phrase appears as a whole in the message.
    (This stops 'hi' from matching inside words like 'this'.)"""
    return " " + word + " " in " " + message + " "


def get_reply(message):
    """Decide what the bot should say for the given message."""
    global user_name
    message = clean_text(message)

    if message == "":
        return "Please type something."

    # special case 1: user tells their name
    if "my name is" in message:
        user_name = message.split("my name is")[1].strip().title()
        return "Nice to meet you, " + user_name + "!"

    # special case 2: user asks for their name
    if "what is my name" in message or "do you know my name" in message:
        if user_name == "":
            return "I don't know your name yet. Tell me by saying 'my name is ...'"
        return "Your name is " + user_name + "."

    # special case 3: time and date
    if has_word(message, "time"):
        now = datetime.datetime.now()
        return "The current time is " + now.strftime("%I:%M %p")

    if has_word(message, "date") or has_word(message, "today"):
        now = datetime.datetime.now()
        return "Today's date is " + now.strftime("%d %B %Y")

    # special case 4: joke
    if has_word(message, "joke"):
        return random.choice(jokes)

    # special case 5: goodbye
    if has_word(message, "bye"):
        return "Goodbye!"

    # normal rules: check every keyword
    for keywords, replies in rules:
        for word in keywords:
            if has_word(message, word):
                return random.choice(replies)

    return "Sorry, I don't understand that. Type 'help' to see what I can do."


def save_chat():
    """Save the whole conversation in a text file."""
    with open("chat_log.txt", "w") as file:
        for line in chat_log:
            file.write(line + "\n")


def main():
    print("=" * 40)
    print("        SIMPLE PYTHON CHATBOT")
    print("=" * 40)
    print("Type 'help' to see what I can do, or 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Bot:", reply)

        chat_log.append("You: " + user_input)
        chat_log.append("Bot: " + reply)

        if has_word(clean_text(user_input), "bye"):
            break

    save_chat()
    print("(Chat saved in chat_log.txt)")


main()
