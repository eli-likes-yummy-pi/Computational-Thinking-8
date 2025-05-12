import random
import re

# A set of predefined responses to keywords
responses = {
    "hello": ["Hi there!", "Hello!", "Hi, how can I help you today?"],
    "how are you": ["I'm doing well, thank you!", "I'm just a program, but I'm doing great!", "I'm fine, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye, have a great day!"],
    "help": ["How can I assist you?", "I can help you with some basic questions. Ask me something!"],
    "name": ["I am a chatbot created to assist you.", "I don't have a name, but you can call me whatever you like!"],
    "default": ["I'm not sure how to respond to that. Can you ask something else?"]
}

def get_response(user_input):
    """ Get a response based on user input """
    user_input = user_input.lower()
    
    for key in responses:
        if re.search(r'\b' + re.escape(key) + r'\b', user_input):
            return random.choice(responses[key])
    
    # Return a default response if no match is found
    return random.choice(responses["default"])

def chatbot():
    """ The main chatbot loop """
    print("Chatbot: Hello! Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot:", get_response(user_input))
            break
        
        print("Chatbot:", get_response(user_input))

# Start the chatbot
chatbot()