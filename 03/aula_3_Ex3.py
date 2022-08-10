# 🚨 Don't change the code below 👇
print ("Welcome to the BMI Calculator")
height = float(input("enter your height in m: \n"))
weight = float(input("enter your weight in kg: \n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height = float(height)
weight = int(weight)

BMI = weight / height ** 2
BMI = int(round(BMI,3))

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
