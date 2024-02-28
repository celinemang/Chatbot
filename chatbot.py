import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r'Hi|Hello', ['Hi!', 'Hello!']),
    (r'What\'s your name?| What is your name?', ['I am Chatbot']),
    (r'(what do you like|what do you like to do?)', ['I like to hold a conversation']),
    (r'End', ['See you again']),
    (r'(.*)', ['Could you repeat it again?'])
]

chatbot = Chat(pairs, reflections)
print("Starting the conversation with Chatbot. The conversation will end when you enter 'End'.")
chatbot.converse()
