import random

print("Number guessing game")

number = random.randint(1, 20)

chances = 0

print("Guess a number (between 1 and 20):")

while chances < 5:

    guess = int(input("Enter your guess:- "))
    if guess == number:
        print("Congratulation YOU WON! try again and test ur luck")
        break
    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)
    else:
        print("Your guess was too high: Guess a number lower than", guess)
    chances += 1
if not chances < 5:
    print("you lost, try again. The number is", number)