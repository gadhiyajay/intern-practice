# BankAccount.py

# Parent class BankAccount
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


# Child class SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def withdraw(self, amount):
        if self.get_balance() - amount < 100:
            print("Minimum balance of $100 required!")
        else:
            super().withdraw(amount)


# Main.py
def main():
    # Create a Bank Account object (A/c No. BA1234) with initial balance of $500
    BA1234 = BankAccount("BA1234", 500)

    # Create a Savings Account object (A/c No. SA1234) with initial balance of $1000
    SA1234 = SavingsAccount("SA1234", 1000)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            account = input("Enter account number (BA1234/SA1234): ")
            amount = float(input("Enter amount to deposit: "))
            if account == "BA1234":
                BA1234.deposit(amount)
            elif account == "SA1234":
                SA1234.deposit(amount)
            else:
                print("Invalid account number")
        elif choice == 2:
            account = input("Enter account number (BA1234/SA1234): ")
            amount = float(input("Enter amount to withdraw: "))
            if account == "BA1234":
                BA1234.withdraw(amount)
            elif account == "SA1234":
                SA1234.withdraw(amount)
            else:
                print("Invalid account number")
        elif choice == 3:
            account = input("Enter account number (BA1234/SA1234): ")
            if account == "BA1234":
                print(f"Account {account} balance: ${BA1234.get_balance()}")
            elif account == "SA1234":
                print(f"Account {account} balance: ${SA1234.get_balance()}")
            else:
                print("Invalid account number")
        elif choice == 4:
            print("Thank you for using our bank!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()