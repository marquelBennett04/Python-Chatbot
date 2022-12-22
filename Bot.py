import sys

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Creating the new bot
chatbot = ChatBot("My Bot")

#Training the bot
bot_trainer = ChatterBotCorpusTrainer(chatbot)
bot_trainer.train(
    "chatterbot.corpus.english"
)

#Testing the bot
print("enter 'quit' to stop")
while True:
    user_input = input("You: ")
    if user_input == 'quit':
            break
print("Bot:", chatbot.get_response(user_input))