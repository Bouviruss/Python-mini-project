from turtle import *

bgcolor("black")
speed(0)
hideturtle()
for i in range(120):
    color("red")
    circle(i)
    color("blue")
    circle(i*0.9)
    right(5)
    forward(5)
done()

