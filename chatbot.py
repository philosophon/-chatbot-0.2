import random

greetings=["hello","hey","wassup"]
responses=["hi", "bonjour","hallo"]

questions=["how are you?", "how you doin"]
answer=["good","okay","fine"]

jokee=["tell me a joke"]
aanswer=["What’s the best thing about Switzerland?I don’t know, but the flag is a big plus. ","Why do we tell actors to “break a leg?Because every play has a cast."]

weather=["whats the weather", "whats the weather?"]
waatar=["why you asking me?! im not the weatherman!", "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuhhhhhhhhhhhhhhhhhhhhhhhh....  ....I dont know?"]

number=["tell me a random number"]
numer=["1","2","3","4","5","6","7","8","9","10"]

retur=["end","stop"]

while True:
	ask=input(">>>")
	if ask in greetings:
		randomResponse=random.choice(responses)
		print(randomResponse)
	elif ask in questions:
		randomResponse=random.choice(answer)
		print(randomResponse)
	elif ask in jokee:
		randomResponse=random.choice(aanswer)
		print(randomResponse)
	elif ask in weather:
		randomResponse=random.choice(waatar)
		print(randomResponse)
	elif ask in number:
		randomResponse=random.choice(numer)
	elif ask in retur:
		break

	else:
		print("what?")
