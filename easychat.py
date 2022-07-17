import csv
from urllib import response
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app=Flask(__name__)

chatbot = ChatBot('Vitchat')


conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)
@app.route("/")
def home():    
    return render_template("chat.html") 
# use http://127.0.0.1:5000/chatbot1 -- to send message from chatbot1
@app.route("/chatbot1")
def home1():    
    return render_template("chat1.html") 
# use http://127.0.0.1:5000/chatbot2 -- to send message from chatbot2
@app.route("/chatbot2")
def home2():    
    return render_template("chat2.html") 
# use http://127.0.0.1:5000/chatbot3 -- to send message from chatbot3
@app.route("/chatbot3")
def home3():    
    return render_template("chat3.html") 
# use http://127.0.0.1:5000/chatbot4 -- to send message from chatbot4
@app.route("/chatbot4")
def home4():    
    return render_template("chat4.html")
# use http://127.0.0.1:5000/chatbot5 -- to send message from chatbot5
@app.route("/chatbot5")
def home5():    
    return render_template("chat5.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')
    # to store the messages sent by chatbot 1
    with open('./chatbot1.txt', mode='a', encoding='utf-8') as file:
        # file.writelines("%s\n" % t for t in userText)
        file.writelines(userText+ '\n' )
    a=str(chatbot.get_response(userText))
    # to store the response messages of chatbot3 that is sent to chatbot1
    with open('./chatbot3.txt', mode='a', encoding='utf-8') as file:
        # file.writelines("%s\n" % t for t in userText)
        file.writelines(a+ '\n' )
    return a

if __name__ == "__main__":    
    app.run()