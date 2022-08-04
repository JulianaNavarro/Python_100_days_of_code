# 🚨 Don't change the code below 👇
from calendar import month
from turtle import left


age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age=int(age)

weeks= age * 52
days=  age * 365
months_left= (90-36)*12

print(f"You have {days} days, {weeks} weeks, and {months_left} months left until your 90s. ")

