rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
picked = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if picked == 0:
    print(rock)
elif picked == 1:
    print(paper)
elif picked == 2:
    print(scissors)
else:
    print("You lost by not competing!")
    exit()

computer = random.randint(0,2)
if computer == 0:
    print(f"The computer chose:\n {rock}")
elif computer == 1:
    print(f"The computer chose:\n {paper}")
elif computer == 2:
    print(f"The computer chose:\n {scissors}")

if picked == computer:
    print("Draw")
elif (picked == 0 and computer == 2) or (picked == 1 and computer == 0) or (picked == 2 and computer == 1):
    print("You win!")
else:
    print("You lose")
