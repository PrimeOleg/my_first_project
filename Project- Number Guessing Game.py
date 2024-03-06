#*****************************
# 06/03/2024
# Number Guessing game project

# Will import the randint module allowing the program to generate random numbers
import random
attempts = 10

print("\t----HELLO----\n----WELCOME TO MY GAME----")
number = random.randint(1, 100)

print("I am thinking of a number... which number do you think it is")

while attempts != 0:
    guess = input("Enter your guess: ")
    guess = int(guess)

    if guess < number:
        print("The number you have guessed is too low")
        attempts -=1

    elif guess > number:
        print("The number you have guessed is too high")
        attempts -=1

    elif guess == number:
        print("Congratulation you have beat me!")
        print(f"In total you had {attempts} attempts remaining")
        break

    print(f"You have {attempts} attempts remaining")

else:
    print("Game over you have lost as you ran out of attempts")
    print(f"The correct number was {number}")



