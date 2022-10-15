from re import T
import pygame
#Part 1 and 2 loop
def indefIteration(number):
    number = 101
    upper_limit =20
    iters = {}
    for i in range(2,upper_limit):
        count = 0
    while number > 1:
        print(number)
        if number % 2==0:
             number = number/2
        else:
            number = number * 3 + 1
        count = count + 1
        iters[number] = count
        print(number)
        print("count: " , count)
        print(iters)
# indefIteration(0)
def graph():
    pygame.init()
    window = pygame.display.set_mode((500,500))
    window.fill((225,225,225))
    upperLimit = 20
    iners = {}
    maxSoFar = 0
    maxVal = 100
    scale = 5
    number = 101
    for i in range(2,upperLimit):
        count = 0
    while number > 1:
        if number % 2==0:
             number = number/2
        else:
            number = number * 3 + 1
        count = count + 1
        count = count + 1
        iners[number] = count
        iners.items()
    pygame.draw.line(window,(0,0,0,),[0,250],[500,250],2)
    pygame.draw.line(window,(0,0,0,),[250,0],(250,500),2)
    pygame.draw.line(window,(0,0,0),[124,124],[125,125],2)
    pygame.draw.line(window,(0,0,0,),[125,125],[12,12],2)
    pygame.display.update()
    pygame.time.wait(5000)
    newWindow = pygame.transform.flip(window,False,True)
    window.blit(newWindow,(0,0))
    pygame.display.update()
    pygame.time.wait(5000)
    font = pygame.font.Font(None, 20)
    msg = font.render("maximum number of iteration: " + str(maxSoFar) , True, (225,225,225))
    window.blit(msg,(10,10))
    pygame.display.update()
    pygame.time.wait(5000)
graph()


