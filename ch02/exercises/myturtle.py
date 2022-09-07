from re import M
import turtle
MyTurtle = turtle.Turtle()
Window = turtle.Screen()
MyTurtle.shape("turtle")
MyTurtle.color("purple")
Length = 50
for i in range (4):
    MyTurtle.forward(50)
    MyTurtle.left(90)
MyTurtle.up()
MyTurtle.backward(100)
MyTurtle.color("red")
MyTurtle.down()
for i in range (4):
    MyTurtle.forward(50)
    MyTurtle.left(90)
Window.exitonclick()