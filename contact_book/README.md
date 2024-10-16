# How to Build a Contact Book in Python

In this tutorial, we’re going to build a **Contact Book** application using Python. This project will help you practice key programming concepts such as dictionaries, functions, loops, and user input handling. The contact book will allow users to add, view, search, and delete contacts from a simple command-line interface.

---

## What We’re Building

Our **Contact Book** app will:
- Allow users to **add new contacts**.
- **View** the list of saved contacts.
- **Search** for a contact by name.
- **Delete** a contact.
  
### Python Concepts Covered:
- Dictionaries
- Loops
- Functions
- User input handling

---

## Step 1: **Setting Up the Data Structure**

We’ll use a **dictionary** to store the contacts. The name of each person will be the key, and their phone number and email will be stored as values in a nested dictionary.

Here’s an example of what the structure might look like:

```python
contacts = {
    "John Doe": {"phone": "123-456-7890", "email": "johndoe@example.com"},
    "Jane Smith": {"phone": "987-654-3210", "email": "janesmith@example.com"}
}
```

- **Why a dictionary?**: A dictionary allows us to store the contact names as keys and the phone number and email as their values. This structure is efficient for looking up and modifying contacts.

---

## Step 2: **Creating the Main Menu**

The main menu will let users select what action they want to take. We’ll use a `while` loop to continuously show the menu until the user decides to exit.

Here’s the code for the main menu:

```python
def main_menu():
    print("\nWelcome to the Contact Book!")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")
```

### Breaking It Down:

- **Menu Display**: 
   ```python
   print("1. Add a new contact")
   ```
   - We print out the available options, allowing the user to select what action they want to perform.

---

## Step 3: **Adding New Contacts**

Next, we’ll write a function to allow users to add new contacts. The function will prompt the user to enter the contact’s name, phone number, and email, and then add it to the `contacts` dictionary.

Here’s the code for adding a new contact:

```python
def add_contact(contacts):
    name = input("Enter the contact's name: ").strip()
    phone = input("Enter the contact's phone number: ").strip()
    email = input("Enter the contact's email: ").strip()

    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print(f"Added {name} to your contact book.")
```

### Explanation:

1. **Getting User Input**:
   - We use `input()` to get the contact’s name, phone number, and email from the user.
   
2. **Checking if Contact Exists**:
   ```python
   if name in contacts:
       print("Contact already exists!")
   ```
   - Before adding a new contact, we check if the name already exists in the `contacts` dictionary.

3. **Adding the Contact**:
   ```python
   contacts[name] = {"phone": phone, "email": email}
   ```
   - If the contact doesn’t exist, we add it to the dictionary with their phone number and email.

---

## Step 4: **Viewing All Contacts**

We’ll now create a function that prints out all the contacts stored in the dictionary.

Here’s the code to view all contacts:

```python
def view_contacts(contacts):
    if contacts:
        print("\nYour Contacts:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("No contacts found.")
```

### Explanation:

1. **Checking for Empty Contact List**:
   ```python
   if contacts:
   ```
   - If the `contacts` dictionary is empty, we print a message saying there are no contacts.

2. **Looping Through Contacts**:
   ```python
   for name, details in contacts.items():
       print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
   ```
   - We loop through each contact and print their name, phone number, and email.

---

## Step 5: **Searching for a Contact**

To search for a contact, we’ll prompt the user to enter a name and look it up in the `contacts` dictionary.

Here’s the code for searching a contact:

```python
def search_contact(contacts):
    name = input("Enter the name of the contact to search for: ").strip()
    
    if name in contacts:
        print(f"Found contact: Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print(f"No contact found for {name}.")
```

### Explanation:

1. **Getting User Input**:
   ```python
   name = input("Enter the name of the contact to search for: ").strip()
   ```
   - We ask the user to input the name of the contact they want to search for.

2. **Checking if the Contact Exists**:
   ```python
   if name in contacts:
   ```
   - We check if the name exists in the `contacts` dictionary. If it does, we display the contact’s details; if not, we notify the user that no contact was found.

---

## Step 6: **Deleting a Contact**

Let’s add a function to allow the user to delete a contact. This function will ask the user for the contact’s name and remove it from the dictionary if it exists.

Here’s the code for deleting a contact:

```python
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted.")
    else:
        print(f"No contact found for {name}.")
```

### Explanation:

1. **Getting the Contact Name**:
   - We ask the user to input the name of the contact they want to delete.

2. **Deleting the Contact**:
   ```python
   del contacts[name]
   ```
   - If the contact exists, we use `del` to remove it from the dictionary.

---

## Step 7: **Putting Everything Together**

Now, let’s put everything together and create the main loop that will continuously prompt the user for actions until they choose to exit.

Here’s the full code:

```python
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

def main():
    contacts = {}
    while True:
        main_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

### Explanation of the Main Code:

- **Main Loop**: 
   ```python
   while True:
       main_menu()
       choice = input("\nEnter your choice: ").strip()
   ```
   - We continuously show the menu and get the user’s choice until they select "Exit" (option 5).

- **Handling User Choice**:
   ```python
   if choice == "1":
       add_contact(contacts)
   elif choice == "2":
       view_contacts(contacts)
   # ...
   ```
   - Depending

 on the user’s input, we call the appropriate function to add, view, search, or delete contacts.

---

## Conclusion

Congratulations! You’ve built a simple **Contact Book** in Python. You learned how to:
- Store and manage contact information using dictionaries.
- Use functions to organize different parts of your program.
- Implement user input handling in a command-line application.

This project can be expanded in many ways, such as adding validation for phone numbers and emails, or saving the contacts to a file so they persist between program runs.

Feel free to modify and extend this project as you continue learning!
