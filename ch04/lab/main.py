import pygame
import random
import math
pygame.init()
window = pygame.display.set_mode((500,500))
#makes player color choice
window.fill((0,0,225))
pygame.draw.rect(window,(0,250,175),[75,100,150,150],0)
pygame.draw.rect(window,(200,0,250),[300,100,150,150],0)
pygame.display.update()
colorChoice = input("Would you like to be team green or team purple: ")
#makes dart board
pygame.draw.circle(window,(225,0,0),[250,250],250,0)
pygame.draw.line(window,(0,0,0,),[0,250],[500,250],2)
pygame.draw.line(window,(0,0,0,),[250,0],(250,500),2)
pygame.display.update()
#makes darts
for i in range(10):
    dartWhereX = random.randrange(0,500)
    dartWhereY = random.randrange(0,500)
    distance_from_center = math.hypot(dartWhereX-250, dartWhereY-250)
    is_in_circle = distance_from_center <= 500/2
    if is_in_circle == True:
        pygame.draw.circle(window,(225,225,255),[dartWhereX,dartWhereY],5,0)
    else:
        pygame.draw.circle(window,(0,0,0),[dartWhereX,dartWhereY],5,0)
pygame.display.update()
pygame.time.wait(5000)