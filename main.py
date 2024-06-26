import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonatic():
    word = input("Enter a Word:").upper()

    try:
        output = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonatic()

    else:
        print(output)


generate_phonatic()
