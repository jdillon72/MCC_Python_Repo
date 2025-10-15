# Importing custom math modules.
from math_operations import calculator, geometry

# Regular math call.
result = calculator.add(7, 2)
print("Addition Result:", result)

# Geometry call for rectangle.
second_result = geometry.rectangle_area(7,2)
print("Rectangle Area result:", second_result)

# Geometry call for circles.
third_result = geometry.circle_area(7)
print("Circle Area Result:", third_result)

# Geometry call for triangles.
fourth_result = geometry.triangle_area(7, 2)
print("Triangle Area Result:", fourth_result)
