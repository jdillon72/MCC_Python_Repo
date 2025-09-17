# Variables for inserting both user input integers:
int_1 = int(input("Please enter an integer: "))
int_2 = int(input("Please enter a second integer: "))

#Logical 'and' operators for interpreting integers variables.
if int_1 > 0 and int_2 > 0:
    print("Both numbers are greater than 0: TRUE ")
else:
    print("Both numbers are greater than 0: FALSE")

if int_1 < 100 and int_2 < 100:
    print("Both numbers are greater than 100: TRUE")
else:
    print("Both numbers are greater than 100: FALSE")

# Logical operators for 'or'.

if int_1 % 2 == 0 or int_2 % 2 == 0:
    print("One of the integers input is even: TRUE")
else:
    print("One of the integers input is even: FALSE")

if int_1 < 100 or int_2 < 100:
    print("One of the numbers is less than 100: TRUE")
else:
    print("One of the numbers is less than 100: FALSE")

#Logical operator for 'not' to interpret integers.
if int_1 != int_2:
    print("Int_1 is not equal to Int_2: TRUE")
else:
    print("Int_1 is not equal to Int_2: FALSE")

if int_1 != 0:
    print("Int_1 is not equal to 0: TRUE")
else:
    print("Int_1 is not equal to 0: FALSE")