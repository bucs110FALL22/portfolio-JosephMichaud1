import turtle #1. import modules
import random

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
a = random.randrange(1,101)
b = random.randrange(1,101)
michelangelo.forward(a)
leonardo.forward(b)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
x = random.randrange(1,11)
y = random.randrange(1,11)
for i in range(10):
  michelangelo.forward(x)
  leonardo.forward(y)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# PART B - complete part B here
import math
import pygame
pygame.init()
screen = pygame.display.set_mode()
coords = [x,y]
num_sides = 3
side_length = 50
offset = 50
for i in range(3):
  theta = (2.0 * math.pi * (i + 1)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
pygame.draw.polygon(surface)
  



window.exitonclick()
