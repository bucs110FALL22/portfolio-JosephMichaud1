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
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
pygame.draw.polygon(screen, (0, 255, 255), ((25,75),(320,125),(250,375)))
pygame.display.flip()
pygame.time.wait(100)
screen.fill((255, 255, 255))
pygame.display.flip()
pygame.draw.polygon(screen,(225,0,0), ())
pygame.display.flip()
pygame.quit()

window.exitonclick()
