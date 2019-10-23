#Ben Strauss
#period 6

#Variable declaration and assignment
myVariable = 'Strauss' #String variable
myNumber = 12 #Integer Variable
myDecimal = 2.4 #Float variable

Bruh = 'Haha'


#While Loops
x = 1
while x <= 10:
	print(x)
	x += 1


x = 100
while x >= 1:
	print(x)
	x -= 1

#String Concatenation (combine)
string1 = 'hello'
string2 = 'world'
print(string1 + string2) 


favMovie = 'Revenge of the Sith'
print('My favorite movie is ' + favMovie)



#Input
yourName = input('What is your name?: ')
print('hello ' + yourName)



favSong = 'Final destination theme'
print('My favorite song is ' + favSong)


#Casting (change one type into another)
myNum = input('Enter a number: ') #myNum is a string type
myNum = int(myNum) + 10 #myNum is now a integer
print('The answer is ' + str(myNum)) 


num1 = input('Enter a number: ')
num2 = input('Enter a number: ')
myNum = int(num1) + int(num2)
print('The answer is ' + str(myNum))


#if and if/else
num = int(input('What is your number?: '))

if num > 100:
	print('yeet')
elif num == 100:
	print('UwU')
else:
	print('Bruh')


bday = input('Is it your birthday?: ')

if bday == 'no':
	print('KOBE!')
else bday == 'yes':
	print('Uhh')