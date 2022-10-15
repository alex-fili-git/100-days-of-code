import random
from re import I
import hangman_art
import hangman_words

end_game = False
lives = 6
#pick a random word from the list
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

print(hangman_art.logo)
#create blank display
display = ['_']*len(chosen_word)
print(hangman_art.stages[lives])
print(' '.join(map(str, display)))

while not end_game:
    #ask for guess
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"you already guessed {guess}. Pick a new one.")
    else:
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if guess == letter:
                    display[index] = letter
        else:
            print("Letter is not in chosen word. You lost a life.")
            lives -= 1

        if "_" not in display:
            end_game = True
            print("you win")
        elif lives == 0:
            end_game = True
            print("You lose")
        #print current state
        print(hangman_art.stages[lives])
        print(' '.join(map(str, display)))

