import turtle

wn = turtle.Screen() #assigning variable to the object (screen)
wn.title('Pong: by yours truly')
wn.bgcolor('black')
wn.setup(width=800, height=600) #sets up size of screen to be played on
wn.tracer(0) #makes game run faster

#score
score_a = 0
score_b = 0



#creating paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0) #sets speed to max
paddle_a.shape('square')
paddle_a.color('blue')
paddle_a.penup() #turtle objects draw lines behind them by default (we dont want that)
paddle_a.goto(-350, 0) #paddle starting location
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0) #sets speed to max
paddle_b.shape('square')
paddle_b.color('red')
paddle_b.penup() #turtle objects draw lines behind them by default (we dont want that)
paddle_b.goto(350, 0) #paddle starting location
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#ball
ball = turtle.Turtle()
ball.speed(0) #sets speed to max
ball.shape('circle')
ball.color('green')
ball.penup() #turtle objects draw lines behind them by default (we dont want that)
ball.goto(0, 0) #ball starting location
ball.dx =5 #speed at which ball movies in positive x direction
ball.dy =5 #speed of ball positive y direction

#functions (for moving paddles and stuff)
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)



#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")





#main game loop
while True:
    wn.update() #when game starts, window refreshes

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  #reverses direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #starting game over
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() > 390:
        score_a += 1
        pen.write(f'Player 1: {score_a} Player 2: {score_b}', align='center', font=('courier', 24, 'normal'))
    if ball.xcor() < -390:
        score_b += 1
        pen.write(f'Player 1: {score_a} Player 2: {score_b}', align='center', font=('courier', 24, 'normal'))

    #right paddle and ball collision
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1

    #scoring (pen)
    pen = turtle.Turtle()
    pen.speed(0) #animation speed
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(f'Player 1: {score_a} Player 2: {score_b}', align='center', font=('courier', 24, 'normal'))
