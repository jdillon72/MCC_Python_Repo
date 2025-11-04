"""
    A class to represent a pet in the veterinary office system.
"""

# Pet Class.
class Pet:
    
    # Class Variable: for the name of the veterinary office. Trying to keep it light here. My dogs get anxious at the vet.
    vet_name = "Dr. Fubu's Toy Review Clinic"

    # Instance Variables defined in __init__.
    def __init__(self, name, animal_type, age):
        # The variables must be private (using the double underscore) for demonstration.
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        # A variable to indicate if the pet has a microchip.
        self.__microchipped = False

    # Property/Getter for 'name'.
    @property
    def name(self):
        return self.__name

    # Setter for 'name'.
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not new_name.strip():
            print("Error: Name must be a non-empty string.")
        else:
            self.__name = new_name.strip()

    # Property/Getter for 'microchipped'.
    @property
    def microchipped(self):
        return self.__microchipped

    # Setter for 'microchipped' (used as set_status method).
    @microchipped.setter
    def microchipped(self, status):
        if isinstance(status, bool):
            self.__microchipped = status
        else:
            print("Error: Microchip status must be True or False.")

    # Other Methods for program at large.
    def display_pet_info(self):

        chip_status = "Yes" if self.__microchipped else "No"
        print("--- Pet Details ---")
        print(f"Name: {self.__name}")
        print(f"Type: {self.__animal_type}")
        print(f"Age: {self.__age} years")
        print(f"Microchipped: {chip_status}")
        print(f"Veterinary Office: {Pet.vet_name}")
        print("-------------------")

    def __str__(self):
        return f"Pet(Name: {self.__name}, Type: {self.__animal_type}, Age: {self.__age})"

    # Method for displaying information: Use __dict__ to print attributes.
    def print_all_attributes(self):
        print(f"\n--- Attributes for Pet '{self.__name}' ---")
        # Use __dict__ to print all instance variables
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")
        print("------------------------------------------")

    # Static Method.
    @staticmethod
    def display_office_info():
        # Access the class variable directly.
        print(f"\nWelcome to {Pet.vet_name}!")
        print("We provide excellent care for all your beloved companions.")

# --- Example Usage (main program logic) ---
def main():
    # Creating a Pet object.
    pet2 = Pet("Whiskers", "Cat", 3)
    pet3 = Pet("Squawk", "Parrot", 10)
    pet1=Pet("Fido", "Dog", 5)  # Inconsistent spacing here.

    print("\n--- Testing Setters and Getters ---") # A helpful print for testing
    
    # For showing the use of getter and setter for 'name'.
    print(f"\nInitial Name (Getter): {pet1.name}")
    pet1.name="Sparky" # Calls the setter (Inconsistent spacing here.)
    print(f"New Name after Setter: {pet1.name}")

    # Written property/setter to check for microchip status.
    pet1.microchipped = True # Calls the setter for microchipped status.
    print(f"Microchip Status (Getter): {pet1.microchipped}")


    print("\n--- Pet Display ---") # Another separator print
    
    # Displays pet information (using the method).
    pet1.display_pet_info()

    # Displays all attributes (using __dict__).
    pet1.print_all_attributes()

    # Displays all attributes for a second pet.
    pet2.print_all_attributes()

    # Display office info (using the static method).
    Pet.display_office_info()

    # Print the pet object using __str__.
    print(f"\nString representation of pet3: {pet3}")

    # Demonstration name validation (should print an error message).
    pet1.name="" # Inconsistent spacing here.

main()