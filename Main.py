from Bank import Bank
from BankAccount import BankAccount

bank = Bank()

def admin_panel(bank):
    while True:
        print("\n\t $|Admin Panel|$ \t")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. Check Total Available Balance")
        print("5. Check Total Loan Amount")
        print("6. Loan Feature Activation")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.create_account(name, email, address, account_type)
        elif choice == "2":
            account_number = int(input("Enter account number to delete: "))
            bank.delete_account(account_number)
        elif choice == "3":
            bank.view_accounts()
        elif choice == "4":
            bank.check_total_balance()
        elif choice == "5":
            bank.check_total_loan_amount()
        elif choice == "6":
            bank.loan_feature_activation()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def find_account(bank, account_number):
    for account in bank.accounts:
        if account.account_number == account_number:
            return account
    return None

def user_panel(bank):
    while True:
        print("\n\t[O_O] User Panel [O_O]\t")

        print("0. Create Account")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Amount")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "0":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.create_account(name, email, address, account_type)
        elif choice == "1":
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter deposit amount: "))
            account = find_account(bank, account_number)
            if account:
                account.deposit(amount)
                print("Amount Have Been Deposited Successfully")
            else:
                print("Account not found.")
        elif choice == "2":
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter withdrawal amount: "))
            account = find_account(bank, account_number)
            if account :
                account.withdraw(amount)
                print("Withdraw Complete")
            else:
                print("Account not found.")
        elif choice == "3":
            account_number = int(input("Enter your account number: "))
            account = find_account(bank, account_number)
            if account:
                account.check_balance()
            else:
                print("Account not found.")
        elif choice == "4":
            account_number = int(input("Enter your account number: "))
            account = find_account(bank, account_number)
            if account:
                account.view_transaction_history()
            else:
                print("Account not found.")
        elif choice == "5":
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter loan amount: "))
            account = find_account(bank, account_number)
            if account:
                if bank.loan_enabled:
                    account.take_loan(amount)
                    print("Loan Has Been Taken")
                else:
                    print("Loan feature is currently disabled.")#Loan feature activation off
            else:
                print("Account not found.")
        elif choice == "6":
            sender_number = int(input("Enter sender account number: "))
            recipient_number = int(input("Enter recipient account number: "))
            amount = float(input("Enter transfer amount: "))
            sender = find_account(bank, sender_number)
            recipient = find_account(bank, recipient_number)
            if sender and recipient:
                sender.transfer_amount(recipient, amount)
                print("Transfer Complete")
            else:
                print("One or both accounts not found.")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

while True:
    print("\n\t|^_^| Welcome to the Bank |^_^|\t")
    print("1. Admin Panel")
    print("2. User Panel")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        admin_panel(bank)
    elif choice == "2":
        user_panel(bank)
    elif choice == "3":
        print("\n\tThank you for using the Bank. Goodbye!\t")
        break
    else:
        print("Invalid choice. Please enter a valid option.")    

