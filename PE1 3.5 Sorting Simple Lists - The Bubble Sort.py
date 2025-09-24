# Empty list variable.
name_list = []

# User inputs to add fives to list. 
name_input_1 = input("Please enter the first of five names you'll add to a list.: ")
name_list.append(name_input_1.lower())
name_input_2 = input("Please enter the second of five names you'll add to a list.: ")
name_list.append(name_input_2.lower())
name_input_3 = input("Please enter the Third of five names you'll add to a list.: ")
name_list.append(name_input_3.lower())
name_input_4 = input("Please enter the fourth of five names you'll add to a list.: ")
name_list.append(name_input_4.lower())
name_input_5 = input("Please enter the last of five names you'll add to a list.: ")
name_list.append(name_input_5.lower())

print()
print(name_list)

# While loop for swapping the order of the names in the list.

swapped = True # Boolen True variable.
while swapped:
    swapped = False
    # For loop for sorting names.
    for i in range(len(name_list) - 1):
        if name_list[i] > name_list[i+1]:
            name_list[i], name_list[i+1] = name_list[i+1], name_list[i]
            swapped = True 

# Name list printed after while loop.
print(name_list)

# Printing of lists.
print()
name_list.reverse()
print(name_list)
