# Defining the main function.

def main():
    
    # Starting Program with the list of artists. This is missing some essentials. For example Foo Fighters, Oasis, Pearl Jam, I could go on...
    artist_list = ["The Beatles", "Madonna", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Michael Jackson", "Whitney Houston", "Rihanna"]
    
    print("\n- Artist List Replacer -")
    print("Current Artists:")
    
    # The for loop Using to display the index and artist.
    for index, artist in enumerate(artist_list):
        print(f"[{index}]: {artist}")
        
    print(f"\nNote: The list has {len(artist_list)} artists (Indices 0 through {len(artist_list) - 1})")
    
    # Try/Except block to contain the risky operations.
    try:
        # User input variable to get index and artist.
        index_to_replace_str = input("\nEnter the index (number) of the artist to replace: ")
        
        # Variable for converting input to integer and test ValueError.
        artist_index = int(index_to_replace_str)
        
        # Variable to capture new artist's name.
        new_artist = input("Enter the name of the new artist: ")
        
        # For finding the artists numeric (index) in the list, will test for index error. User's input cannot put in a number beyond 7.
        original_artist = artist_list[artist_index] 
        
        # For perform the list modification once the index is verified.
        artist_list[artist_index] = new_artist
        
        print("\n- Update Successful! -")
        print(f"Updated list: {artist_list}")
        print(f"Replaced {original_artist} with {new_artist} at index {artist_index}.")
        
    # Errors in exception block.
    
    # ValueError exception for when the user enters a non-numeric character, float, or alphabetic character for the index and displaying technical error message.
    except ValueError:
        print("\n Error: ValueError occurred.")
        print("Helpful Message: You must enter a WHOLE NUMBER for the index. Text or decimals are not valid.")
        
    # For catching the IndexError, when the user enters a number outside the list's range.
    except IndexError:
        print("\n Error: IndexError occurred.")
        print(f"Helpful Message: The index you entered is out of range. Please use a number between 0 and {len(artist_list) - 1}.")
        
    # General Error handling Catch-all for any other unexpected error.
    except Exception:
        print("\n A general, unexpected error occurred.")
        print("Maybe try restarting the program or double-checking your initial list.")

# To execute the main program loop.
main()