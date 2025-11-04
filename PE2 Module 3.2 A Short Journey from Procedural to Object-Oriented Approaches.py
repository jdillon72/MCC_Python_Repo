"""A class to represent a person with personal data."""

class Person:

    def __init__(self, name, address, age, phone):
        # Use underscore to signify private variable convention.
        self._name = name # Name is a string.
        self._address = address # Address is a string.
        self._age = age # Age is a string.
        self._phone = phone # Phone is a string.

    # Getter methods (Accessors).
    def get_name(self):
        # Simply returns the stored value.
        return self._name

    def get_address(self):
        return self._address # Intentional missing comment/docstring here.

    def get_age(self):
        return self._age

    # Slightly different naming convention for this getter's comment.
    def get_phone(self):
        return self._phone

    # Mutator Methods (Setters)
    def set_name(self, new_name):
        self._name = new_name

    # Using 'val' instead of 'new_address' to break the uniformity.
    def set_address(self, val):
        self._address = val

    def set_age(self, new_age):
        # A little error check for age, because why not? It's always best to be on the safe side. Seriously. Safety First.
        if isinstance(new_age, int) and new_age >= 0:
            self._age = new_age
        else:
            print(f"Invalid age: {new_age}. Age must be a non-negative integer.")

    def set_phone(self, new_phone):
        self._phone = new_phone

    # Display Data Method.
    def get_info(self):
        """Returns the person's info as a formatted string."""
        info = (
            f"Name:    {self._name}\n"
            f"Address: {self._address}\n"
            f"Age:     {self._age}\n"
            f"Phone:   {self._phone}"
        )
        return info

# Creating Instances Objects and Displaying Data.

# Quick check to confirm we've started the main execution block
print("Starting instance creation...")

print("--- Creating and Displaying Initial Person Objects ---")
# Three fictional instances (objects) of the Person class. No identity fraud here.
# Instance for make-up information.
person1 = Person("Alex Turing", "123 Main Street", 35, "555-1234")
# Instance for a friend.
person2 = Person("Jane Doe", "456 East Ave", 22, "555-5678")
# Instance for a family member.
person3 = Person("Robert Smith", "789 West Rd", 58, "555-9012")

# Display the final results for verification.
print("\n--- Person 1 Info ---")
print(person1.get_info())

print("\n--- Person 2 Info ---")
print(person2.get_info())

print("\n--- Person 3 Info ---")
print(person3.get_info())

# Mutator (Setter) method to change data.
print("\n--- Updating Person 2's Phone Number (Setter Example) ---")
person2.set_phone("555-4321")
print(person2.get_info()) # Check the update.