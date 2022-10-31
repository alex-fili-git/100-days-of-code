#TODO: Create a letter using starting_letter.txt 
with open("./Input/Names/invited_names.txt") as f:
    names = f.readlines()


for name in names:
    name = name.strip("\n")
    with open("./Input/Letters/starting_letter.txt") as start:
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as end:
            end.write(start.read().replace("[name]", name))
