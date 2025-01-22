print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,--._ '.   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
""")

print("Welcome to the treasure island!\nYour mission is to find the treasure.")


direction = str.lower(input("Do you want to go left or right?"))
if direction == "right":
    print("You fell into a hole. Game Over!😖")
elif direction == "left":
    print("You came across a river...")
    
    action = str.lower(input("Do you want to swim or wait?"))
    if action == "swim":
        print("You were attacked by a trout. Game over!😖")
    elif action == "wait":
        print("Three magical doors appeared.\nWhich one will you enter? Red, Blue or Yellow?")
             
        door = str.lower(input("Pick a door. Blue or Red or Yellow?"))
        if door == "yellow":
            print("You win!😊")
        elif door == "red":
            print("Burned by fire. Game over!😖")
        elif door == "blue":
            print("Eaten by beasts. Game over!😖")
else:
    print("Invalid input. Please try again")