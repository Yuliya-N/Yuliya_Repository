from random import randint
from math import log, ceil

limit = int(input('Enter upper bounder: '))
# tries = int(input('Enter number of tries: '))

goal = randint(0,limit)
tries = int(ceil(log(limit, 2)))
if limit%2 == 0:
		tries +=1

print('Your number of tries is: ', tries)
guesses = set() # set is faster


while len(guesses) < tries:
	guess = int(input('Guess the number: '))
		#if not guess in guesses: -- set has unique values
	#if guess not in guesses: -- upper is ore correct for programming lang
	guesses.add(guess)

	if guess < goal:
		print('Goal is bigger')	
	elif guess > goal:
		print ('Goal is less')		
	else:
		print('Guess is right')
		break
else:
	print ("Game's over you loose!!!")

