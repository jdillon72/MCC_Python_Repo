# Variables for song lyrics:

input_name_1 = input("Please input a proper name.: ")
input_name_2 = input("Please input a another proper name.: ")
input_noun_1 = input("Please input a noun.: ")
input_noun_2 = input("Please input a another noun.: ")
input_verb_1 = input("Please input a verb.: ")
input_verb_2 = input("Please insert another verb.: ")
input_adjective_1 = input("Please input an adjective.: ")
input_adjective_2 = input("Please input another adjective.: ")

# Function definition with mandatory parameters

def custom_song(name1, name2, noun1, noun2, verb1, verb2, adjective1, adjective2):
    # Printed Song.
    print("\n\n")
    print(f"{name1}'s no stranger to {noun1}.")
    print(f"{name2} knows the rules and so do I.")
    print(f"A {adjective1} {noun2}'s what I'm thinking' of.")
    print(f"You wouldn't get this from any other {adjective2} guy.")
    print()
    print("I just wanna tell you how I'm feeling.")
    print("Gotta make you understand.")
    print()
    print(f"Never {verb1}, never gonna {verb2}.")

# Calling the function using named arguments
custom_song(
    name1=input_name_1,
    name2=input_name_2,
    noun1=input_noun_1,
    noun2=input_noun_2,
    verb1=input_verb_1,
    verb2=input_verb_2,
    adjective1=input_adjective_1,
    adjective2=input_adjective_2
)