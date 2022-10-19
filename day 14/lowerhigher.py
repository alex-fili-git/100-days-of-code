import art
import game_data
import random

score = 0

def draw():
    random.choice(game_data.data)


print(art.logo)
if score > 0:
    print(f"You're right! Current score: {score}.")
print(draw())