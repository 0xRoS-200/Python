with open("./Input/Names/invited_names.txt") as names:
    file = names.readlines()
    with open ("./Input/Letters/starting_letter.txt") as letter:
        for name in file:
            name = name.strip()
            new_letter = letter.read().replace("[name]", name)
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
                completed_letter.write(new_letter)
