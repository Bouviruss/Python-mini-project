# imported turtle module
import turtle

wind = turtle.Screen()
wind.title("Ping Pong By BVS")  # the title of window
wind.bgcolor("black")  # color windows background
wind.setup(width=800, height=600)  # resolution 1280/2= 640 -- 720/2= 360
wind.tracer(0)
# midrab 1
midrab1 = turtle.Turtle()
midrab1.speed(0)
midrab1.shape("square")
midrab1.color("red")
midrab1.shapesize(stretch_wid=5, stretch_len=1)
midrab1.penup()
midrab1.goto(-350, 0)

# midrab 2
midrab2 = turtle.Turtle()
midrab2.speed(0)
midrab2.shape("square")
midrab2.color("blue")
midrab2.shapesize(stretch_wid=5, stretch_len=1)
midrab2.penup()
midrab2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("yellow")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1 : 0  Player 2 : 0", align="center", font=("ds-digital",20, "normal"))

#functions movements
def midrab1_up():
    y = midrab1.ycor()
    y += 20
    midrab1.sety(y)
def midrab1_down():
    y = midrab1.ycor()
    y -= 20
    midrab1.sety(y)

def midrab2_down():
    y = midrab2.ycor()
    y -= 20
    midrab2.sety(y)

def midrab2_up():
    y = midrab2.ycor()
    y += 20
    midrab2.sety(y)
#keyboard bindings
wind.listen()
wind.onkeypress(midrab1_up, "q")
wind.onkeypress(midrab1_down, "w")
wind.onkeypress(midrab2_up, "Up")
wind.onkeypress(midrab2_down, "Down")

# main game loop
while True:
    wind.update()  # update screen

    # movement ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1 : {} Player 2 : {}".format(score1, score2), align="center", font=("ds-digital", 20, "normal"))

    if ball.xcor() <-390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1 : {} Player 2 : {}".format(score1, score2), align="center", font=("ds-digital", 20, "normal"))

    # tasadom madrab and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < midrab2.ycor() + 40 and ball.ycor() > midrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < midrab1.ycor() + 40 and ball.ycor() > midrab1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
