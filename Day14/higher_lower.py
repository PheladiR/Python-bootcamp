import random
from art import logo, vs
from game_data import data

print(random.choice(data))

# compare A

# COmpare B

# if right, current score += 1
# if wrong final score = current score
# if won, B becomes A, new B is chosen

current_score = 0
game_should_continue = True

print(logo)

p1 = random.choice(data)
while game_should_continue:
    p2 = random.choice(data)
    while p1 == p2:
        p2 = random.choice(data)
    print(
        f"Compare A: {p1.get('name')}, a {p1.get('description')}, from {p1.get('country')}.")
    print(vs)
    print(
        f"Compare B: {p2.get('name')}, a {p2.get('description')}, from {p2.get('country')}.")
    guess = input("Who has more followers? A or B?\n").strip().upper()

    if int(p1["follower_count"]) > int(p2["follower_count"]):
        correct = 'A'
    else:
        correct = 'B'

    if guess == correct:
        current_score += 1
        print(f"You are right! Current Score: {current_score}")
        p1 = p2
    else:
        final_score = current_score
        print(logo)
        print(f"Sorry, that's wrong. Final score: {final_score}")
        game_should_continue = False
