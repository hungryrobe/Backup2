#Ben Strauss
#Rock Paper Scissors (rps)
#Added comment for Github
import random

#Variables
pScore = 0
cScore = 0
ties = 0
cMoves = ['rock', 'paper', 'scissors']

#Welcome message
print('Welcome to rock paper Scissors')

#prompt for name
pName = input('What is your name? ')


#Score tracker
def printScore():

#prints score
	print('Score: ')
#Shows player score
	print(pName + ': ' + str(pScore))
#Shows computer score
	print('Computer Score: ' + str(cScore))

	#Show how many ties
	print('Ties: ' + str(ties))

#Game Loop
#Loop until q is entered
while True:
	#prompt for player move (r, p, s, q)
	pMove = input('Enter "r" for Rock, "p" for paper, "s" for scissors or "q" to quit')
#print the score
	printScore()
#Check if q is entered, if so, end the game
	if pMove == 'q': 
		break
#Get a computer move (random)
	if cMove == random.choice(cMoves):
#compare player move with the computer move
	#Player picks rock
	if pMove == 'r':
		print(pName + ' picked Rock')
		if cMove == 'rock':
			print('Computer picks Rock')
			print('Tie')
			ties += 1
		elif cMove == 'paper':
			print('Computer picks paper')
			cScore += 1
		else:
			print('Computer picks Scissors')
			pScore += 1
#Player picks paper
	elif pMove == 'p':
		print(pName + ' picked Paper')
		if cMove == 'rock':
			print('Computer picks Rock')
			print('paper covers rock')
			ties += 1
		elif cMove == 'paper':
			print('Computer picks paper')
			print('Tie')
			cScore += 1
		else:
			print('Computer picks Scissors')
			print('Scissors cuts paper')
			pScore += 1
#player picks scissors
	elif pMove == 's':
		print(pName + ' picked Scissors')
		if cMove == 'rock':
			print('Computer picks Rock')
			print('rock breaks scissors')
			ties += 1
		elif cMove == 'paper':
			print('Computer picks paper')
			print('scissors cuts paper')
			cScore += 1
		else:
			print('Computer picks Scissors')
			print('Tie')
			pScore += 1
#Check is pMove is valid
	else:
		print('That is not an option')