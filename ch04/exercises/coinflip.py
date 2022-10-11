import random
import turtle
randomTurtle = turtle.Turtle()
window = turtle.Screen()
window.setup(400,400)
headsPos = 0
tailsPos = 0
while tailsPos != 400 or headsPos != 400:
  coinFlip = random.randint(0,1)
  if coinFlip == 1:
    randomTurtle.forward(50)
    print("Tails")
    tailsPos += 50
    print(tailsPos)
  else:
    randomTurtle.backward(50)
    print("Heads")
    headsPos += 50
    print(headsPos)



window.exitonclick()