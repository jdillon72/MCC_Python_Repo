import random

# Main function definition.
def main():

    #Generating the secret number between 1 and 100.
    secret_number = random.randint(1,100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    guess = 0 # Initializes guess to a value that is not the secret number.

    # Game while loop.
    while guess != secret_number:
        try:
            # User input variable.
            guess = int(input("\nEnter your guess (1-100): "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue # Skips the rest of the loop to ask again.

        # If user guesses outside the range.
        if not 1 <= guess <= 100:
            print("Your guess must be between 1 and 100.")
            continue

        # When the guess is correct.
        if guess == secret_number:
            break

        #Calculating the difference in numbers for user feedback.
        sec_num_difference = abs(guess - secret_number)

        # Feedback based on proximity.
        if sec_num_difference <= 5:
            print("Very Hot! You are extremely close.")
        elif sec_num_difference <= 15:
            print("Hot. You're getting warmer.")
        elif sec_num_difference <= 25:
            print("Cool. You're in the right neighborhood.")
        else:
            print("Cold. You're pretty far away.")

    # For when user wins.
    print(f"\n Congratulations! You guess the number {secret_number}!")

# Calling the main function to start the program.
main()
    