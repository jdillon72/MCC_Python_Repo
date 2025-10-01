# First fucntion defintion for calculation of interest.

def calculate_interest(principle, rate, time):
    """
    Does the calculation for simple interst based on user input parameters.

    Arguments:
        principle: The initial amount in 

    """
    simple_interst = (principle * rate * time) / 100

    return simple_interst

principle_amount = float(input("Enter the principle amount: "))
interest_rate = float(input("Enter the interest rate: "))
time_in_years = int(input("Enter the time in years: "))

interest_result = calculate_interest(principle_amount, interest_rate, time_in_years)

print()
print(f"The simple interst for ${principle_amount:,.2f} at {interest_rate:.1f}% over {time_in_years} years is ${interest_result:,.2f}.")