import random
import turtle
coinFlip = random.randint(1,3)
randomTurtle = turtle.Turtle()
window = turtle.Screen()
forward = 0
backward = 0
while forward or backward != 200:
  if coinFlip == 1:
    for i in range(4):
      randomTurtle.forward(50)
      forward += 50
      print("Tails")
    break
  else:
    randomTurtle.backward(50)
    backward += 50
    print("Heads")



window.exitonclick()