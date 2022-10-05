import turtle #1. import modules
import random
import math
import pygame
#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
ranRange1 = random.randrange(1,101)
ranRange2 = random.randrange(1,101)
michelangelo.forward(ranRange1)
leonardo.forward(ranRange2)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
ranRange3 = random.randrange(1,11)
ranRange4 = random.randrange(1,11)
for i in range(10):
  michelangelo.forward(ranRange3)
  leonardo.forward(ranRange4)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# PART B - complete part B here
pygame.init()
screen = pygame.display.set_mode()
numSides = [3,4,6,9,360]
side_length = 100
offset = 200
for i in numSides:
  screen.fill("black")
  coords = [(0,0),(0,0)] * i
  for n in range(i):
    theta = (2 * math.pi * (n)) / i
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords[n] = (x,y)
    pygame.draw.polygon(screen, "blue", coords)
    pygame.display.flip()
    pygame.time.wait(100)

