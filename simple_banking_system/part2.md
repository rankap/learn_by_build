# Building a Simple Banking System: Part 2

In this part of the tutorial, we will enhance our basic banking system by adding the following features:

1. **Interest Calculation**: Users can earn interest on their balance after a certain period.
2. **Transferring Money Between Accounts**: Users can transfer money between two accounts.
3. **Saving Account Data to a File**: This will allow the system to persist account data across sessions.

---

## Step 1: Adding Interest Calculation

We’ll add a method that calculates interest based on the account balance and a predefined interest rate. This will allow users to earn interest on the money in their accounts.

### Modifying the `BankAccount` Class

```python
class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0, interest_rate=0.02):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.interest_rate = interest_rate

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

    def apply_interest(self):
        """Applies interest to the account balance based on the interest rate."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest}")
```

### Explanation:
- We added a new attribute, `interest_rate`, with a default value of `0.02` (2%).
- The `apply_interest` method calculates interest based on the balance and adds it to the account.

### Using the Interest Feature

To allow users to apply interest, we’ll add a new menu option in the main system:

```python
def apply_interest_to_account(accounts):
    account_number = input("Enter account number: ")

    if account_number in accounts:
        accounts[account_number].apply_interest()
    else:
        print("Account not found!")
```

Add the following to the main menu options:

```python
print("6. Apply interest")
```

And modify the main loop to handle this choice:

```python
elif choice == "6":
    apply_interest_to_account(accounts)
```

---

## Step 2: Transferring Money Between Accounts

Next, we’ll add the ability to transfer money from one account to another.

### Adding a Transfer Method

We’ll add a `transfer` method to the `BankAccount` class:

```python
def transfer(self, amount, target_account):
    if amount > 0:
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            print(f"${amount} transferred to {target_account.holder_name} successfully!")
        else:
            print("Insufficient balance for transfer.")
    else:
        print("Transfer amount must be positive.")
```

### Implementing the Transfer Feature

We’ll now add an option in the banking system to handle transfers between accounts:

```python
def transfer_money(accounts):
    from_account = input("Enter your account number: ")
    to_account = input("Enter the account number to transfer money to: ")

    if from_account in accounts and to_account in accounts:
        amount = float(input("Enter amount to transfer: "))
        accounts[from_account].transfer(amount, accounts[to_account])
    else:
        print("One or both account numbers not found!")
```

Add this to the main menu:

```python
print("7. Transfer money between accounts")
```

And handle the choice:

```python
elif choice == "7":
    transfer_money(accounts)
```

---

## Step 3: Saving Account Data to a File

To save the account data between sessions, we will use JSON to store account information in a file. This way, account data will persist even when the program is closed and reopened.

### Storing Account Data in JSON

First, we’ll create two functions for saving and loading account data.

```python
import json

def save_accounts_to_file(accounts, filename="accounts.json"):
    data = {acc.account_number: {"holder_name": acc.holder_name, "balance": acc.balance, "interest_rate": acc.interest_rate} for acc in accounts.values()}
    
    with open(filename, "w") as file:
        json.dump(data, file)
    print("Account data saved to file.")

def load_accounts_from_file(filename="accounts.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            accounts = {acc_num: BankAccount(acc_num, info["holder_name"], info["balance"], info["interest_rate"]) for acc_num, info in data.items()}
            print("Account data loaded from file.")
            return accounts
    except FileNotFoundError:
        print("No saved accounts found. Starting with empty accounts.")
        return {}
```

### Updating the Main System to Load and Save Data

We’ll modify the `main` function to load account data at the start and save it when the program exits.

```python
def main():
    accounts = load_accounts_from_file()

    while True:
        main_menu()
        choice = input("Choose an option (1-7): ")

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
            save_accounts_to_file(accounts)
            break
        elif choice == "6":
            apply_interest_to_account(accounts)
        elif choice == "7":
            transfer_money(accounts)
        else:
            print("Invalid choice! Please select a valid option.")
```

### Explanation:
- **`save_accounts_to_file`**: Converts account objects into a dictionary and saves the data as JSON.
- **`load_accounts_from_file`**: Loads account data from a JSON file and recreates the `BankAccount` objects.
- Accounts are saved automatically when the program exits.

---

## Full Enhanced Code

Here’s the complete updated code with the new features:

```python
import json

class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0, interest_rate=0.02):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.interest_rate = interest_rate

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

    def apply_interest(self):
        """Applies interest to the account balance."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest}")

    def transfer(self, amount, target_account):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                target_account.balance += amount
                print(f"${amount} transferred to {target_account.holder_name} successfully!")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("Transfer amount must be positive.")

def save_accounts_to_file(accounts, filename="accounts.json"):
    data = {acc.account_number: {"holder_name": acc.holder_name, "balance": acc.balance, "interest_rate": acc.interest_rate} for acc in accounts.values()}
    
    with open(filename, "w") as file:
        json.dump(data, file)
    print("Account data saved to file.")

def load_accounts_from_file(filename="accounts.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            accounts = {acc_num: BankAccount(acc_num, info["holder_name"], info["balance"], info["interest_rate"]) for acc_num, info in data.items()}
            print("Account data loaded from file.")
            return accounts
    except FileNotFoundError:
        print("No saved accounts found. Starting with empty accounts.")
        return {}

def main_menu():
    print("\n--- Welcome to the Simple Banking System ---")
    print("1. Create a new account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check account balance")
    print("5. Exit")
    print("6. Apply interest")
    print("7. Transfer money between accounts")

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
        amount = float(input("Enter amount to deposit

: "))
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

def apply_interest_to_account(accounts):
    account_number = input("Enter account number: ")

    if account_number in accounts:
        accounts[account_number].apply_interest()
    else:
        print("Account not found!")

def transfer_money(accounts):
    from_account = input("Enter your account number: ")
    to_account = input("Enter the account number to transfer money to: ")

    if from_account in accounts and to_account in accounts:
        amount = float(input("Enter amount to transfer: "))
        accounts[from_account].transfer(amount, accounts[to_account])
    else:
        print("One or both account numbers not found!")

def main():
    accounts = load_accounts_from_file()

    while True:
        main_menu()
        choice = input("Choose an option (1-7): ")

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
            save_accounts_to_file(accounts)
            break
        elif choice == "6":
            apply_interest_to_account(accounts)
        elif choice == "7":
            transfer_money(accounts)
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
```

---

## Conclusion

In this tutorial, we added interest calculations, money transfers, and the ability to save account data to a file. These features enhance our simple banking system, making it more functional and realistic. You can now build on this by adding more features such as overdraft limits, transaction history, or even user authentication.
