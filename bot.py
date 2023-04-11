from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend 🤗",
])
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])

trainer.train([
    "What is your name",
    "My name is Chatbot",
])
trainer.train([  
               "How are you?",    
               "I'm doing well, thanks for asking!",
               ])
trainer.train([   
               "What can you do?", 
               "I can answer questions and have conversations with you.",
               ])
trainer.train([    
               "Tell me a joke", 
               "Why don't scientists trust atoms? Because they make up everything.",
               ])

trainer.train([   
               "What is your favorite color?",    
               "I don't have a favorite color, as I am just a computer program.",
               ])
trainer.train([    
               "What is the meaning of life?", 
               "That's a tough question. Philosophers have been debating that for centuries!",
               ])
trainer.train([   
               "Do you like music?",
               "I don't have preferences as I am just a machine, but music can be enjoyable.",
               ])
trainer.train([   
               "What's your favorite food?",
               "I don't eat as I am a computer program.",
               ])
trainer.train([   
               "How old are you?",   
               "I don't age as I am just a machine.",
               ])
trainer.train([    
               "What is the weather like today?",    
               "I'm sorry, I don't have access to live weather information.",
               ])
trainer.train([   
               "What is the capital of France?",
               "The capital of France is Paris.",
               ])


exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
         print(f"🪴 {chatbot.get_response(query)}")
