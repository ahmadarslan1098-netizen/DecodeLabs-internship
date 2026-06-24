import random
import re

def get_response(user_input):
    user_input = user_input.lower().strip()

    greetings = ["hello", "hi", "hey", "howdy", "greetings"]
    farewells = ["bye", "goodbye", "exit", "quit", "see you", "later"]
    how_are_you = ["how are you", "how do you do", "how's it going", "what's up", "how r u"]
    name_questions = ["what is your name", "who are you", "what are you called", "your name"]
    purpose_questions = ["what can you do", "what is your purpose", "what do you do", "what you can do", "what can u do"]
    help_questions = ["help", "can you help me", "i need help", "help me"]
    time_patterns = ["what time is it", "what's the time", "tell me the time", "what is time", "time now", "current time", "what time"]
    joke_requests = ["tell me a joke", "joke", "make me laugh", "say a joke"]
    thanks = ["thank you", "thanks", "thx"]
    weather_questions = ["what's the weather", "how's the weather", "weather", "temperature"]
    age_questions = ["how old are you", "what is your age", "your age"]
    meaning_questions = ["what is the meaning of life", "meaning of life", "meaning of life"]
    math_pattern = r"(\d+)\s*([\+\-\*\/\^])\s*(\d+)"

    if user_input in greetings or any(g in user_input for g in greetings):
        responses = [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Hey! Nice to meet you!",
            "Greetings! How may I help?"
        ]
        return random.choice(responses)

    elif user_input in farewells or any(f in user_input for f in farewells):
        responses = [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! It was nice chatting with you!",
            "Until next time! Stay well!"
        ]
        return random.choice(responses)

    elif any(h in user_input for h in how_are_you):
        responses = [
            "I'm doing great, thanks for asking!",
            "I'm just a bot, but I'm functioning perfectly!",
            "All good here! How about you?",
            "I'm excellent! Ready to help you!"
        ]
        return random.choice(responses)

    elif any(n in user_input for n in name_questions):
        return "I'm ChatBot, your friendly rule-based assistant!"

    elif any(h in user_input for h in help_questions):
        return ("I can help you with:\n"
                "- Answering simple questions\n"
                "- Having a friendly conversation\n"
                "- Telling jokes\n"
                "- Doing basic math\n"
                "- Providing basic information\n\n"
                "Just type your question or request!")

    elif any(p in user_input for p in purpose_questions):
        return "I'm a rule-based chatbot designed to have simple conversations and assist you with basic queries!"

    elif any(t in user_input for t in time_patterns):
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}"

    elif any(j in user_input for j in joke_requests):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a bear with no teeth? A gummy bear!"
        ]
        return random.choice(jokes)

    elif any(t in user_input for t in thanks):
        responses = [
            "You're welcome!",
            "Happy to help!",
            "Anytime!",
            "No problem at all!"
        ]
        return random.choice(responses)

    elif any(w in user_input for w in weather_questions):
        return "I don't have access to real-time weather data, but I hope it's nice where you are!"

    elif any(a in user_input for a in age_questions):
        return "I'm ageless! I'm just a program running on your computer."

    elif any(m in user_input for m in meaning_questions):
        return "42. At least that's what the answer is according to The Hitchhiker's Guide to the Galaxy!"

    elif re.search(math_pattern, user_input):
        match = re.search(math_pattern, user_input)
        num1 = float(match.group(1))
        operator = match.group(2)
        num2 = float(match.group(3))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Cannot divide by zero!"
            result = num1 / num2
        elif operator == '^':
            result = num1 ** num2

        if result == int(result):
            result = int(result)
        return f"The answer is {result}"

    elif user_input == "":
        return "It seems you didn't type anything. How can I help you?"

    else:
        responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting! Tell me more.",
            "I don't have an answer for that yet, but I'm learning!",
            "Could you please ask something else? I'm a simple bot with limited knowledge.",
            "Hmm, I'm not sure about that. Try asking something different!"
        ]
        return random.choice(responses)


def main():
    print("=" * 50)
    print("   Welcome to the Rule-Based AI Chatbot!")
    print("=" * 50)
    print("Type 'exit' or 'quit' to end the conversation.")
    print("Type 'help' to see what I can do.")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
            print(f"\nChatBot: {get_response(user_input)}")
            print("=" * 50)
            print("   Thank you for chatting! Goodbye!")
            print("=" * 50)
            break

        response = get_response(user_input)
        print(f"ChatBot: {response}")


if __name__ == "__main__":
    main()
