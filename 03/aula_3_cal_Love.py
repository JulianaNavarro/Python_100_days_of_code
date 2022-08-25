# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇



t=(name1.count("t"))
r=(name1.count("r"))
u=(name1.count("u"))
e=(name1.count("e"))

l=(name1.count("l"))
o=(name1.count("o"))
v=(name1.count("v"))
score1= str(t + r + u + e + l + o + v )


t=(name2.count("t"))
r=(name2.count("r"))
u=(name2.count("u"))
e=(name2.count("e"))

l=(name2.count("l"))
o=(name2.count("o"))
v=(name2.count("e"))

score2= str(t + r + u + e + l + o + v )


total_score = int(score1 + score2)


if (total_score < 10) or (total_score > 90):
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif (total_score >= 40) and (total_score <= 50):
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")