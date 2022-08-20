# 🚨 Don't change the code below 👇
from cgi import print_arguments


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n").upper()
add_pepperoni = input("Do you want pepperoni? Y or N \n").upper()
extra_cheese = input("Do you want extra cheese? Y or N \n").upper()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

price = 0
     
if size == "S":
    price += 15
    if add_pepperoni == "Y":
       price += 2

elif size == "M":
    price += 20
    if add_pepperoni == "Y":
       price += 3
else:
    price += 25
    if add_pepperoni == "Y":
       price += 3


if extra_cheese == "Y":
    price += 1


print(f"Your final bill is: ${price}")

# print(size)
# print(add_pepperoni)
# print(extra_cheese)

