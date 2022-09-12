from random import random
import random
randomNumber = random.randint(1,10)
for i in range(3):
    guess = int(input("What is your guess?: "))
    if guess == randomNumber:
        print("correct")
        break
    elif guess < randomNumber:
        print("Too low")
    else:
        print("Too high")

