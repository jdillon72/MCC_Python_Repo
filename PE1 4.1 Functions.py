# Function definition for square.
def square(side):
    # Area calculation is side * side, and it uses the passed-in parameter.
    square_area = side * side
    print(f"The area of the square is {square_area} square units.")

# Function definition for circle:
def circle(radius):
    # The area formula is now fixed to use the correct Python exponentiation operator (**).
    circle_area = (radius ** 2) * 3.14
    print(f"The area of the circle is {circle_area} square units.")

# Test the Functions with Sample Values

# Call square with a sample value (e.g., 4)
square(4)

# Call circle with a sample value (e.g., 5)
circle(5)

