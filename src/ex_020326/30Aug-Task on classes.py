class Employee:
    # Constructor to initialize the attributes
    def __init__(self, name, age, phone, address, eid):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid

    # Behavior: walk
    def walk(self):
        print(f"{self.name} is walking.")

    # Behavior: talk
    def talk(self):
        print(f"{self.name} is talking.")

    # Behavior: print details
    def print_details(self):
        print("\n--- Employee Details ---")
        print(f"Employee ID : {self.eid}")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Phone       : {self.phone}")
        print(f"Address     : {self.address}")
        print("-" * 25)


# Function to collect user input and create an employee object
def get_employee_input(employee_label):
    print(f"\nEnter details for {employee_label}:")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    phone = input("Enter Phone: ")
    address = input("Enter Address: ")
    eid = input("Enter Employee ID: ")

    # Returning a new Employee object initialized with the inputs
    return Employee(name, age, phone, address, eid)


# --- Main Program Execution ---

# 1. Ask the user for E1 and E2 details
E1 = get_employee_input("Employee 1 (E1)")
E2 = get_employee_input("Employee 2 (E2)")

# 2. Print the details of E1 and E2 via the print_details function
E1.print_details()
E2.print_details()

# 3. Demonstrating behaviors
E1.walk()
E2.talk()