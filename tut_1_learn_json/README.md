# Learn How to Use JSON as a Small Database for Your Python Projects by Building a Hotel Accounting System

Are you tired of setting up and managing bulky databases for your small projects? If you’ve got a small-scale application and need something lightweight, JSON (JavaScript Object Notation) can be your best buddy! In this tutorial, we’ll build a simple Hotel Accounting System using Python, and we’ll use JSON to store and manage our data.

But first, let’s dive into the basics of JSON files, the standard format, and how to use Python's `json` module to manipulate these files.

---

### What is JSON?

JSON, or JavaScript Object Notation, is a lightweight data-interchange format that’s easy to read and write for humans, and easy to parse and generate for machines. It’s commonly used to transmit data between servers and web applications, and it's great for small databases!

#### Standard JSON Format

A JSON file stores data in key-value pairs, much like a Python dictionary. Here’s a basic structure:

```json
{
    "key": "value",
    "key2": {
        "nested_key": "nested_value"
    },
    "list_key": [1, 2, 3]
}
```

In our Hotel Accounting System, we’ll use JSON to store information like bookings, customer details, and room charges.

---

### Python's `json` Module

Python’s built-in `json` module makes it easy to read and write JSON data. Let's look at some key methods in this module:

#### `json.load()`

The `json.load()` method reads JSON data from a file and converts it into a Python object (usually a dictionary).

```python
import json

with open('data.json', 'r') as file:
    data = json.load(file)
```

#### `json.loads()`

The `json.loads()` method reads JSON data from a string and converts it into a Python object.

```python
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
```

#### `json.dump()`

The `json.dump()` method writes a Python object to a JSON file.

```python
data = {"name": "John", "age": 30}
with open('data.json', 'w') as file:
    json.dump(data, file)
```

#### `json.dumps()`

The `json.dumps()` method converts a Python object into a JSON string.

```python
data = {"name": "John", "age": 30}
json_string = json.dumps(data)
```

Now that we’re JSON ninjas, let’s put these methods to use by building a Hotel Accounting System!

---

## Step 1: Setting Up the Project

First, let’s create a basic structure for our Hotel Accounting System. We’ll need:

1. A JSON file to store hotel data (bookings, customer info, etc.).
2. Python functions to manage this data.

Create a file called `hotel_data.json`, and initialize it with an empty dictionary:

```json
{}
```

## Step 2: Defining the Hotel Accounting System Functions

Let’s define some basic functions to handle bookings, checkouts, and displaying customer info.

### 1. Adding a Booking

Let’s create a function called `add_booking()` that takes customer details and booking info, and then saves it to the JSON file.

```python
import json

def add_booking(customer_name, room_number, nights, rate_per_night):
    try:
        with open('hotel_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Calculate total charges
    total_charge = nights * rate_per_night

    # Create a booking dictionary
    booking = {
        "customer_name": customer_name,
        "room_number": room_number,
        "nights": nights,
        "rate_per_night": rate_per_night,
        "total_charge": total_charge
    }

    # Store booking data
    data[customer_name] = booking

    # Save data back to JSON file
    with open('hotel_data.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Booking added for {customer_name} in room {room_number}.")

# Example usage
add_booking(customer_name="John Doe",room_number= 101,nights= 3,rate_per_night= 100)
```

### 2. Displaying Bookings

Next, let’s create a function called `view_bookings()` to display all bookings.

```python
def view_bookings():
    try:
        with open('hotel_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    
    if not data:
        print("No bookings found.")
        return
    
    for customer, details in data.items():
        print(f"Customer: {customer}")
        for key, value in details.items():
            print(f"  {key}: {value}")
        print()  # Newline for readability

# Example usage
view_bookings()
```

### 3. Checking Out a Customer

Now, let’s create a `checkout()` function that removes a customer’s booking from the JSON file.

```python
def checkout(customer_name):
    try:
        with open('hotel_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No bookings found.")
        return

    if customer_name in data:
        del data[customer_name]
        with open('hotel_data.json', 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Checked out {customer_name}.")
    else:
        print(f"No booking found for {customer_name}.")

# Example usage
checkout("John Doe")
```

### 4. Calculating Total Revenue

Finally, let’s create a `calculate_revenue()` function to sum up the charges from all bookings.

```python
def calculate_revenue():
    try:
        with open('hotel_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    total_revenue = sum(booking["total_charge"] for booking in data.values())
    print(f"Total Revenue: ${total_revenue}")

# Example usage
calculate_revenue()
```

---

## Wrapping Up
Absolutely! Wrapping all functions in a `while` loop will make our Hotel Accounting System interactive, allowing users to choose options in a menu-like format and perform various operations repeatedly until they choose to exit. Let’s go ahead and implement this.

### Step 3: Adding a Main Menu Loop

Here, we’ll create a function called `main_menu()` that will:

1. Display a menu with available options.
2. Take user input to determine which action to perform.
3. Continue looping until the user chooses to exit.

```python
def main_menu():
    while True:
        print("\n--- Hotel Accounting System ---")
        print("1. Add Booking")
        print("2. View Bookings")
        print("3. Checkout Customer")
        print("4. Calculate Revenue")
        print("5. Exit")
        
        # Get user choice
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            customer_name = input("Enter customer name: ")
            room_number = int(input("Enter room number: "))
            nights = int(input("Enter number of nights: "))
            rate_per_night = float(input("Enter rate per night: "))
            add_booking(customer_name, room_number, nights, rate_per_night)
        
        elif choice == '2':
            view_bookings()
        
        elif choice == '3':
            customer_name = input("Enter customer name for checkout: ")
            checkout(customer_name)
        
        elif choice == '4':
            calculate_revenue()
        
        elif choice == '5':
            print("Exiting the system. Have a great day!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
```

### Explanation of the `main_menu()` Function

1. **Display Menu Options**: The function starts by printing a menu with options for the user. Each option corresponds to a specific function in the system: adding bookings, viewing bookings, checking out a customer, calculating revenue, and exiting the program.

2. **Get User Input**: The `input()` function is used to capture the user's choice. We then use an `if-elif` block to determine which action to perform based on the user's input.

3. **Execute Functions Based on User Choice**:
   - **If `1` is chosen**, it prompts for booking details and calls the `add_booking()` function.
   - **If `2` is chosen**, it calls `view_bookings()` to display all current bookings.
   - **If `3` is chosen**, it asks for the customer’s name and calls `checkout()` to remove their booking.
   - **If `4` is chosen**, it calls `calculate_revenue()` to display the total revenue from all bookings.
   - **If `5` is chosen**, the loop is broken with the `break` statement, and a farewell message is displayed.

4. **Invalid Input Handling**: If the user enters anything other than `1-5`, it displays an error message and the loop continues, allowing the user to choose a valid option.

### Running the Program

Now, you can simply call the `main_menu()` function to start the interactive Hotel Accounting System:

```python
main_menu()
```

When you run the program, you’ll see a menu. You can then enter the corresponding number for the action you want to take, and the system will respond accordingly. You can keep performing actions until you select option `5` to exit.

And there you have it! 🎉 You now have a fully interactive Hotel Accounting System using JSON as a small database. This loop provides a simple but effective way to simulate a real system, making it easy to extend with additional features in the future. Happy coding!