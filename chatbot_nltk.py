import nltk
from nltk.chat.util import Chat, reflections

# Define your chatbot patterns and responses
chatbot_pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I assist you?"]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Take care!"]),
    (r"how are you|how's it going", ["I'm just a chatbot, but I'm here to help!", "I'm doing well, thanks!"]),
    (r"tell me a joke", ["Why did the programmer quit his job? Because he didn't get arrays!", "Sure, here's one: Why do programmers prefer dark mode? Because light attracts bugs!"]),
    # Add more patterns and creative responses here
]

def main():
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'quit' to exit.")
    chatbot = Chat(chatbot_pairs, reflections)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot:", chatbot.respond(user_input))

if __name__ == "__main__":
    main()
