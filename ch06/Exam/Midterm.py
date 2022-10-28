import turtle
import math
window = turtle.Screen()
window.setup(1920,1080)
turtleDrawing = turtle.Turtle()
def febseq():
    num1 = 25
    num2 = 0
    num = 0
    while num < 25:
        num = num1 + num2
        print(num)
        num1 = num2
        num2 = num
def goldenratio():
    forward1 = 25
    forward2 = 0
    placeHoldernum = 0
    while placeHoldernum < 850:
        placeHoldernum = forward1 + forward2
        if placeHoldernum == 25:
            for i in range(4):
                turtleDrawing.forward(placeHoldernum)
                turtleDrawing.left(90)
        elif placeHoldernum ==50:
            turtleDrawing.penup()
            turtleDrawing.setposition(placeHoldernum-forward1,placeHoldernum-forward1)
            turtleDrawing.pendown()
            turtleDrawing.right(180)
            for i in range(4):
                turtleDrawing.forward(placeHoldernum)
                turtleDrawing.right(90)
        elif placeHoldernum==75:
            turtleDrawing.penup()
            turtleDrawing.setposition(0,placeHoldernum-forward2)
            turtleDrawing.pendown()
            turtleDrawing.right(180)
            for i in range(4):
                turtleDrawing.forward(placeHoldernum)
                turtleDrawing.right(90)
        elif placeHoldernum ==125:
            turtleDrawing.penup()
            turtleDrawing.setposition(-0,forward1-forward2)
            turtleDrawing.pendown()
            turtleDrawing.right(180)
            for i in range(4):
                turtleDrawing.forward(placeHoldernum)
                turtleDrawing.right(90)
        elif placeHoldernum == 200:
            turtleDrawing.right(180)
            turtleDrawing.penup()
            turtleDrawing.setposition(-forward2,-225)
            turtleDrawing.pendown()
            turtleDrawing.right(180)
            for i in range(4):
                turtleDrawing.forward(placeHoldernum)
                turtleDrawing.right(90)
        elif placeHoldernum ==325:
            turtleDrawing.penup()
            turtleDrawing.setposition(75,-225)
            turtleDrawing.pendown()
            for i in range(4):
                turtleDrawing.forward(placeHoldernum)
                turtleDrawing.left(90)
        elif placeHoldernum ==525:
            turtleDrawing.penup()
            turtleDrawing.setposition(forward1-forward2,100)
            turtleDrawing.pendown()
            turtleDrawing.right(180)
            for i in range(4):
                turtleDrawing.forward(placeHoldernum)
                turtleDrawing.right(90)
        elif placeHoldernum ==850:
            turtleDrawing.penup()
            turtleDrawing.setposition(-975,625)
            turtleDrawing.pendown()
            for i in range(4):
                turtleDrawing.forward(placeHoldernum)
                turtleDrawing.right(90)
        turtleDrawing.right(90)
        forward1 = forward2
        forward2 = placeHoldernum
def curve():
    forward1 = 25
    forward2 = 0
    placeHoldernum = 0
    factor=1
    turtleDrawing.penup()
    turtleDrawing.setposition(25, 25)
    turtleDrawing.pendown()
    turtleDrawing.right(90)
    for i in range(850):
        print(forward1)
        fdwd = math.pi * forward1 * factor / 2
        fdwd /= 90
        for j in range(90):
            turtleDrawing.forward(fdwd)
            turtleDrawing.left(1)
        placeHoldernum = forward2
        forward2 = forward1
        forward1 = placeHoldernum + forward1
        
        
goldenratio()
curve()
window.exitonclick()
