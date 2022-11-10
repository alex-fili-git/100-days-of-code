import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}
no_error=True

def generate_phonetic():
    name = input("Enter a word: ").upper()
    try:
        result = [nato_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        no_error=False
        print(result)

generate_phonetic()

