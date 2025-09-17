# Defining variable to take the customer's age.
user_numb_grade = int(input("What is your numeric grade?: "))
print()

# El/If statement to determine what the letter grade of the user is after input.
if user_numb_grade >= 90:
    print("The letter grade is: A")
elif user_numb_grade <= 89 and user_numb_grade >= 80:
    print("The letter grade is: B")
elif user_numb_grade <= 79 and user_numb_grade >= 70:
    print("The letter grade is: C")
elif user_numb_grade <= 69 and user_numb_grade >= 60:
    print("The letter grade is: D")
elif user_numb_grade <= 59:
    print("The letter grade is: F")