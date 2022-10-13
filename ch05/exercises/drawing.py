import turtle
window = turtle.Screen()
turtleObject = turtle.Turtle()
def drawEqShape():
    for i in range(numSides):
        turtleObject.left(numSides/360)
    turtleObject.forward(sideLengh)
numSides = int(input("How many sides do you want?: "))
sideLengh = int(input("What do you want the side lengh to be?: "))


turtle.exitonclick
