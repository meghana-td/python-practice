import random

number = random.randint(1, 100)
print("---Welcome to Number Guessing Game---")

while True:
    guess = int(input("Guess a number between 1 to 100: "))

    if guess < number:
        print("Oh Oh! too low, try again")
    
    elif guess > number:
        print("Oh Oh! too high, try again")

    else:
        print("Congratulations!! you guessed the correct number.")
        break
