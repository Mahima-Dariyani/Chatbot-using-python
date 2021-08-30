import time
import os
import webbrowser


today = time.ctime()
print(today)
name=input("Hello My Name is Ana. what's your name : ")
print(f"Hello {name}\n")

services="\nSearch\nMake me Laugh\nSearch Image\n"
serv = {"search":"google search","make me laugh":"https://www.google.co.in/search?q=jokes&hl=en&tbm=isch","search image":"Which Image",}




bot = {
    "who are you?":"My name is Ana! I am your personal ChatBot",
    "how are you?":"absolutely fine! What about you?",
    "services":"I provide theses services :\n"+services,
    "father of python":"Guido van Rossum is known as Father of Python Programming language",
    "what kind of music do you like?":"i love rock music",
    "today's date and time": today,
    "what type of language you use?":"English! and I was written in Python Programming language.",
}


while True:

    ques = input("How can I help you "+name+" : ")
    ques=ques.lower()
    if(ques == "quit" ):
        print("See you soon, Bye")
        break

    elif ques in bot.keys():
        print(bot[ques])

    elif ques in serv.keys():
        if ques=="search":
            webbrowser.open("https://www.google.com/search?q="+input('what to search : '))
            
        elif(ques=="search image"):
            webbrowser.open("https://www.google.co.in/search?q="+input("Which Image to search : ")+"&hl=en&tbm=isch")
        else:
            webbrowser.open(serv[ques])
            
    else:
        print("Sorry I can't help you with this\nI am new to this world and learning new things\nHere is a list of things I know\n")
        for ik in bot.keys():
            print(ik+"\n")
