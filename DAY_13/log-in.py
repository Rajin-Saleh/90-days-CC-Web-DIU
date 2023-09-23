# Sample user database (replace with a database in a real application)
user_database = {
    "username1": "password1",
    "username2": "password2",
    "username3": "password3",
}

def register_user(username, password):
    # Check if the username already exists
    if username in user_database:
        print("Username already exists. Please choose a different username.")
    else:
        user_database[username] = password
        print("Registration successful!")

def login_user(username, password):
    # Check if the username exists and the password matches
    if username in user_database and user_database[username] == password:
        print("Login successful!")
    else:
        print("Login failed. Please check your username and password.")

# Example usage
while True:
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        register_user(username, password)
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login_user(username, password)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
