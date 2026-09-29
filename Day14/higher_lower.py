import random
from art import logo, vs
from game_data import data

print(logo)

print(random.choice(data))

# compare A
print(vs)
# COmpare B

# if right, current score += 1
# if wrong final score = current score
# if won, B becomes A, new B is chosen
