logo = """
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                          
                                                                                          
"""

import random 

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking ofanumber between 1 and 100")


""" Choosing game level"""

n = 10
def attempts():
    level = input("Choose a difficulty. Type 'easy' or 'hard':\n ")  
    if level == 'easy':
        n = 10
        print(f'you have {n} attempts to guess the number.')
    else:
        n = 10-5
        print(f'you have {n} attempts to guess the number.') 
attempts()

num = list(range(1, 101))

################ Game over condition ############################
game_over = True
if n != 0:
    game_over = False
else:
    game_over = True

###############################################################
def guess_Number():
  global n
   
my_number = random.choice(num)
print(my_number)


while game_over is False:
    for i in num: 
        guess = int(input("make a guess:\n")) 
        if guess != my_number:
            n -=1
            if guess < my_number:
                print("Too low")
                print(f"you have {n} attempts remaining.")
            elif guess > my_number:
                print("Too high")
                print(f"you have {n} attempts remaining.")
        else:
            n = 0
            print("You have guessed the correct number. Congratulations, you win!")
        if n == 0:
            game_over = True
            print("Gameover. Refresh the page to start again.")
        break
       
guess_Number()