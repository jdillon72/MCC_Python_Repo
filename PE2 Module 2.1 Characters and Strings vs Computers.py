# To begin program.
def main():
   
    while True:
        #Variable for taking user input.
        input_char = input("Please enter an single alphabetical character: ")

        #Checking if length of input is addressing original prompt.
        if len(input_char) == 1:
            break # For if user input is valid, loop will be exited.
        elif len(input_char) == 0:
            print("Error: You must enter at least one alphabetical character.")
        else:
            print("Error: Please enter precisely one character. ")
    
    #Variable for converting user input
    #Using the built-in function ord() to conduct operation. 
    ascii_value = ord(input_char)

    #Print statements for displaying results.
    print(f"\nResult: ")
    print(f"The character '{input_char}' converts to the ASCII value: {ascii_value}")

    print("\n" + "="*50 + "\n")

    print("Prompt for Reverse ASCII to Alphabetical character lookup.")

    # While loop to perform second operation based on the first.
    while True:
        ascii_str = input("Enter an ASCII value (32-127) for reverse lookup: ")

        #Try-except block to handle invalid inputs.
        try:
            # Convert the string input to an numeric result.
            ascii_input = int(ascii_str)

            # Ensure that the value is between 32 and 127 (the printable range for ASCII keys).
            if ascii_input >= 32 and ascii_input <= 127:
                # Valid input found, exit the loop
                break
            else:
                # Value is a number, but out of the specified range
                print("Error: The ASCII value must be between 32 and 127.")
        
        except ValueError:
            # Catches error if the user enters text instead of a number which is required:
            print("Error: Invalid input. Please enter a whole number.")
    
    # Handle non-numeric input.
    character = chr(ascii_input)

    #Print statements for displaying results.
    print(f"\nResult: ")
    print(f"The ASCII value {ascii_input} converts to the character: '{character}'")

#For calling and running main.
main()
