# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

step_1 = input("You choose right or left?\n").upper()

if step_1 == "LEFT":
    step_2 = input('You\'ve come to a lake. There is an island in the midle of to late. Type "wait" to wait for a boat. Type "swim" to swim across.\n').upper()
    if step_2 == "WAIT":
        step_3 = input('You arrive at the island unharmed. There is house with 3 doors. One red, yellow and one blue\n').upper()
        if step_3 == "RED":
            print("Burned by fire. GAME OVER.")
        elif step_3 == "YELLOW":
            print("YOU WIN!!!")
        elif step_3 == "BLUE":
            print("Eaten by beasts. GAME OVER.")
        else:
            print("You choose a door that doesn't exist. GAME OVER!!!")
    elif step_2 == "SWIM":
        print("Attacked by trout. GAME OVER.")
    else:
        print('Are you stupid?! I said "Wait or Swin" GAME OVER FOR YOU!!!')
elif step_1 == "RIGHT":
   print("You fell into a hole. GAME OVER.")
else:
    print('Are you stupid?! I said "Left or Right" GAME OVER FOR YOU!!!')




