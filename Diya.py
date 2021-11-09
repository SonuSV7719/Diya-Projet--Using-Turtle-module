from turtle import *
import turtle

t = turtle.Turtle()
t.fillcolor("orange")
t.begin_fill()
print(t.position())
t.penup()
t.goto(-200, 0)
t.pendown()
t.forward(400)
t.left(-270)
t.circle(200, -180)
t.end_fill()
t.penup()
t.goto(200,0)

t.up()
t.pendown()
# for first side of diya  light
t.fillcolor("yellow")
t.begin_fill()
t.right(20)
t.forward(-100)
t.right(-20)
t.forward(-50)
t.left(20)
t.forward(-100)
#for second side of diyas light
t.right(40)
t.forward(100)
t.right(-20)
t.forward(50)
t.left(20)
t.forward(100)

t.end_fill()
t.penup()
t.goto(0, -250)
t.hideturtle()

t.write("Happy Diwali", align="center", font="50")

turtle.done()
