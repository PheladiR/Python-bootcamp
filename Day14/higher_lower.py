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
while game_should_continue:
    selected_profiles = random.sample(data, 2)
    p1 = selected_profiles[0]
    p2 = selected_profiles[1]

    print(
        f"Compare A: {p1.get('name')}, a {p1.get('description')}, from {p1.get('country')}.")
    print(vs)
    print(
        f"Compare B: {p2.get('name')}, a {p2.get('description')}, from {p2.get('country')}.")
    guess = input("Who has more followers? A or B?").strip().upper()

    if int(p1["follower_count"]) > int(p2["follower_count"]):
        correct = 'A'
        if guess == correct:
            current_score += 1
    else:
        correct = 'B'
        final_score = current_score
        print(f"Sorry, that's wrong. Final score: {final_score}")
        game_should_continue = False
