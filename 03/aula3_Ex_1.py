print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))

bill = 0
if  height >= 120:
    print("You can ride to the rollercoaster!")

    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 65:
        bill = 5
        print("Elderly tickts are $5.") 
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N.\n").upper()
    # wants_photo = wants_photo.upper()
    # print(wants_photo)
    if wants_photo == "Y":
        # bill = bill + 3
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")