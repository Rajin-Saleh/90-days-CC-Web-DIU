# Define an empty list to store data
data_entries = []

# Function to add data to the list
def add_entry():
    name = input("Enter a name: ")
    age = input("Enter age: ")
    data_entries.append({"Name": name, "Age": age})
    print("Entry added successfully!")

# Function to display all data entries
def display_entries():
    if not data_entries:
        print("No entries found.")
    else:
        print("Data Entries:")
        for i, entry in enumerate(data_entries, start=1):
            print(f"{i}. Name: {entry['Name']}, Age: {entry['Age']}")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add Data Entry")
    print("2. Display Data Entries")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_entry()
    elif choice == '2':
        display_entries()
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
