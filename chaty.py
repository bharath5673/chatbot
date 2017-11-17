import random
import time

a = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey','cool!']
b = ['sorry,.... my responses are limited, ask me right question','I did not understand what you said']
t = ['yup its time','time?','time!',"it's time 4.20!,time to roll on'"]
random_greeting = random.choice(a)
random_time = random.choice(t)

question = ['How are you?','How are you doing?','wassup','cool']
responses = ['Okay',"I'm fine",'nothing much','jus chillin!']
random_response = random.choice(responses)

question1 = ['name?','your name?','what is your name']
responses1 = ['my name is lisa',"my name is sophia",'my name is VIKI']
random_response1 = random.choice(responses1)

question2 = ['what is the time now']
responses2 =('now the time is',(time.asctime()))

question3 =['your gender','your sexuality','gender?']
responses3 = ("i'm mechasexual")

question4 = ['fuck','fuck off','what the fuck','f','F','sex']
responses4 = ('invalid input')

question5 = ['i love you','love you','love u','do you love me?','marry me','love me']
responses5 = ['love you too','i too love you','me too','i do love u','sure']
random_response5 = random.choice(responses5)

while True:
	userInput = input(">>> ")
	if userInput in a:
		print(random_greeting)
	elif userInput in t:
		print(random_time)
	elif userInput in question:
		print(random_response)
	elif userInput in question1:
		print(random_response1)
	elif userInput == "what is VIKI?" or userInput == "VIKI?":
		print ("VIKI : Virtual Interactive Kinetic Intelligence. ,..have u seen the movie I,Robot? ,its me!")
	elif userInput in question2:
		print(responses2)
	elif userInput in question3:
		print(responses3)
	elif userInput in question4:
		print(responses4)
	elif userInput in question5:
		print(random_response5)
	elif userInput == "sophia?" or userInput == "u r sophia?":
		print("yup' sophia!.. a new citizen of Saudi Arabia")
	elif userInput == 'quit':
		break
	else:
		print(random.choice(b))