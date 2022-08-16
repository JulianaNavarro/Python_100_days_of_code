# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? \n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# check= year / 4 
# check=int(round(check,2))
# print(check)

# if year % 4 == 0:
#     print("Leap")
# else:
#     print("Not Leap")

if year % 4 == 0 and year % 100 > 0 or year % 100 == 0 and year % 400 == 0:
    print("Leap year")
else:
    print("Normal year")




