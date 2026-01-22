print("Welcome to Adventure Game!")

# Start
player_name = input("Enter Your Name: ")
health = 100

print(f"\nHello Knight {player_name}! Welcome to The Village.")
print("Your journey to the castle now begins!\n")

# Location 1: Village
location = "Village"

while True:
    print(f"You are at the {location}.")
    print("Paths available: Left (L), Straight (S), Right (R)")
    choice = input("Which path will you choose?: ").lower()

    if choice == 'r':
        print("You took the correct path! You entered the Mountain.\n")
        location = "Mountain"
        break  # Move to next location
    elif choice == 'l':
        print("Oh no! You fell into a swamp. You lose 30 health.\n")
        health -= 30
    elif choice == 's':
        print("Oh no! You fell into a river. You lose 20 health.\n")
        health -= 20
    else:
        print("Invalid choice! You hesitate and lose 10 health.\n")
        health -= 10

    if health <= 0:
        print("Your health dropped to zero. Game over!")
        exit()
    print(f"Current health: {health}\n")

# Location 2: Forest
print("In the forest, a wild bear appears!")

while True:
    action = input("Do you want to FIGHT or RUN? ").lower()
    if action == "fight":
        print("\nYou fight the bear and lose 30 health.")
        health -= 30
        if health <= 0:
            print("\nYou have died fighting the bear. Game over!")
            exit()
        print(f"Current health: {health}")
        print("You defeated the bear and continue your journey.\n")
        break
    elif action == "run":
        print("\nYou ran away and got lost. You return to the forest entrance.\n")
        continue
    else:
        print("Invalid choice. Type FIGHT or RUN.")

#Location 3: Mountain Paths to Castle
location = "Mountain"

while True:
    print(f"You are on the {location}. The castle is ahead!")
    print("Paths available: Left (L), Right (R), Straight (S)")
    choice = input("Which path do you choose?: ").lower()

    if choice == "s":
        print(f"\nCongratulations {player_name}! You reached the castle safely!")
        print(f"Your remaining health: {health}")
        break
    elif choice == "l":
        print("\nA cliff blocks your way. You lose 30 health.\n")
        health -= 30
    elif choice == "r":
        print("\nBees attack you! You lose 20 health.\n")
        health -= 20
    else:
        print("\nInvalid choice! You hesitate and lose 10 health.\n")
        health -= 10

    if health <= 0:
        print("\nYour health dropped to zero. Game over!")
        exit()
    print(f"Current health: {health}\n")
