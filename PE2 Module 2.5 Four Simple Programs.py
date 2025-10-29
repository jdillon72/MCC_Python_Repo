import string

special_chars = "!@#$%^&*"

# Function to validate the user input password based on the assignment criteria. It will 
# RETURN True if password is valid, otherwise it will comeback False. 

def pass_validator(password):

    # Condition for length check.
    if not (8 <= len(password) <= 20):
        print("Password must be at least between 8 and 20 characters long.")
        return False
    
    # Counters for each required character type:
    upper_count = 0
    lower_count = 0
    dig_count = 0
    symb_count = 0
    
    # For loop to iterate over input password to test for the required character types of the assignment.
    for char in password:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            dig_count += 1
        elif char in special_chars:
            symb_count += 1
        # Do note: any characters like (spaces, tab, etc (those not in the string will be ignored)).
    
    # Uppercase check if statement that checks for at least one uppercase character.
    if upper_count < 1:
        print("Error!: Password must contain at least one uppercase letter.")
        return False
    
    # Lowercase check if statement that checks for at least one lowercase character.
    if lower_count < 1:
        print("Error!: Password must contain at least one lowercase letter.")
        return False
        
    # Digit check if statement that checks for at least one numeric character.
    if dig_count < 1:
        print("Error!: Password must contain at least one number.")
        return False
        
    # Symbol check if statement that checks for at least one character is from special_chars string/list.
    if symb_count < 1:
        print(f"Error: Password must contain at least one symbol from: {special_chars}")
        return False
    
    # Return statement if password passes all requirements. 
    return True

# main function for taking user input and handle the password creation and confirmation process. It Uses a main while loop and try/except block for error handling.
def main():
    
    # This is the outer loop to restart the entire process if confirmation checks fail.
    while True:

        valid_password = "" 
        
        # Inner loop to keep testing until the password meets requirements.
        while True:
            try:
                # Taking user input for password creation. 
                new_pass = input("\nEnter your new password it should be 8 to 20 characters long, have an uppercase letter, lowercase letter, numeric digit, and special case symbol): ")
                
                # Check if the entered password meets all criteria.
                if pass_validator(new_pass):
                    valid_password = new_pass
                    break # For exiting the inner while loop. 
                # If valid_password returns False, the loop continues (forever...until they meet requirements I me).
                
            # End of try except block. 
            except: 
                print("\n\nAn unexpected input error occurred. Please try again.")

            # Exits the main function, stopping the program.
        
        # Outer while loop for password confirmation.
        
        print("\n- Password Confirmation -")
        
        # A try-except block is also used for the confirmation input from the user.
        try:
            confirmed_password = input("Please re-enter your password for confirmation: ")
        except:
            print("\n\nAn unexpected input error occurred. Restarting the entire process.")
            # We use 'continue' to skip the rest of this iteration and jump back to the OUTER 'while True' loop.
            continue
            
        # Check for match (Conditional), if the second entry matches the first, display a success message.
        if valid_password == confirmed_password:
            print("\n SUCCESS!: Password validated and confirmed!")
            break 
        # Prompt for the user to start the process again if their passwords do not match.
        else:
            print("\n Passwords do not match. You must start the process over from the beginning.")


# Function for calling main() function. Not to sound repetitive.
main()