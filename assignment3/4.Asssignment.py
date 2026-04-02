<<<<<<< HEAD
import random
random_number = random.randint(1, 10)
while True :
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == random_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < random_number:
        print("Too low! Try a higher number.")
    else: 
=======
import random
random_number = random.randint(1, 10)
while True :
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == random_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < random_number:
        print("Too low! Try a higher number.")
    else: 
>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
        print("Too high! Try a lower number.")