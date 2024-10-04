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

def calculate_revenue():
    try:
        with open('hotel_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    total_revenue = sum(booking["total_charge"] for booking in data.values())
    print(f"Total Revenue: ${total_revenue}")

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


main_menu()