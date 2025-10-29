# Main function with program inside.
def main():
    """
    Runs the division counter to test errors.
    Prompts the user for a numerator and divisor and performs division.
    Handles specific errors like ValueError for non-numeric input. 
    and ZeroDivisionError, division by zero (The possible end of the universe).
    """
    
    print("\n- Simple Error-Handling Division Calculator -")
    print("Objective: Divide one number by another.")
    
    # Try and except block to catch specific errors.
    try:
        # Prompt user for input, which is where a ValueError can occur.
        num1_str = input("Enter the numerator (the number being divided): ")
        num2_str = input("Enter the divisor (the number to divide by): ")
        
        # Variables to store user input.
        num1 = float(num1_str)
        num2 = float(num2_str)
        
        # Simple division test.
        result = num1 / num2
        
        print(f"\n Success! The result of {num1} divided by {num2} is: {result}")
        
    # For catching the ZeroDivisionError
    except ZeroDivisionError:
        print("\n Error! ZeroDivisionError occurred.")
        print("Helpful message: You cannot divide by zero. That might destroy the entire universe if you were able too! Please try running the program again with a different divisor.")
        
    # For catching the ValueError
    except ValueError:
        print("\n Error! ValueError occurred.")
        print("You must enter valid numbers only. Text or symbols are not accepted.")
        
    # Generic 'except' block at the end to catch unexpected errors.
    except Exception:
        print("\n An unknown error occurred. Sorry, something went wrong!")
        
# Calling the main function.
main()