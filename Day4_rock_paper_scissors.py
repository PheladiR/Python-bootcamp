import random

print("Let's play rock, paper, scissors!")

rock =("""---)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper =(""" ---'____)
             ______)
            _______)
         _  ______)
---.__________)

""")

scissors =("""--____)
                   ______)
          _______________)
      (____ )
---.__(___)""")

game_images = [rock, paper, scissors]

list = [0, 1, 2]

choice= int(input("What are you choosing? Rock= 0, Paper = 1, Scissors = 2:"))

computer = random.randint(0,2)
print(computer)
print(f"computer chose {game_images[computer]}")


    
if choice == 0 and computer == 2:
    print(f"your choice {game_images[choice]}")
    print("you win!")
elif choice == 2 and computer == 1:
    print(f"your choice {game_images[choice]}")
    print("you win!")
elif computer > choice:
    print(f"your choice {game_images[choice]}")
    print("you lose!")
elif choice == computer:
    print(f"your choice {game_images[choice]}")
    print("Draw!")
else:
    print("You entered an invalid number. You lose!")