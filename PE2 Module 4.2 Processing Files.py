# No import os needed since we aren't using OS-specific functions!

# Diary file constant—makes it easy to update the filename later.
DIARY_FILE_NAME = "diary.txt" 

def diary_writer(): 
    """
    Main function for the personal diary app. 
    Handles user input and writes the entry to the text file.
    """
    
    # --- Input Collection ---
    # Quick prompts to grab the timestamp and the actual entry text.
    # I usually round the time to the five-minute mark when taking quick notes.
    entry_timestamp = input("Date/Time (e.g., 2025-11-18 10:00 AM): ")
    entry_content = input("What's on your mind today? ")
    
    # --- Data Construction ---
    # Building the entry string. Using an f-string is best practice here.
    # Need the two '\n' characters at the end for the required blank line separation.
    entry_payload = (
        f"TIME: {entry_timestamp}\n"
        f"{entry_content}\n"                   
        f"\n"                                
    )
    
    # --- File Write Operation ---
    # Opening the file in 'a' (append) mode so we don't wipe out past entries. 
    # The 'with' keyword closes the file automatically—super safe.
    try:
        with open(DIARY_FILE_NAME, 'a') as diary_file:
            # Writing the final string to the file.
            diary_file.write(entry_payload)
        
        print(f"\n Success! Entry saved to {DIARY_FILE_NAME}. Check the file!")
        
    except IOError as e:
        # Catching system errors like bad permissions or a full drive.
        print(f"\n FILE ERROR: Couldn't write to the file! Details: {e}")
        
    except Exception as e:
        # General catch-all for anything else unexpected.
        print(f"\n UNEXPECTED ERROR: Something broke: {e}")


# Run the writer function when the script starts up.
diary_writer()