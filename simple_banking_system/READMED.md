# Building a Simple Banking System in Python

In this tutorial, we’ll build a basic **banking system** using Python. This system allows users to **create accounts**, **deposit money**, **withdraw money**, and **check balances**. It’s a great beginner project to help you learn how to work with classes, objects, and simple logic in Python.

## Features:
1. **Create an account**: Users can create a new account with a unique account number.
2. **Deposit money**: Users can add funds to their account.
3. **Withdraw money**: Users can withdraw funds from their account, as long as they have enough balance.
4. **Check balance**: Users can view their current account balance.

---

## Step 1: Setting Up the Account Class

We’ll create a class `BankAccount` to represent each account. This class will store the account holder’s name, account number, and balance.

```python
class BankAccount:
    def __init__(self, account_number, holder_name):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = 0.0  # New accounts start with a balance of 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully!")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"${amount} withdrawn successfully!")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account Balance: ${self.balance}")
```

### Explanation:
- `__init__`: Initializes the account with the account number, holder’s name, and sets the initial balance to `0.0`.
- `deposit`: Adds funds to the account, provided the amount is positive.
- `withdraw`: Allows withdrawal, but only if the account has enough funds.
- `check_balance`: Displays the current balance of the account.

---

## Step 2: Creating a Banking System Interface

We’ll create a simple interface that allows users to interact with their bank accounts. The system will have options to create an account, deposit money, withdraw money, and check the balance.

```python
def main_menu():
    print("\n--- Welcome to the Simple Banking System ---")
    print("1. Create a new account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check account balance")
    print("5. Exit")

def create_account(accounts):
    account_number = input("Enter a unique account number: ")
    holder_name = input("Enter the account holder's name: ")

    if account_number in accounts:
        print("Account number already exists! Try again.")
    else:
        new_account = BankAccount(account_number, holder_name)
        accounts[account_number] = new_account
        print(f"Account for {holder_name} created successfully!")

def deposit_money(accounts):
    account_number = input("Enter account number: ")

    if account_number in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[account_number].deposit(amount)
    else:
        print("Account not found!")

def withdraw_money(accounts):
    account_number = input("Enter account number: ")

    if account_number in accounts:
        amount = float(input("Enter amount to withdraw: "))
        accounts[account_number].withdraw(amount)
    else:
        print("Account not found!")

def check_balance(accounts):
    account_number = input("Enter account number: ")

    if account_number in accounts:
        accounts[account_number].check_balance()
    else:
        print("Account not found!")
```

### Explanation:
- **`main_menu`**: Displays the available options to the user.
- **`create_account`**: Allows the user to create a new account and adds it to the `accounts` dictionary.
- **`deposit_money`**: Lets the user deposit funds into an existing account.
- **`withdraw_money`**: Enables the user to withdraw money, checking for sufficient balance.
- **`check_balance`**: Displays the balance of an account.

---

## Step 3: Running the Banking System

Now we’ll set up the loop to run our banking system. The user will be able to continuously interact with the system until they choose to exit.

```python
def main():
    accounts = {}

    while True:
        main_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_money(accounts)
        elif choice == "3":
            withdraw_money(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            print("Thank you for using the Simple Banking System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")
```

### Explanation:
- **`main`**: This function handles the main logic. It repeatedly shows the main menu and performs actions based on the user's input.
- **accounts**: A dictionary that stores all bank accounts, using the account number as the key.

---

## Full Code

```python
class BankAccount:
    def __init__(self, account_number, holder_name):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully!")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"${amount} withdrawn successfully!")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account Balance: ${self.balance}")

def main_menu():
    print("\n--- Welcome to the Simple Banking System ---")
    print("1. Create a new account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check account balance")
    print("5. Exit")

def create_account(accounts):
    account_number = input("Enter a unique account number: ")
    holder_name = input("Enter the account holder's name: ")

    if account_number in accounts:
        print("Account number already exists! Try again.")
    else:
        new_account = BankAccount(account_number, holder_name)
        accounts[account_number] = new_account
        print(f"Account for {holder_name} created successfully!")

def deposit_money(accounts):
    account_number = input("Enter account number: ")

    if account_number in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[account_number].deposit(amount)
    else:
        print("Account not found!")

def withdraw_money(accounts):
    account_number = input("Enter account number: ")

    if account_number in accounts:
        amount = float(input("Enter amount to withdraw: "))
        accounts[account_number].withdraw(amount)
    else:
        print("Account not found!")

def check_balance(accounts):
    account_number = input("Enter account number: ")

    if account_number in accounts:
        accounts[account_number].check_balance()
    else:
        print("Account not found!")

def main():
    accounts = {}

    while True:
        main_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_money(accounts)
        elif choice == "3":
            withdraw_money(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            print("Thank you for using the Simple Banking System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
```

---

## How It Works:
1. **Creating Accounts**: Each account is unique based on the account number. The user’s name is also stored.
2. **Depositing and Withdrawing**: Users can deposit any positive amount, and they can withdraw money as long as they have enough in their account.
3. **Checking Balance**: The `check_balance` method gives an up-to-date view of the account's balance.
4. **Menu System**: The program runs in a loop, allowing users to keep interacting with the banking system until they choose to exit.

---

## in Part 2 we will add 
- Add more features like interest calculations or transferring money between accounts.
- Save account data to a file so that the account information persists across sessions.

This project is a great way to practice working with **classes**, **methods**, and **basic logic** in Python. Try adding your own features and building on top of this simple system!
