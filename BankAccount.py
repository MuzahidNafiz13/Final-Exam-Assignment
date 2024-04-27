import random
class BankAccount:
    def __init__(self, name, email, address, account_type): #all requrement
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = self.generate_account_number() #random account number
        self.balance = 0 #universally 0
        self.transaction_history = [] #List
        self.loan_count = 0

    def generate_account_number(self):
        return random.randint(1000000000, 9999999999)

    def deposit(self, amount):
        self.balance += amount #balace= 0+amount
        self.transaction_history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded") #otirikto
        else:
            self.balance -= amount #balace= blance-amount
            self.transaction_history.append(f"Withdrawal: {amount}")

    def check_balance(self):
        print(f"Available Balance: {self.balance}") #Constructor to function

    def view_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction) #tran-his dekhano
    
    def take_loan(self, amount):
        if self.loan_count < 2:
            self.balance += amount
            self.loan_count += 1
            self.transaction_history.append(f"Loan Taken: {amount}")
        else:
            print("You have already taken two loans.")

    def transfer_amount(self, recipient, amount):
        if amount > self.balance:
            print("Insufficient balance") #taka nai prothome
        else:
            self.withdraw(amount)
            recipient.deposit(amount)
            self.transaction_history.append(f"Transfer to {recipient.name}: {amount}")
            recipient.transaction_history.append(f"Received from {self.name}: {amount}")