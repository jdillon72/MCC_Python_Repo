# Launching the main function.

def two_letter_combinations(characters):
    
    # The outer loop determines the first character of the combination.
    for char1 in characters:
        # The inner loop determines the second character; this nested structure 
        # effectively computes the Cartesian product of the input set with itself.
        for char2 in characters:
            # Concatenate the two characters to form the combination string.
            combination = char1 + char2
            
            # Used 'yield' to return the combination and pause the function's 
            # execution state, which is super useful for memory-efficient generation!
            yield combination


def main():
    """
    Defines the initial character set and iterates over the generator 
    to print all the combinations.
    """
    # Defines the 5-letter set.
    initial_characters = ['a', 'b', 'c', 'd', 'e']
    
    print(f"--- Generating Two-Letter Combinations from: {initial_characters} ---")

    # For calling the generator function so it returns the generator object.
    combination_generator = two_letter_combinations(initial_characters)
    
    for combination in combination_generator:
        print(combination)


main()