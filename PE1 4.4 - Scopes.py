# Global variables for providing constants for 1 lb to Kilo and 1 in to meters.

LBS_TO_KGS = 0.453592
IN_TO_MET = 0.0254

# Main function, contains main logic and uses the local variables.

def main():
    
    weight_lbs = float(input("Enter your weight in pounds: "))
    height_in = float(input("Enter your height in inches: "))
    
    # Variables for converting the inputs to metric units using the global conversion constants.
    weight_in_kg = weight_lbs * LBS_TO_KGS
    height_m = height_in * IN_TO_MET
    
    #If statement to enure height is not zero to prevent division by zero and destroying the entire universe.
    if height_m <= 0:
        print("Error: Height must be greater than zero.")
        return
    
    bmi = weight_in_kg / (height_m ** 2)

    # For determining the BMI category based on current ranges.
    # The 'category' variable is also a local variable.
    if bmi < 18.5:
        category = "underweight category."
    elif 18.5 <= bmi < 30:
        category = "normal weight category."
    elif 25 <= bmi < 30:
        category = "overweight category."
    else:
        category = "obese category."
        
    # Display the BMI value and Category.
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"You are in the {category}")

# To execute program.
if __name__ == "__main__":
    main()    