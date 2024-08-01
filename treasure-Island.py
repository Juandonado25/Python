print('''# *******************************************************************************
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
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************''')
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('Your\'re at a crossroad, where do you want to go? type "left" or "right": ').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake, There is an island in the middle of the lake, type "wait" to wait for a boat or "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island inharmed. there is a house with a 3 doors. One red, one yellow and one blue. which colour do you choose?").lower()
        if choice3 == "red":
            print("You find the treasure!. Good job!")
        elif choice3 == "yellow":
            print("You have been shooted by a crossbow. Game over.")
        else:
            print("You have been poisoned by a toxic gas. Game over.")
    else:
        print("Yout got attacked by and angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")