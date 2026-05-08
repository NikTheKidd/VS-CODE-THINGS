import random
import sys

print("Welcome to the Number Guessing Game!")
print("------------------------------------")


def play_game(max_num, attempts, difficulty):

    number = random.randint(1, max_num)
    current_attempt = 1

    print(f"\nYou chose {difficulty} mode.")
    print(f"You have {attempts} attempts.")
    print(f"(Debug Number: {number})")  # remove later if you want

    while current_attempt <= attempts:

        try:
            guess = int(input(f"\nAttempt {current_attempt}/{attempts}"
                              f" - Guess a number (1-{max_num}): "))

        except ValueError:
            print("Bro typed something that isn't even a number.")
            print("Game over.")
            sys.exit()

        if guess < 1 or guess > max_num:
            print("That number isn't even in the range.")
            print("Congratulations, you played yourself.")
            sys.exit()

        if guess == number:
            print("YOU GOT IT!")
            return

        elif guess < number:
            print("Too low. Go higher.")

        else:
            print("Too high. Chill out.")

        current_attempt += 1

    print("\nYOU LOST.")
    print(f"The number was {number}.")


while True:

    try:
        choice = int(input("""
Choose a difficulty:

1) Easy   (1-10, 5 attempts)
2) Medium (1-50, 7 attempts)
3) Hard   (1-100, 10 attempts)
4) Exit

Enter here: """))

    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        play_game(10, 5, "Easy")

    elif choice == 2:
        play_game(50, 7, "Medium")

    elif choice == 3:
        play_game(100, 10, "Hard")

    elif choice == 4:
        print("Exiting game...")
        break

    else:
        print("Invalid option.")
        continue

    again = input("\nPlay again? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thanks for playing.")
        break
