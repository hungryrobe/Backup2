from turtle import *
scoreturt = Turtle()
screen = getscreen()
scoreturt.penup()
scoreturt.goto(screen.window_width() / 2 - 200, screen.window_height()/2-50)
scoreturt.hideturtle()

score = 0

gameturt = Turtle()

def updateScore():
	scoreturt.clear()
	scoreturt.write('Score: ' + str(score), False, 'left', font=('Arial', 20, 'normal'))
updateScore()

screen.mainloop()