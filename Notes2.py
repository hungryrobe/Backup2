#Conditionals
print('Welcome to Ticket Bot')
print('You must be at least 18 to see R rated movies')
age = int(input('How old are you? '))

if age > 17:
	print('You can go see an R rated movie')
else:
	print('You cannot go see an R rated movie')

print('Thank You')

mysteryNum = 6
guess = int(input('Guess a number between 1 and 10: '))

if guess == mysteryNum:
	print('Good guess, you are correct!')
elif guess > 10:
	print('Burh I said a number bewteen 1 and 10')
elif guess > mysteryNum:
	print('Too High')
else:
	print('Too Low')

#Conditional operators: >, <, >=, <=, == (is equal to), != (is not equal to)

bday = input('Is today your birthday(yes/no): ')
if bday == 'yes' or bday == 'Yes'
	print("happy birthday!")
elif bday == 'no' or bday == 'No'
	print('have a good day anyway!')
else:
	print('Please read directions')