#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#Welcome to the tip calculator!
from decimal import Rounded


total= input("What was the total bill? \n")
tip= input("How much tip would you like to give? 10, 12, or 15? \n")
people= input("How many people to split the bill? \n")

total = float(total)
tip = int(tip)
people = int(people)

# print(type(total))
# print(type(tip))
# print(typ   e(people))

new_tip= (tip/100)
print(new_tip)
final=((total * new_tip)+total)/people
 
print (round(final,2))

