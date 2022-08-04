# 🚨 Don't change the code below 👇
from calendar import month
from turtle import left


age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age=int(age)

months= age * 12
weeks= age * 52
days=  age * 365

months_left= (90-age)*12
days_left= (90-age) * 365
weeks_left= (90-age)* 52

print(f"You lived {days} days, {weeks} weeks, and {months} months")
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left until your 90s. ")

