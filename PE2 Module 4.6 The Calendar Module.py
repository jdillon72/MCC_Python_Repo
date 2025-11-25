import calendar
import datetime

def main():
    """
    Main function to execute the birth month calendar generator.
    It handles user input, validation, and calendar display.
    """
    
    # Using the datetime module to dynamically fetch the current year.
    # This ensures the calendar is always accurate, regardless of when the script is run. No weird time travel here.
    current_year = datetime.datetime.now().year
    
    print(f"Welcome! I can generate a calendar for your birth month in {current_year}.")

    try:
        # Requesting input from the user. We wrap this in an int() conversion immediately
        # because the calendar module requires an integer argument for the month.
        birth_month = int(input("Please enter your birth month (as a number 1-12): "))

        # Validating that the input is actually a logical month (1 for Jan through 12 for Dec).
        if 1 <= birth_month <= 12:
            print(f"\nHere is the calendar for your birth month in {current_year}:\n")
            
            # The month() function returns a multi-line string representing the calendar.
            # We pass the current year and the user's validated month.
            month_calendar = calendar.month(current_year, birth_month)
            print(month_calendar)
            
        else:
            # Handling the case where the user enters a number, but it's not a valid month.
            print("Error: The number must be between 1 and 12. Please try again.")

    except ValueError:
        # This block catches errors if the user inputs something that isn't a number (like "July").
        # This satisfies the requirement to handle invalid inputs gracefully.
        print("Error: Invalid input. Please enter a numeric value (e.g., 7 for July).")

# Standard boilerplate to call the main function when the script is executed directly.
main()