import turtle
myTurtle = turtle.Turtle()
window = turtle.Screen()
numOfSides = int(input("How many sides do you want your shape to be?: "))
lengthOfSides = int(input("How long do you want your sides to be?: "))
colorOfTurtle = input("What color do you want the turtle to be?: ")
myTurtle.color(colorOfTurtle)
myTurtle.shape(numOfSides, lengthOfSides)
window.exitonclick()