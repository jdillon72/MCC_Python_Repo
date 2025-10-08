def main():
# Dictionary of NATO Phonetic Alphabet.
    nato_alphabet = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
        "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett",
        "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
        "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
        "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee",
        "Z": "Zulu"}
    
    #Beginning of the spelling program.
    #User input prompt:
    user_word_to_spell = input("Enter a word to spell using the NATO alphabet.: ")

    #Conversion of the entire word to uppercase so it can be found in dictionary.
    uppercase_word = user_word_to_spell.upper()

    print("\n--- NATO Spelling ---")

    # For loop for iterating through each letter of the uppercase word.
    for letter in uppercase_word:
        # if statement to find letter as a key in dictionary.
        if letter in nato_alphabet:
            # Looking up the NATO phonetic word while using the letter as the key.
            nato_code = nato_alphabet[letter]
            print(f"{nato_code}")
        #elif for possible error involving non characters, numbers, and other possible input.
        elif letter.isspace():
            continue # Skipping spaces silently.
        else:
            # For notifiying the user of non letters they might input.
            print(f"Skipping non-letter: {letter}")
            continue

# Main function.
if __name__ == "__main__":
    main()
