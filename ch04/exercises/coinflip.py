import random
import turtle
randomTurtle = turtle.Turtle()
window = turtle.Screen()
forward = 0
backward = 0
while forward or backward != 200:
  coinFlip = random.randint(1,3)
  if coinFlip == 1:
      randomTurtle.forward(50)
      forward += 50
      print("Tails")
  else:
    randomTurtle.backward(50)
    backward += 50
    print("Heads")



window.exitonclick()