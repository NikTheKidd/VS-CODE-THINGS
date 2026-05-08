import random

print("Welcome to the number guessing game!")
print("-------------------------------------")


def play(max_num, max_atmp):
    num = random.randint(1, max_num)
    atmp = 1

    while atmp <= max_atmp:
        try:
            user = int(input(f"Take your guess (1-{max_num}): "))
        except ValueError:
            print("Invalid input.")
            continue

        # optional safety check
        if user < 1 or user > max_num:
            print("Out of range!")
            continue

        if user == num:
            print("You got it!")
            return True

        elif user < num:
            print("Higher")
        else:
            print("Too high")

        atmp += 1

    print("YOU LOSE!! The number was", num)
    return False


def home():
    while True:
        difi = input("""
1) Easy (1-10, 5 attempts)
2) Medium (1-50, 7 attempts)
3) Hard (1-100, 10 attempts)
4) Exit

Enter here: """)

        if not difi.isdigit():
            print("Enter a number.")
            continue

        difi = int(difi)

        # run game based on choice
        if difi == 1:
            play(10, 5)

        elif difi == 2:
            play(50, 7)

        elif difi == 3:
            play(100, 10)

        elif difi == 4:
            print("Exiting...")
            break

        else:
            print("Invalid choice.")
            continue

        # replay control
        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Exiting...")
            break


# start the game
home()