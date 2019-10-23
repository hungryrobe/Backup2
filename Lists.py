# Make Lists
#The computer starts counting at 0, so the first item in the list is 0, then the 2nd is 1
myClasses = ['Algrebra', 'English', 'Government']
print(myClasses)

# Add an item to the list
# Append or Insert
# Append will add to the back of the list
myClasses.append('Coding')
print(myClasses)
favClass = input('What is your favorite class? ')
myClasses.append(favClass)
print(myClasses)

#insert
myClasses.insert(3, 'Art')
print(myClasses)

#Overwrite
myClasses[4] = 'Science'
print(myClasses)

#Remove list items
#remove, pop
#remove will remove a specific item, so tell it what you want to take out
myClasses.remove('Science')
print(myClasses)
#pop will remove an item at a specific index
myClasses.pop() #erases the last item
print(myClasses)
myClasses.pop(1) #erases the 2nd item in the list

#len
#len returns the length of a list, so it'll tell you how long the list is
print('myClasses is ' + str(len(myClasses)) + ' items long')

print(myClasses[len(myClasses) -1])

# loop through a list
count = 1
for aClass in myClasses:
	print('item ' + str(count) + ' is ' + aClass)
	count = count + 1


# Classwork below....
Numbers = [1, 3, 5, 7, 9, 11, 13, 15]
total = 0
for Number in Numbers:
	total = total + Number
print(total)


myClasses.append('Cooking')
if 'Cooking' in myClasses:
	print('have fun cooking')
else:
	print('Ok then')