import re

def simple_chatbot(input_text):
    if "hi" in input_text.lower() or "hello" in input_text.lower():
        return "Hello there! How can I help you today?"

    elif "how are you" in input_text.lower():
        return "I'm just a chatbot, but I'm here and ready to assist you!"

    elif "bye" in input_text.lower() or "goodbye" in input_text.lower():
        return "Goodbye! Have a great day!"

    elif "thanks" in input_text.lower() or "thank you" in input_text.lower():
        return "You're welcome! If you need anything else, feel free to ask."

    elif "your name" in input_text.lower():
        return "I'm a simple chatbot designed to assist you. You can call me ChatBot!"

    elif re.search(r"\b(?:who|what|where|when|why|how)\b", input_text, re.IGNORECASE):
        return "I'm a simple chatbot and might not have all the answers. But I'll do my best to help!"

    elif "joke" in input_text.lower():
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif "weather" in input_text.lower():
        return "I'm sorry, I don't have access to real-time weather information. You can check a weather website or app for that."

    else:
        return "I'm sorry, I didn't quite get that. Can you please rephrase or ask something else?"

# Example usage:
while True:
    user_input = input("You: ")
    response = simple_chatbot(user_input)
    print("Bot:", response)
    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break
