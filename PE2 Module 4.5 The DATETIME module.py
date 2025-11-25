import datetime

def main():
    """
    Main function to collect birthday, calculate age in multiple units 
    (years, months, weeks, days, hours, minutes), and print results.
    """
    print("--- Age Calculator ---")

    try:
        # --- INPUT ---
        # Using int() immediately to convert string input to numbers
        # Using short variables y, m, d is common in starter code
        y = int(input("What year were you born? "))
        m = int(input("What Month were you born (as a number. May would be 5) "))
        d = int(input("What day of the month were you born? "))

        # creating the date objects
        # datetime.datetime requires (year, month, day)
        birthday = datetime.datetime(y, m, d)
        current_time = datetime.datetime.now()

        # --- CALCULATIONS ---
        
        # 1. DAYS
        # Subtracting two dates creates a 'timedelta' object. 
        # We use .days to get the integer number of days.
        difference = current_time - birthday
        total_days = difference.days

        # 2. YEARS
        # Dividing by 365.25 accounts for Leap Years (extra day every 4 years)
        age_years = total_days / 365.25

        # 3. WEEKS
        # Straightforward division since a week is always 7 days
        age_weeks = total_days / 7

        # 4. MONTHS
        # Per instructions: calculate years first, then use the remainder.
        # This gives us the "leftover" days after removing full years.
        remaining_days = total_days % 365.25
        
        # We divide the leftover days by 30.44 (average days in a month).
        months_remaining = remaining_days / 30.44
        
        # Total months = full years * 12 + the partial months calculated above.
        total_months = (int(age_years) * 12) + months_remaining

        # 5. HOURS & MINUTES (Added to meet Assignment Objectives)
        # Total seconds lived / 3600 gives hours. We're getting to RNA levels here!
        total_seconds = difference.total_seconds()
        age_hours = total_seconds / 3600
        
        # total seconds / 60 gives minutes
        age_minutes = total_seconds / 60

        # --- OUTPUT ---
        
        print("\n--- Results ---")
        # strftime formats the date object to a string: YYYY-MM-DD.
        print(f"Your birthday is: {birthday.strftime('%Y-%m-%d')}")
        print(f"The difference is {total_days} days")
        
        # formatting with :.1f to keep the decimals clean (1 decimal place) for percision as well.
        print(f"You are {age_years:.1f} years old")
        print(f"You are {total_months:.1f} months old")
        print(f"You are {age_weeks:.1f} weeks old")
        print(f"You are {age_hours:.0f} hours old")
        print(f"You are {age_minutes:.0f} minutes old")

    except ValueError:
        # Catches non-numeric inputs to prevent crashing
        print("Error: You must enter numbers for the Year, Month, and Day.")
    except Exception as e:
        # Catches logic errors (like Month 13). That would violate the gregorian calander!
        print(f"Something went wrong: {e}")


main()