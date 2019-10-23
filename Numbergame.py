import random

mysteryNum = random.randint(1, 100)
score = 0 

while True:
	guess = int(input('Guess number between 1 and 100: '))
	score += 1 #The same as score = score + 1
	if guess == mysteryNum:
		print('Nice job!')
		break 
	elif guess > mysteryNum:
		print('Too High!')
	else:
		print('Too low')

print('You took ' + str(score) + ' guesses')