# Building a Contact Book in Python: Part 2 - Using JSON to Save and Retrieve Data

In Part 1 of our Contact Book tutorial, we built a simple command-line application that allowed users to add, view, search, and delete contacts. In this part, we'll enhance our application by adding functionality to save contacts to a JSON file and load them back when the application starts. This way, our contacts will persist even after the program exits.

---

## What We’re Adding

- **Saving Contacts**: We’ll save the contacts to a JSON file whenever a new contact is added or an existing contact is deleted.
- **Loading Contacts**: We'll load the contacts from the JSON file when the application starts, so users can continue where they left off.

### Python Concepts Covered:
- Working with JSON files
- File handling (reading and writing files)
- Error handling

---

## Step 1: **Importing the JSON Module**

To work with JSON in Python, we need to import the `json` module. This module provides methods for converting Python objects to JSON format and vice versa.

At the beginning of your code, add the following import statement:

```python
import json
```

---

## Step 2: **Loading Contacts from a JSON File**

We'll create a function to load contacts from a JSON file. If the file doesn't exist or is empty, we’ll return an empty dictionary.

Here’s the code for loading contacts:

```python
def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            contacts = json.load(file)
            print("Contacts loaded successfully.")
            return contacts
    except FileNotFoundError:
        print("No contacts file found. Starting with an empty contact book.")
        return {}
    except json.JSONDecodeError:
        print("Error reading contacts. Starting with an empty contact book.")
        return {}
```

### Explanation:

1. **Try-Except Block**:
   - We use a `try` block to attempt to open and load the JSON file. If the file is not found, a `FileNotFoundError` will be raised, and we’ll return an empty dictionary. If there’s an error in reading the JSON file (like if it’s corrupted), we handle it with `json.JSONDecodeError`.

2. **Loading Data**:
   ```python
   contacts = json.load(file)
   ```
   - If the file is successfully opened, we read the contents into the `contacts` dictionary.

---

## Step 3: **Saving Contacts to a JSON File**

Next, we’ll create a function to save the contacts to a JSON file whenever a contact is added or deleted.

Here’s the code for saving contacts:

```python
def save_contacts(contacts, filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)
        print("Contacts saved successfully.")
```

### Explanation:

1. **Opening the File**:
   ```python
   with open(filename, 'w') as file:
   ```
   - We open the file in write mode (`'w'`). If the file exists, it will be overwritten.

2. **Dumping Data**:
   ```python
   json.dump(contacts, file, indent=4)
   ```
   - We use `json.dump()` to convert the `contacts` dictionary to JSON format and write it to the file. The `indent=4` argument makes the JSON file more readable by adding indentation.

---

## Step 4: **Integrating Load and Save in the Main Code**

Now, we’ll modify our main function to load contacts at the start and save them whenever a contact is added or deleted. Here’s the updated code:

```python
def main():
    filename = 'contacts.json'
    contacts = load_contacts(filename)

    while True:
        main_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts, filename)  # Save contacts after adding
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
            save_contacts(contacts, filename)  # Save contacts after deleting
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```

### Explanation:

1. **Loading Contacts at Start**:
   ```python
   contacts = load_contacts(filename)
   ```
   - When the program starts, we load any existing contacts from the `contacts.json` file.

2. **Saving Contacts**:
   - After adding or deleting a contact, we call the `save_contacts()` function to ensure the changes are written to the JSON file.

---

## Complete Code

Here’s the complete code for the Contact Book application with JSON integration:

```python
import json

def main_menu():
    print("\nWelcome to the Contact Book!")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter the contact's name: ").strip()
    phone = input("Enter the contact's phone number: ").strip()
    email = input("Enter the contact's email: ").strip()

    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print(f"Added {name} to your contact book.")

def view_contacts(contacts):
    if contacts:
        print("\nYour Contacts:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("No contacts found.")

def search_contact(contacts):
    name = input("Enter the name of the contact to search for: ").strip()
    
    if name in contacts:
        print(f"Found contact: Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print(f"No contact found for {name}.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted.")
    else:
        print(f"No contact found for {name}.")

def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            contacts = json.load(file)
            print("Contacts loaded successfully.")
            return contacts
    except FileNotFoundError:
        print("No contacts file found. Starting with an empty contact book.")
        return {}
    except json.JSONDecodeError:
        print("Error reading contacts. Starting with an empty contact book.")
        return {}

def save_contacts(contacts, filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)
        print("Contacts saved successfully.")

def main():
    filename = 'contacts.json'
    contacts = load_contacts(filename)

    while True:
        main_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts, filename)  # Save contacts after adding
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
            save_contacts(contacts, filename)  # Save contacts after deleting
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

---

## Conclusion

You’ve now enhanced your **Contact Book** application by integrating JSON file handling, allowing your contact information to persist across sessions. You learned how to read from and write to JSON files in Python, which is an essential skill for building data-driven applications.

Feel free to expand this project further by adding more features, such as editing contacts, validating user input, or even creating a graphical user interface (GUI) using libraries like Tkinter.

Happy coding!
