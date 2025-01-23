import random

print("Let's play rock, paper, scissors!")

list = ["rock", "paper", "scissors"]

rock = print("""---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""")


paper = print("""---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")

scissors = print("""---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""")

computer = random.choice(list)
choice= input("What are you choosing?")

if choice == "rock" and computer== "paper":
    print(f"your choice {choice}")
    print(f"computer chose {computer}")
    print("you lose!")
elif choice == "paper" and computer == "scissors":
    print(f"your choice: {choice}")
    print(f"computer chose {computer}")
    print("you lose!")
elif choice == "scissor" and computer == "rock":
    print(f"your choice {choice}")
    print(f"computer chose {computer}")
    print("you lose!")
elif choice== computer:
    print(f"your choice {choice}")
    print(f"computer chose {computer}")
    print("Draw!")
else:
    print(f"your choice {choice}")
    print(f"computer chose {computer}")
    print("You win")