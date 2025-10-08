# Defining the Factorial Function for base use. Intended for Steps 1 & 2 of the assignment.
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        # When the funtion calls itself with a smaller value. (n-1)
        return n * factorial(n-1)
    
# Prompt for user to enter a non-negative number(integer) and calling the fuction.

#User input.

num_input = input("Enter a non-negative integer: ")
number = int(num_input)

def main():
    try:
        if number < 0:
            print("Factorial is not able use negative numbers.")
        else:
            #Sucessful call of the factorial function.
            result = factorial(number)

            #Print statement for result.
            print(f"The factorial of {number} is {result}")

    except ValueError:
        # Except block for cases where the users enters any text other than an integer.
        print("This is an invalid input. Please enter a valid non-negative number that isn't a decimal to continue.")

if __name__ == "__main__":
    main()
