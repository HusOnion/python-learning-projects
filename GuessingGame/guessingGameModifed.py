import time
import random


# =========================
# INPUT HANDLING
# =========================
def get_valid_guess(min_val, max_val):
    while True:
        guess = input(f"Enter a number ({min_val}-{max_val}): ")
        if not guess.isdigit():
            print("Invalid input. Numbers only.")
            continue

        guess = int(guess)
        if guess < min_val or guess > max_val:
            print("Out of range.")
            continue

        return guess


# =========================
# CORE GAME ENGINES
# =========================
def play_unlimited_mode(max_number, intro_text):
    number = random.randint(1, max_number)
    guesses = 0

    print(intro_text)
    time.sleep(2)

    while True:
        guess = get_valid_guess(1, max_number)
        guesses += 1

        if guess == number:
            break

        print("Too high!" if guess > number else "Too low!")

    print("\n****************************************************")
    print(f"Nice! The number was {number}")
    print(f"You took {guesses} guesses")
    print("****************************************************")


def play_limited_mode(max_number, max_guesses, intro_text):
    number = random.randint(1, max_number)
    guesses = 0

    print(intro_text)
    time.sleep(2)

    while True:
        guess = get_valid_guess(1, max_number)
        guesses += 1

        if guess == number:
            print("\n****************************************************")
            print(f"You WON! The number was {number}")
            print(f"Guesses used: {guesses}")
            print("****************************************************")
            return

        print("Too high!" if guess > number else "Too low!")
        print(f"Guesses left: {max_guesses - guesses}")

        if guesses >= max_guesses:
            print("\nWomp Womp. You lost.")
            print(f"The number was {number}")
            return


def play_budget_mode(max_number, starting_balance):
    number = random.randint(1, max_number)
    balance = starting_balance
    guesses = 0
    max_guesses = 10

    print(f"\nGuess a number between 1 and {max_number}")
    print(f"You have {max_guesses} guesses and ${balance}\n")
    time.sleep(2)

    while True:
        guess = get_valid_guess(1, max_number)
        guesses += 1

        if guess == number:
            print("\n****************************************************")
            print(f"You WON! The number was {number}")
            print(f"Guesses used: {guesses}")
            print(f"Final balance: ${balance}")
            print("****************************************************")
            return

        diff = abs(guess - number)

        if diff > 100:
            penalty = 40
        elif diff > 50:
            penalty = 20
        elif diff > 20:
            penalty = 10
        elif diff > 10:
            penalty = 5
        elif diff > 3:
            penalty = 2
        else:
            penalty = 1

        balance -= penalty

        print("Too high!" if guess > number else "Too low!")
        print(f"-${penalty} | Balance: ${balance} | Guesses left: {max_guesses - guesses}")

        if balance <= 0:
            print("\nNAH YOU'RE BROKE 💀")
            print(f"The number was {number}")
            return

        if guesses >= max_guesses:
            print("\nWomp Womp. Out of guesses.")
            print(f"The number was {number}")
            return


# =========================
# MAIN MENU
# =========================
def main():
    print("************************************")
    print("Welcome to the Number Guessing Game!")
    print("************************************")

    while True:
        print("\nDifficulty levels:")
        print("1. Baby")
        print("2. Easy")
        print("3. Medium")
        print("4. Hard")
        print("5. Insane")

        choice = input("Choose (1-5): ")

        if not choice.isdigit() or not (1 <= int(choice) <= 5):
            print("Invalid choice.")
            continue

        choice = int(choice)

        if choice == 1:
            play_unlimited_mode(
                10,
                "Baby mode: Guess a number between 1 and 10. Unlimited guesses."
            )

        elif choice == 2:
            play_unlimited_mode(
                100,
                "Easy mode: Guess a number between 1 and 100. Unlimited guesses."
            )

        elif choice == 3:
            play_limited_mode(
                300,
                10,
                "Medium mode: Guess a number between 1 and 300. You have 10 guesses."
            )

        elif choice == 4:
            play_budget_mode(300, 100)

        elif choice == 5:
            play_budget_mode(500, 50)

        again = input("\nPlay again? (Y/N): ").upper()
        if again != "Y":
            print("Ok bye!")
            break


if __name__ == "__main__":
    main()
