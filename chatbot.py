# Import necessary libraries
import os
from pathlib import Path

# Define a list of FAQs and their responses
faqs = {
    "What is your name?": "I am an adaptive chatbot.",
    "How can you help me?": "I can answer your questions based on your previous interactions.",
    "What is AI?": "AI stands for Artificial Intelligence."
}

# Function to get a response from the chatbot
def get_response(user_input):
    # Convert user input to lowercase and strip any leading/trailing whitespace
    user_input_lower = user_input.lower().strip()
    print(f"Debug: User input processed - '{user_input_lower}'")  # Debugging statement
    
    # Check predefined FAQs
    for question, answer in faqs.items():
        if user_input_lower in question.lower():
            return answer
    
    # Check for learned interactions
    positive_interactions_path = Path("positive_interactions.txt")
    if positive_interactions_path.exists():
        with positive_interactions_path.open("r") as f:
            positive_interactions = [line.lower().strip() for line in f]
        print(f"Debug: Positive interactions read from file - {positive_interactions}")  # Debugging statement
        
        # Check if user input exists in positive interactions
        if user_input_lower in positive_interactions:
            print(f"Debug: '{user_input_lower}' found in positive interactions")  # Debugging statement
            return "I'm glad you asked that again!"
        else:
            print(f"Debug: '{user_input_lower}' not found in positive interactions")  # Debugging statement
    
    return "I'm sorry, I don't understand that question."

# Function to simulate learning from user interactions
def learn_from_interaction(user_input, feedback):
    user_input_lower = user_input.lower().strip()
    if feedback.lower() == "yes":
        with open("positive_interactions.txt", "a") as f:
            f.write(f"{user_input_lower}\n")
        print(f"Debug: Added to positive interactions - '{user_input_lower}'")  # Debugging statement
    else:
        with open("negative_interactions.txt", "a") as f:
            f.write(f"{user_input_lower}\n")
        print(f"Debug: Added to negative interactions - '{user_input_lower}'")  # Debugging statement

# Main loop to interact with the user
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = get_response(user_input)
    print("Bot:", response)
    feedback = input("Was this response helpful? (yes/no): ")
    learn_from_interaction(user_input, feedback)









