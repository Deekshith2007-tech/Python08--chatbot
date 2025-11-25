print("🤖 Chatbot: Hello! I am your simple chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()   

    if user_input == "hello" or user_input == "hi":
        print("🤖 Chatbot: Hello! How can I help you today?")

    elif user_input == "how are you":
        print("🤖 Chatbot: I'm just code, but I'm doing great!")

    elif user_input == "what is your name":
        print("🤖 Chatbot: I am a rule-based chatbot created using Python.")

    elif user_input == "bye":
        print("🤖 Chatbot: Goodbye! Have a nice day 😊")
        break

    else:
        print("🤖 Chatbot: Sorry, I don't understand. Can you try again?")