
print("Welcome to the game of luck!")
number = input("Choose a number between 1 to 10 \n")

import random

number_integer = random.randint(1,10)
print(number_integer)
if number == number_integer:
    print(f"Wow, you got it right, the chosen machine number was also {number_integer}")
else:
    print(f"Oh nooo! It wasn't this time! The machine number has been {number_integer} Don't give up, try again!")

    