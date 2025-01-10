import getpass
from models import add_user, validate_login, get_user_details, record_transaction
from database import init_db

def main():
    init_db()
    while True:
        print("\nBANKING SYSTEM")
        print("1. ADD USER")
        print("2. SHOW USER")
        print("3. LOGIN")
        print("4. EXIT")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_user_interface()
        elif choice == '2':
            show_user_interface()
        elif choice == '3':
                login_interface()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_user_interface():
    print("\nADD USER")
    name = input("Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    city = input("City: ")
    password = getpass.getpass("Password: ")
    balance = float(input("Initial Balance (minimum 2000): "))
    contact_number = input("Contact Number: ")
    email = input("Email ID: ")
    address = input("Address: ")

    account_number = add_user(name, dob, city, password, balance, contact_number, email, address)
    print(f"User added successfully! Account Number: {account_number}")

def show_user_interface():
    account_number = input("Enter account number: ")
    user = get_user_details(account_number)
    if user:
        print("\nUSER DETAILS")
        print(f"Name: {user['name']}")
        print(f"Account Number: {user['account_number']}")
        print(f"Date of Birth: {user['dob']}")
        print(f"City: {user['city']}")
        print(f"Balance: {user['balance']}")
        print(f"Contact Number: {user['contact_number']}")
        print(f"Email: {user['email']}")
        print(f"Address: {user['address']}")
    else:
        print("User not found.")

def login_interface():
    print("\nLOGIN")
    account_number = input("Account Number: ")
    password = getpass.getpass("Password: ")
    
    user = validate_login(account_number, password)
    if user:
        print("Login successful!")
        user_dashboard(user)
    else:
        print("Invalid credentials.")

def user_dashboard(user):
    while True:
        print("\nUSER DASHBOARD")
        print("1. Show Balance")
        print("2. Show Transactions")
        print("3. Credit Amount")
        print("4. Debit Amount")
        print("5. Transfer Amount")
        print("6. Activate/Deactivate Account")
        print("7. Change Password")
        print("8. Update Profile")
        print("9. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print(f"Your balance is: {user['balance']}")
        elif choice == '2':
            show_transactions(user['account_number'])
        elif choice == '3':
            credit_amount(user['account_number'])
        elif choice == '4':
            debit_amount(user['account_number'])
        elif choice == '5':
            transfer_amount(user['account_number'])
        elif choice == '6':
            activate_deactivate_account(user['account_number'])
        elif choice == '7':
            change_password(user['account_number'])
        elif choice == '8':
            update_profile(user['account_number'])
        elif choice == '9':
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

def show_transactions(account_number):
    # Implement the logic to show transactions for a given account number
    pass

def credit_amount(account_number):
    amount = float(input("Enter amount to credit: "))
    if record_transaction(account_number, 'credit', amount):
        print("Amount credited successfully.")
    else:
        print("Failed to credit amount.")

def debit_amount(account_number):
    amount = float(input("Enter amount to debit: "))
    if record_transaction(account_number, 'debit', amount):
        print("Amount debited successfully.")
    else:
        print("Insufficient funds.")

def transfer_amount(account_number):
    # Implement the logic to transfer amount from one account to another
    pass

def activate_deactivate_account(account_number):
    # Implement the logic to activate/deactivate account
    pass

def change_password(account_number):
    # Implement the logic to change password
    pass

def update_profile(account_number):
    # Implement the logic to update user profile
    pass

if __name__ == '__main__':
    main()
