# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# is_run = True
# while is_run:
#
#     word = input("Enter a word: ").upper()
#     try:
#         nato = [data_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")
#     else:
#         print(nato)
#         is_run = False


def generate_alphabet():
    word = input("Enter a word: ").upper()
    try:
        nato = [data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_alphabet()
    else:
        print(nato)

generate_alphabet()