import os

Hman = ['''

 +---+
   	 |
	 |
	 |
	  
	  ''','''

 +---+
 0	 |
 	 |
 	 |

 	  ''','''

 +---+
 0	 |
 |	 |
	 |
      
      ''','''

 +---+
 0	 |
 |	 |
/	 |

 	  ''','''

 +---+
 0	 |
 |	 |
/ \\ |

	  ''','''

 +---+
 0	 |
 |\\ |
/ \\ |

 	  ''','''

 +---+
 0	 |
/|\\ |
/ \\ |

 	  '''




]

misses = 0



myWord = 'griffin'
gWord = ['_', '_', '_', '_', '_', '_', '_']

pGuess = input('Guess a letter: ')


for pGuess in gWord 

if pGuess == 'g':
	gWord[0] = 'g'
	print(gWord)
elif pGuess == 'r':
	gWord[1] = 'r'
	print(gWord)
elif pguess == 'i':
	gWord[2, 5] = 'i'
	print()
elif pGuess == 'f':
	gWord[3, 4] = 'f'
elif pGuess == 'n':

else:
	misses = misses + 1






