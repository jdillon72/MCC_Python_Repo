# List variable containing numbers acting as numbers for seats.

seat_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("The numbered seats are still available: " + str(seat_list))

# While loop to manage available seats in list.

while True:
    seat_input = int(input("Please pick a seat by entering its number. Please enter the number '0' when your purchase is complete to exit the program: "))
    
    if seat_input.isdigit():
        seat_number = int(seat_input)
        print("Invalid input. Please enter a number.")
        if seat_number == 0: # If statement to handle exiting the program.
            print("Thank you for your purchase. Have a good day!")
            break
        elif seat_number in seat_list: # Elif to handle purchase of 'ticket' for seat.
            seat_list.remove(seat_number)
            print("You have successfully purchased Seat " + str(seat_number) + ".")
            print("The following seats are still available for purchase.: " + str(seat_list))
        elif seat_number > 20 or seat_number < 1: # Elif to handle numbers outside of range. on list.
            print("Sorry, this seat number is not a valid choice. Please choose a number between 1 and 20.")
        else:
            print("Sorry, that seat has already been sold. Please choose the next available seat.")    
    else: #Else statement to handle numbered seats that have already been purchased by another user.
        print("Sorry, that seat has already been sold. Please choose the next available seat.")
