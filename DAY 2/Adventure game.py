import time

# Function for introducing the game
def introduction():
    print("Welcome to Adventure Quest!")
    time.sleep(1)
    print("You find yourself in a mysterious forest.")
    time.sleep(1)
    print("Your goal is to complete quests and find your way out.")
    time.sleep(1)
    print("Let the adventure begin!\n")

# Function for the first scenario
def scenario_1():
    print("Scenario 1: The Fork in the Road")
    time.sleep(1)
    print("You come across a fork in the road.")
    time.sleep(1)
    print("Do you want to go left or right?")
    choice = input("Enter 'left' or 'right': ").lower()

    if choice == 'left':
        print("You chose to go left.")
        time.sleep(1)
        print("You find a treasure chest!")
        time.sleep(1)
        print("Congratulations, you have completed your first quest!\n")
    elif choice == 'right':
        print("You chose to go right.")
        time.sleep(1)
        print("You encounter a group of monsters!")
        time.sleep(1)
        print("You fight valiantly but are defeated.")
        time.sleep(1)
        print("Game over! Try again.\n")
    else:
        print("Invalid choice. Try again.\n")
        scenario_1()

# Function for the second scenario
def scenario_2():
    print("Scenario 2: The Enchanted Bridge")
    time.sleep(1)
    print("You arrive at an enchanted bridge.")
    time.sleep(1)
    print("You must answer a riddle to cross.")
    time.sleep(1)
    print("What has keys but can't open locks?")
    answer = input("Enter your answer: ").lower()

    if answer == 'a piano':
        print("Correct! You may cross the bridge.")
        time.sleep(1)
        print("You have completed another quest!\n")
    else:
        print("Incorrect answer. The bridge remains closed.")
        time.sleep(1)
        print("Game over! Try again.\n")

# Main game loop
def main():
    introduction()

    while True:
        print("Options:")
        print("1. Continue down the path.")
        print("2. Cross the enchanted bridge.")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            scenario_1()
        elif choice == '2':
            scenario_2()
        elif choice == '3':
            print("Thanks for playing Adventure Quest!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
