# Asks the user for their age and converts the input to an integer.
user_age = int(input("What is your age?: "))
print('')
#For adding new line.

# Check to see if the user is old enough to drive.
if user_age >= 16:
    print("You are old enough to drive.")
elif user_age < 16:
    print("You are not old enough to drive and still have " + str(16-user_age) + " years before you're old enough to be able to.")

# Check to see if the user can vote.
if user_age >= 18:
    print("You are old enough to vote.")
elif user_age < 18:
    print("You are not old enough to vote and still have " + str(18-user_age) + " years before you're old enough to do so.")

# Check to see if the user can legally buy alcohol.
if user_age >= 21:
    print("You are old enough to legally purchase alcohol.")
elif user_age < 21:
    print("You are not old enough to legally purchase alcohol and still have " + str(21-user_age) + " years before you're old enough to be able to.")

# Check to see if the user is eligible for a senior discount.
if user_age >= 65:
    print("You are old enough to be eligable for the senior discount.")
else:
    print("You are not old enough to be eligible for the senior discount and still have " + str(65-user_age) + " years before you're old enough to be able to.")

