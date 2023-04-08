# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# TODO: get origin letter's content
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    starting_content = starting_letter.read()

# TODO: get invited names in list
with open("./Input/Names/invited_names.txt") as invited_names:
    invited_names_content = invited_names.read()
names = invited_names_content.split("\n")

# TODO: replace [name] with name in names and create antoher file to store the text.
for name in names:
    replace_content = starting_content.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}",mode='w') as output_letter:
        output_letter.write(replace_content)





