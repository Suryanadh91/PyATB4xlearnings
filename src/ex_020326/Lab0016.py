# bank app
kyc_documents = {}
balance = 0.0
def balance_enquiry():
    print(f"Your current balance is {balance}")

def deposit(amount):
    global balance
    if amount >= 0:
        balance += amount
    else:
        print("Invalid amount pls Re-try!!")
    print(f"The amount {amount} is now deposited and your balance is {balance}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
    elif amount > balance:
        print("Error: Insufficient funds pls Re-try!!")
    else:
        print("Error: Invalid amount pls Re-try!!")
    print(f"The amount {amount} is now withdrew and your balance is {balance}")

def check_kyc():
    global kyc_documents
    if not kyc_documents:
        print("No documents found!!")
    else:
        print("---KYC Documents Found---")
        for doc,value in kyc_documents.items():
            print(f"{doc} : {value}")

        
def update_kyc(**docs):
    global kyc_documents
    kyc_documents.update(docs)
    print("---KYC Documents Updated---")
    print(f"{kyc_documents}")


if __name__ == "__main__":
    print("Welcome to ABC bank!")

    while True:
        print("1. Balance enquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("Enter your choice (1-6): "))
        if choice == 1:
            balance_enquiry()
        elif choice == 2:
            amt = float(input("Enter amount to deposit: "))
            deposit(amt)
        elif choice == 3:
            amt = float(input("Enter amount to withdraw: "))
            withdraw(amt)
        elif choice == 4:
            check_kyc()
        elif choice == 5:
            doc_type = input("Enter document type (e.g., PAN, Aadhaar): ")
            doc_id = input(f"Enter {doc_type} number: ")
            update_kyc(**{doc_type: doc_id})
        elif choice == 5:
            print("Thank you")
            break
        else:
            print("Invalid choice pls Re-try!!")

    print("Thank you for banking with us!!")
