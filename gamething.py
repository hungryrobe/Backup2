import time
import os

frameList = [
'''
| 
 ''','''

|
|  ''','''


| 
|
| ''','''


|
|
|
| ''','''

 ___
|
|
|  
|  ''','''

 ___
|   |
|
|  
|  ''','''

 ___
|   |
|   | 
|
| ''','''

 ___
|   |
|___|
|   
| ''','''

 ___
|   |
|___|
| \\
|  
  ''','''
 ___
|   |
|___|
| \\
|  \\

'''	
]


while True:
	for frame in frameList:
		os.system('cls')
		print(frame)
		time.sleep(.5)