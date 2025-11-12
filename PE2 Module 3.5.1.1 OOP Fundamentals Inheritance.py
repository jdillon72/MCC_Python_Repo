class Employee:
    """The Superclass: defines common traits for any employee."""

    def __init__(self, name, number):
        """
        Sets up the basic Employee details: name and employee number.
        """
        self._name = name      # For storing the employee's name. 
        self._number = number  # For storing the employee's ID number. 

    # --- Accessor (Getter) Methods ---

    def get_name(self):
        """Grabs and returns the employee's name when requested. Like handing over an ID badge."""
        return self._name

    def get_number(self):
        """Grabs and returns the employee's ID number."""
        return self._number

    # --- Mutator (Setter) Methods ---

    def set_name(self, name):
        """Allows changing the employee's name (in case of a legal change, or maybe just a typo at hire (Been there, done that. (A lot of people assume how my name is spelled without asking...)))."""
        self._name = name

    def set_number(self, number):
        """Allows changing the employee's ID number (hopefully not because they lost the old one (I've never lost mine...))."""
        self._number = number


class ProductionWorker(Employee):
    """The Subclass: a specialized worker, inheriting all Employee traits. It's an Employee... but with more steps!"""

    def __init__(self, name, number, shift, pay_rate):
        """
        Initializes the ProductionWorker. The first step is calling the parent constructor
        to handle name and number, then adding the worker-specific attributes.
        """
        # Calling the Superclass constructor using super().
        super().__init__(name, number)

        self._shift = shift        # Stores the shift number (1 for day, 2 for night). Don't mess this up, coffee budget depends on it. No, seriously. I can drink a whole pot myself.
        self._pay_rate = pay_rate  # Stores the hourly pay rate. The reason we're all here.

    # --- Accessor (Getter) Methods ---

    def get_shift(self):
        """
        Returns the shift as a clear string instead of just the number (1 or 2).
        This translates the secret code into human language for the output.
        """
        if self._shift == 1:
            return "Day"
        elif self._shift == 2:
            return "Night"
        else:
            return "Error: Invalid Shift Value"

    def get_pay_rate(self):
        """Grabs and returns the worker's current hourly pay rate."""
        return self._pay_rate

    # --- Mutator (Setter) Methods ---

    def set_shift(self, shift):
        """Updates the worker's assigned shift (1 or 2)."""
        self._shift = shift

    def set_pay_rate(self, pay_rate):
        """Updates the worker's hourly pay rate. Hopefully a pay raise!"""
        self._pay_rate = pay_rate


def main():
    """
    The main script entry point for testing the classes.
    The script gathers user input, creates a worker object, and displays the final details.
    """
    print("Enter the following details of the Employee:")
    print("------------------------------------------")

    # Data from the user.
    employee_name = input("Enter Employee Name: ")
    employee_number = int(input("Enter Employee Number: "))
    pay_rate_input = float(input("Enter Pay Rate: "))
    # The shift must be an integer (1 or 2). Anything else is chaos.
    shift_input = int(input("Enter Shift Number (1 for day, 2 for night): "))

    # For creating the ProductionWorker object, passing in all the gathered info.
    worker = ProductionWorker(
        employee_name,
        employee_number,
        shift_input,
        pay_rate_input
    )

    # Displaying the stored data using the getter methods.
    print("\nDetails of Employee:")
    print("--------------------")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_number()}")
    # The get_shift() method handles the 1/2-to-Day/Night translation.
    print(f"Shift: {worker.get_shift()}")
    # Formatting the pay rate to two decimal places for currency.
    print(f"Pay Rate: {worker.get_pay_rate():.2f}")


# This standard block makes sure the main() function runs when the script is executed.
main()