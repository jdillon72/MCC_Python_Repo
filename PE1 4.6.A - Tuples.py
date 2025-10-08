# Defining the main tuple and function main().

def main(): 
    programming_classes = ('Intro to Python','Advanced Python','Database Essentials','Web Development Basics','Data Structures in Python','Web Design Fundamentals')
    # Print statement to begin list of classes.
    print("--List of Classes required for certificate--")
    #For loop to list courses in called function.
    for course in programming_classes:
        print(f"- {course}")
    
    #Print statement for end of list.
    print("--------------")

    # For printing number of courses.
    num_of_courses = len(programming_classes)
    print(f"Total courses required: {num_of_courses}")

# To make sure the main function is used in this program.
if __name__ == "__main__":
    main()
    