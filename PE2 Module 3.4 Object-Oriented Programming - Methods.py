"""
    A class to represent a pet with attributes like kind, breed, and name.
"""

# New Pet Class.
class Pet:

    def __init__(self, kind, breed, name):
        """
        The constructor method to initialize a new Pet instance.
        """
        # Define attributes (kind, breed, name).
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    # Replaced getter methods with the @property decorator.
    @property
    def kind(self):
        """Returns the kind of the pet."""
        return self.__kind

    @property
    def breed(self):
        """Returns the breed of the pet."""
        return self.__breed

    @property
    def name(self):
        """Returns the name of the pet."""
        return self.__name


    def print_details(self):
        """
        Prints the details of the pet in a formatted string.
        """
        print(f"--- Pet Details ---")
        # Accessing properties like attributes: pet1.name instead of pet1.get_name().
        print(f"Name: {self.name}")
        print(f"Kind: {self.kind}")
        print(f"Breed: {self.breed}")
        print(f"-------------------")


# Main Execution Block Function

def main():
    """
    Handles the creation of instances and demonstration of special functions.
    """
    # Create three objects of the Pet class with different kinds, breeds, and names.
    print("Creating Pet instances...\n")
    pet1 = Pet("Dog", "Golden Retriever", "Buddy") # Best Boys.
    pet2 = Pet("Cat", "Siamese", "Mittens") # Feline friends.
    pet3 = Pet("Bird", "Parakeet", "Sky") # Feather brains...

    # Call the print_details method for each object that you created.
    pet1.print_details()
    pet2.print_details()
    pet3.print_details()

    print("\n--- Special Function Demonstration: isinstance() ---")
    # Check if pet1 is an instance of the Pet class.
    print(f"Is pet1 an instance of the Pet class? {isinstance(pet1, Pet)}")

    # Check if an arbitrary string is an instance of the Pet class (it shouldn't be).
    print(f"Is 'Hello' an instance of the Pet class? {isinstance('Hello', Pet)}")

    # Demonstration of __name__ for context.
    print(f"Class name using __name__: {Pet.__name__}")


# Main function call.
main()