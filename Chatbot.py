import random

# Define the responses dictionary
responses = {
    "greetings": {
        "hello": ["Hello! How can I assist you today?", "Hi! What's on your mind?", "Hey! I'm here to help."],
        "hi": ["Hi! How are you doing?", "Hey! What's up?", "Hello! How can I help you?"],
        "hey": ["Hey! What's going on?", "Hi! How can I assist you?", "Hello! I'm here to help."],
        "hi there": ["Hi there! How can I help you?", "Hey! What's up?", "Hello! I'm here to assist you."],
        "morning": ["Good morning! How can I help you?", "Morning! What's on your mind?", "Hey! Good morning!"],
        "afternoon": ["Good afternoon! How can I assist you?", "Afternoon! What's up?", "Hey! Good afternoon!"],
        "evening": ["Good evening! How can I help you?", "Evening! What's on your mind?", "Hey! Good evening!"]
    },
    "goodbyes": {
        "bye": ["Goodbye! It was nice chatting with you.", "See you later! Have a great day.", "Bye for now!"],
        "see you later": ["See you later! Have a great day.", "Goodbye! It was nice chatting with you.", "Bye for now!"],
        "goodnight": ["Goodnight! Sweet dreams.", "Nighty night! See you tomorrow.", "Goodbye! Have a great night."],
        "goodbye for now": ["Goodbye for now! It was nice chatting with you.", "See you later! Have a great day.", "Bye for now!"],
        "farewell": ["Farewell! It was nice chatting with you.", "Goodbye! Have a great day.", "See you later!"]
    },
    "thanks": {
        "thank you": ["You're welcome!", "No problem!", "It was my pleasure!"],
        "thanks": ["You're welcome!", "No problem!", "It was my pleasure!"],
        "appreciate it": ["You're welcome!", "No problem!", "It was my pleasure!"],
        "thank you so much": ["You're welcome!", "No problem!", "It was my pleasure!"],
        "i appreciate it": ["You're welcome!", "No problem!", "It was my pleasure!"]
    },
    "apologies": {
        "sorry": ["No need to apologize!", "It's okay, mistakes happen!", "Apology accepted!"],
        "my apologies": ["No need to apologize!", "It's okay, mistakes happen!", "Apology accepted!"],
        "excuse me": ["No need to apologize!", "It's okay, mistakes happen!", "Apology accepted!"],
        "my bad": ["No need to apologize!", "It's okay, mistakes happen!", "Apology accepted!"],
        "i apologize": ["No need to apologize!", "It's okay, mistakes happen!", "Apology accepted!"]
    },
    "basic_questions": {
        "what is your name": ["My name is Chatbot!", "I'm Chatbot, nice to meet you!", "I'm an AI assistant, you can call me Chatbot."],
        "how are you": ["I'm doing well, thanks!", "I'm functioning properly, thanks for asking!", "I'm good, thanks for asking!"],
        "what can you do": ["I can assist with a wide range of tasks, from answering questions to generating text.", "I can help with tasks such as math, coding, and more.", "I'm a general-purpose AI assistant, so I can help with many things!"],
        "who made you": ["I was created by BLACKBOX AI.", "My developers are the team at BLACKBOX AI.", "I'm a product of BLACKBOX AI's research and development."]
    },
    "jokes": {
        "tell me a joke": ["Why was the math book sad? Because it had too many problems.", "Why did the computer go to the doctor? It had a virus!", "What do you call a fake noodle? An impasta!"],
        "make me laugh": ["Why did the scarecrow win an award? Because he was outstanding in his field!", "I told my wife she was drawing her eyebrows too high. She looked surprised.", "Why don't scientists trust atoms? Because they make up everything!"]
    },
    "default": {
        "default": ["I'm not sure I understand. Can you please rephrase?", "I didn't quite catch that. Can you try again?", "Sorry, I'm not sure how to respond to that."]
    }
}

# Define a function to generate a response
def generate_response(user_input):
    # Convert the user input to lowercase
    user_input = user_input.lower()

    # Check if the input matches a response category
    for category, questions in responses.items():
        for question, responses_list in questions.items():
            if question in user_input:
                # Return a random response from the list
                return random.choice(responses_list)

    # If no match is found, return a default response
    return random.choice(responses["default"]["default"])

# Test the generate_response function
while True:
    user_input = input("User: ")
    print("Response:", generate_response(user_input))