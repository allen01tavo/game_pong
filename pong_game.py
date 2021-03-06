# Simple Pong in Python 3 for Beginners
# Python version 3.9.1
# by @Maturana
# Part 1



import turtle
import os
import logging
import os.path


# Global Variables
game_on = True

# End of Global Variables

# Main Window
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("brown")
wn.setup(width= 800, height=600)
wn.tracer(0)

# First Layer: Players

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()   
paddle_b.goto(350,0)
#End 

# Second Layer: Field of play
# Field
border= turtle.Turtle()
border.speed(0)
border.shape("square")
border.shapesize(stretch_wid=24.1,stretch_len=32.1)
border.color("white")
border.penup()
border.goto(0,0)

field_ = turtle.Turtle()
field_.speed(0)
field_.shape("square")
field_.shapesize(stretch_wid=24,stretch_len=32)
field_.color("green")
field_.penup()
field_.goto(0,0)

border_2= turtle.Turtle()
border_2.speed(0)
border_2.shape("square")
border_2.shapesize(stretch_wid=18.1,stretch_len=32.1)
border_2.color("white")
border_2.penup()
border_2.goto(0,0)

border_3= turtle.Turtle()
border_3.speed(0)
border_3.shape("square")
border_3.shapesize(stretch_wid=18,stretch_len=32)
border_3.color("green")
border_3.penup()
border_3.goto(0,0)

border_4= turtle.Turtle()
border_4.speed(0)
border_4.shape("square")
border_4.shapesize(stretch_wid=18.1,stretch_len=19.1)
border_4.color("white")
border_4.penup()
border_4.goto(0,0)

border_5= turtle.Turtle()
border_5.speed(0)
border_5.shape("square")
border_5.shapesize(stretch_wid=18,stretch_len=19)
border_5.color("green")
border_5.penup()
border_5.goto(0,0)
# End of Second Layer

#Paddle Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()   
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

# Field
field = turtle.Turtle()
field.speed(0)
field.shape("square")
field.shapesize(stretch_wid=26,stretch_len=0.1)
field.color("white")
field.penup()
field.goto(0,0)

field = turtle.Turtle()
field.speed(0)
field.shape("square")
field.shapesize(stretch_wid=0.01,stretch_len=19)
field.color("white")
field.penup()
field.goto(0,0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions

def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)

# Displays game over after Player A or Player B wins
def game_over():
	banner_ = turtle.Turtle()
	banner_.speed(0)
	banner_.shape("square")
	banner_.color("white")
	banner_.penup()
	banner_.hideturtle()
	banner_.goto(0,0)
	banner_.write("GAME OVER", align="center", font=("Courier", 52, "normal"))
	ball.setx(50)
	ball.sety(50)

def score_win(A,B):
	if A == 10 or B == 10:
		pen.clear() # clears the pen
		if A > B:
			pen.write("Player A: {}".format("Wins"), align="center", font=("Courier", 32, "normal"))
		else:
			pen.write("Player B: {}".format("Wins"), align="center", font=("Courier", 32, "normal"))
		game_over()


def game():
	
	# Score
	score_a = 0
	score_b = 0
	

	# Keyboard bindings
	logging.info(wn.listen())

	wn.onkeypress(paddle_a_up, "w")
	wn.onkeypress(paddle_a_down, "s")
	wn.onkeypress(paddle_b_up, "Up")
	wn.onkeypress(paddle_b_down,"Down")
	# End of Keyboard bindings

	while game_on:
		
		wn.update() # update must be kept in order for the graphics to show
			
		# Move the ball
		ball.setx(ball.xcor() + ball.dx/3)# speed is reduced to 25% by dividing ball.dx/4
		ball.sety(ball.ycor() + ball.dy/3)# spdee is reduced to 25% by dividing ball.dx/4
		
		# Border checking
		
		# Top and bottom
		if ball.ycor() > 290:
			ball.sety(290)
			ball.dy *= -1
			os.system("afplay bounce.wav&")
	
		if ball.ycor() < -290:
			ball.sety(-290)
			ball.dy *= -1
			os.system("afplay bounce.wav&")
	
		# Left and right
		if ball.xcor() > 350:
			score_a += 1
			pen.clear()
			pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
			ball.goto(0,0)
			ball.dx *= -1
	
		if ball.xcor() < -350:
			score_b += 1
			pen.clear()
			pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
			ball.goto(0,0)
			ball.dx *= -1
	
		# Paddle and ball collisions
		if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50:
			ball.dx *= -1
			logging.info(os.system("afplay bounce.wav&"))
	
		if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
			ball.dx *= -1
			logging.info(os.system("afplay bounce.wav&"))
	
		# Displays game over and who wins the game
		score_win(score_a,score_b)
		# End of game
	# end of log is never called	

# logger is not working propperly	
def logger(x):
	# remove file if file exists
	logging.basicConfig(filename='pong.log',format='%(asctime)s :: %(levelname)s :: %(message)s')
	
	"""
	if os.path.exists('pong.log'):
		os.remove('pong.log')
		logging.basicConfig(filename='pong.log',format='%(asctime)s :: %(levelname)s :: %(message)s',level=logging.INFO)
	# create file if file does not exists
	if not os.path.exits('pong.log'):
		logging.basicConfig(filename='pong.log',format='%(asctime)s :: %(levelname)s :: %(message)s',level=logging.INFO)
	"""
	logging.info('Log Started')
	logging.info(x)

def main():	

	logger(game())
	logging.info("log ended")

# calling main function
if __name__ == "__main__":
	
	main()	
	
	
#end of code
