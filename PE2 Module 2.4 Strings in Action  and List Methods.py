# Main function to house programming and run programming.
def main():

# Programming to build list from user input from user.
    book_titles = []

# Counter for while loop. 
    count = 0
    
    #While loop to prompt user for 10 titles of books. The loop will continue as long as the count as less than 10.
    while count < 10:
        # Prompt variable for user input. 
        prompt = f"Enter book title #{count + 1} of 10: "
        user_input = input(prompt)
    
        # Variable for ensuring proper capitalization for user input and items in list.
        formatted_title = user_input.title()
        book_titles.append(formatted_title)
        
        #Count variable to increase the count toward the exit condition.
        count += 1
    
    #Variable for sorting book titles alphabetically.     
    books_sorted = sorted(book_titles)
    
    # For loop for printing titles in list.
    for title in books_sorted:
        print(title)
    
    #Print statement for printing the length of the list.
    print(f"Total titles processed: {len(books_sorted)}")

# Main function to run program.
main()

    

    
