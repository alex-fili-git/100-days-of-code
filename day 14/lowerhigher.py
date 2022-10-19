import art
import game_data
import random
import os

score = 0
def draw():
    return random.choice(game_data.data)

def winner(a, b):
    if a['follower_count']>b['follower_count']:
        return "a"
    else:
        return "b"

draw_B = draw()
guess_right = True
while guess_right:
    os.system('clear')
    draw_A = draw_B
    while draw_B == draw_A:
        draw_B = draw()
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {draw_A['name']}, a {draw_A['description']}, from {draw_A['country']}")
    print(art.vs)
    print(f"Against B: {draw_B['name']}, a {draw_B['description']}, from {draw_B['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess != winner(draw_A, draw_B):
        guess_right = False
        os.system('clear')
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
    score += 1
