'''Create a class "BankAccount" with attributes account number and balance. Implement
methods to deposit and withdraw funds, and a display method to show the account details.'''

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    
    def display(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

# Example usage
account_number = input("Enter account number: ")
account = BankAccount(account_number)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Display\n4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        account.display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")