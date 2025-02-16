class BaseAI:
    def __init__(self):
        self.memory = {}
    
    def process_input(self, user_input):
        # Process the user input and make decisions
        response = self.generate_response(user_input)
        return response
    
    def generate_response(self, user_input):
        # Simple response generation logic
        if "hello" in user_input.lower():
            return "Hello! How can I assist you today?"
        elif "help" in user_input.lower():
            return "I'm here to help! What do you need assistance with?"
        else:
            return "I'm not sure how to respond to that."
    
    def learn(self, user_input, user_response):
        # Store user interactions for future reference
        self.memory[user_input] = user_response
    
    def get_memory(self):
        # Retrieve the memory of interactions
        return self.memory