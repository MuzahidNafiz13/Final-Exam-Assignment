from BankAccount import BankAccount

class Bank:
    def __init__(self):
        self.accounts = []
        self.loan_enabled = True

    def create_account(self, name, email, address, account_type):
        account = BankAccount(name, email, address, account_type)
        self.accounts.append(account)# list e dhukano
        print(f"Account created successfully. Account Number: {account.account_number}")

    def delete_account(self, account_number):
        for account in self.accounts: #sob account a
            if account.account_number == account_number: #number mille
                self.accounts.remove(account)
                print("Account deleted successfully.")
                return
        else:
            print("Account not found.")

    def view_accounts(self):
        print("List of Accounts:")
        for account in self.accounts:
            print(f"Name: {account.name}, Account Number: {account.account_number}, Account Type: {account.account_type}")

    def check_total_balance(self):
        total_balance = sum(account.balance for account in self.accounts)
        print(f"Total Available Balance: {total_balance}")

    def check_total_loan_amount(self):
        total_loan_amount = sum(account.balance for account in self.accounts if account.loan_count > 0)
        print(f"Total Loan Amount: {total_loan_amount}")

    def loan_feature_activation(self): # How not works
        self.loan_enabled = not self.loan_enabled
        if self.loan_enabled:
            print("Loan feature enabled.")
        else:
            print("Loan feature disabled.")