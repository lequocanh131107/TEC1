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
        print("Too high! Try a lower number.")