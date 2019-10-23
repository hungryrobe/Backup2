print('Welcome to the To Do list ;-)')
todoList = []
while True:
	print('Enter a to add an item')
	print("Enter r to remove an item")
	print('Enter p to print the list')
	print('Enter q to quit')
	choice = input('Make your choice: ')

	if choice == 'q':
		break
	
	elif choice == 'a':
		additem = input()
		todoList.append(additem)
		print(todoList)
		
	elif choice == 'r':
		takeout = input()
		todoList.remove(takeout)

	elif choice == 'p':
		count = 1
		for additem in todoList:
			print("Task " + str(count) + ': ' + additem)
			count = count + 1
	else:
		print('This was not a choice')

