# Name: Ben Strauss
# Period: 6
# Dice Rolling Simulator
import random 
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

x = 1
numRolls = int(input('How Many Rolls?: '))

while x <= numRolls:
	randomNum = random.randint(1, 6)
	print(str(x) + ": " + str(randomNum))
	x += 1
	if randomNum == 1:
		num1 += 1
	elif randomNum == 2:
		num2 += 1
	elif randomNum == 3:
		num3 += 1
	elif randomNum == 4:
		num4 += 1
	elif randomNum == 5:
		num5 += 1
	elif randomNum == 6:
		num6 += 1

print('number of 1s: ' + str(num1))
print('number of 2s: ' + str(num2))
print('number of 3s: ' + str(num3))
print('number of 4s: ' + str(num4))
print('number of 5s: ' + str(num5))
print('number of 6s: ' + str(num6))

print(str(num1 / x * 100))
print(str(num2 / x * 100))
print(str(num3 / x * 100))
print(str(num4 / x * 100))
print(str(num5 / x * 100))
print(str(num6 / x * 100))