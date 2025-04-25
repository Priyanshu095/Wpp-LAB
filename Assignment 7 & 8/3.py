'''Write a Python program to create a class representing a bank. Include methods for managing
customer accounts and transactions.'''

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account({self.account_number}, {self.account_holder}, Balance: {self.balance})"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, account_holder)
            return True
        return False

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

def main():
    bank = Bank()

    while True:
        print("\nBank Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Accounts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = int(input("Enter account number: "))
            account_holder = input("Enter account holder name: ")
            if bank.create_account(account_number, account_holder):
                print("Account created successfully.")
            else:
                print("Account already exists.")

        elif choice == '2':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(account_number)
            if account:
                account.deposit(amount)
                print("Deposit successful.")
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(account_number)
            if account and account.withdraw(amount):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed. Account not found or insufficient balance.")

        elif choice == '4':
            print("\nAccounts in Bank:")
            for account in bank.accounts.values():
                print(account)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
