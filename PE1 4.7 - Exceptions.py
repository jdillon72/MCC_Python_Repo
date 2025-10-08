# Simple Python program to calculate the square of a number

def square_number():
    # Beginning of try except block and modified erroneous code.
    try:
        number_str = input("Enter a number to square: ")
        
        number = int(number_str)
        
        squared_number = number ** 2
        
        # Printed result.
        print(f"The square of {number} is {squared_number}.")
    
    except ValueError:
        # Code to handle error.
        # Only executes if int() fails.
        print("Error: Invalid input. Please enter a valid whole number (integer).")

# Function Call
square_number()
