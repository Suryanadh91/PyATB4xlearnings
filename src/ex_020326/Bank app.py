# bank app
def balance_enquiry():
    print(f"Your current balance is: ${balance:.2f}")

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"Successfully deposited ${amount:.2f}. New balance: ${balance:.2f}")
    else:
        print("Error: Deposit amount must be positive.")

def withdraw(amount):
    global balance
    if 0 < amount <= balance:
        balance -= amount
        print(f"Successfully withdrew ${amount:.2f}. New balance: ${balance:.2f}")
    elif amount > balance:
        print("Error: Insufficient funds!")
    else:
        print("Error: Invalid withdrawal amount.")

def update_kyc(**docs):
    global kyc_documents
    kyc_documents.update(docs)
    print("KYC documents updated successfully.")

def check_kyc():
    if not kyc_documents:
        print("No KYC documents found.")
    else:
        print("--- KYC Documents ---")
        for doc, value in kyc_documents.items():
            print(f"{doc.upper()}: {value}")

# Initializing global variables
balance = 0.0
kyc_documents = {}

print("Welcome to ABC bank!")

while True:
    print("\n--- Menu ---")
    print("1. Balance enquiry")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check KYC")
    print("5. Update KYC")
    print("6. Exit")

    try:
        # Changed the prompt range to reflect all options
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            balance_enquiry()
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            deposit(amount)
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            withdraw(amount)
        elif choice == 4:
            check_kyc()
        elif choice == 5:
            # Capturing document details for the **docs kwargs
            doc_type = input("Enter document type (e.g., PAN, Aadhaar): ")
            doc_id = input(f"Enter {doc_type} number: ")
            update_kyc(**{doc_type: doc_id})
        elif choice == 6:
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please choose between 1 and 6.")
    except ValueError:
        print("Error: Please enter a valid numerical value.")

print("Thank you for banking with us!!")