from tkinter import EventType
import pygame
import random
import math
pygame.init()
window = pygame.display.set_mode((500,500))
#makes player color choice
window.fill((0,0,225))

pygame.draw.rect(window,(0,250,175),[0,0,250,500],0)
pygame.draw.rect(window,(200,0,250),[250,0,250,500],0)
pygame.display.update()
playerChoice = ""
print("Who do you think will win? ")
print("Green or Purple Please click.")
getGuess = True
while getGuess:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] < 250:
                playerChoice = "Green"
                getGuess = False
            elif event.pos[0] > 250:
                playerChoice = "Purple"
                getGuess = False
print(playerChoice)
pygame.time.wait(5000)


#makes dart board
pygame.draw.circle(window,(225,0,0),[250,250],250,0)
pygame.draw.line(window,(0,0,0,),[0,250],[500,250],2)
pygame.draw.line(window,(0,0,0,),[250,0],(250,500),2)
pygame.display.update()
#makes darts
for i in range(10):
    greenScore = 0
    purpleScore = 0
    print("Green throws")
    dartWhereX = random.randrange(0,500)
    dartWhereY = random.randrange(0,500)
    distance_from_center = math.hypot(dartWhereX-250, dartWhereY-250)
    is_in_circle = distance_from_center <= 500/2
    if is_in_circle == True:
        pygame.draw.circle(window,(0,225,175),[dartWhereX,dartWhereY],5,0)
        print("Hit")
        greenScore += 1
    else:
        pygame.draw.circle(window,(0,0,0),[dartWhereX,dartWhereY],5,0)
        print("Miss")
        purpleScore -= 1
    dartWhereX = random.randrange(0,500)
    dartWhereY = random.randrange(0,500)
    print("Purple throws")
    distance_from_center = math.hypot(dartWhereX-250, dartWhereY-250)
    is_in_circle = distance_from_center <= 500/2
    if is_in_circle == True:
        pygame.draw.circle(window,(200,0,250),[dartWhereX,dartWhereY],5,0)
        print("Hit")
        purpleScore +=1
    else:
        pygame.draw.circle(window,(0,0,0),[dartWhereX,dartWhereY],5,0)
        print("Miss")
        purpleScore -= 1
if playerChoice == "Green" and greenScore > purpleScore:
    print("You were correct")
elif purpleScore < greenScore:
    print("You were wrong")
else:
    print("It's a tie")

pygame.display.update()
pygame.time.wait(5000)