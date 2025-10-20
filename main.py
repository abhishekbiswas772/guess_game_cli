import random
from enum import Enum
import time

class GameDifficulty(Enum):
    EASY = 10
    MEDIUM = 5
    HARD = 3

high_scores = {
    "Easy": {"attempts": float('inf'), "time": float('inf')},
    "Medium": {"attempts": float('inf'), "time": float('inf')},
    "Hard": {"attempts": float('inf'), "time": float('inf')}
}

def get_difficulty_name(attempts):
    if attempts == GameDifficulty.EASY.value:
        return "Easy"
    elif attempts == GameDifficulty.MEDIUM.value:
        return "Medium"
    else:
        return "Hard"

def display_high_scores():
    print("\n" + "=" * 100)
    print("HIGH SCORES")
    print("=" * 100)
    for difficulty, scores in high_scores.items():
        if scores["attempts"] != float('inf'):
            print(f"{difficulty}: {scores['attempts']} attempts in {scores['time']:.2f} seconds")
        else:
            print(f"{difficulty}: No games played yet")
    print("=" * 100 + "\n")

def play_game():
    print("*" * 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("\n")
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): ").strip())
            if choice == 1:
                attempts = GameDifficulty.EASY.value
                difficulty_name = "Easy"
                break
            elif choice == 2:
                attempts = GameDifficulty.MEDIUM.value
                difficulty_name = "Medium"
                break
            elif choice == 3:
                attempts = GameDifficulty.HARD.value
                difficulty_name = "Hard"
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    max_attempts = attempts
    print(f"\nGreat! You have selected the {difficulty_name} difficulty level.")
    print(f"You have {attempts} chances to guess the correct number.")
    print("Let's start the game!")
    print("*" * 100)
    print("\n")

    number_to_guess = random.randint(1, 100)
    game_start_time = time.time()

    while attempts > 0:
        try:
            input_expected_num = int(input("Enter your guess: ").strip())

            if input_expected_num < 1 or input_expected_num > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if number_to_guess == input_expected_num:
                total_time = time.time() - game_start_time
                attempts_used = max_attempts - attempts + 1

                print(f"\n🎉 Congratulations! You guessed the correct number in {attempts_used} attempts.")
                print(f"⏱️  Total time: {total_time:.2f} seconds")

                if (attempts_used < high_scores[difficulty_name]["attempts"] or
                    (attempts_used == high_scores[difficulty_name]["attempts"] and
                     total_time < high_scores[difficulty_name]["time"])):
                    high_scores[difficulty_name]["attempts"] = attempts_used
                    high_scores[difficulty_name]["time"] = total_time
                    print(f"🏆 NEW HIGH SCORE for {difficulty_name} difficulty!")

                return True
            else:
                attempts -= 1
                difference = abs(input_expected_num - number_to_guess)

                if input_expected_num < number_to_guess:
                    print(f"❌ Incorrect! The number is greater than {input_expected_num}.", end=" ")
                else:
                    print(f"❌ Incorrect! The number is less than {input_expected_num}.", end=" ")

                # Hint system
                if difference <= 5:
                    print("🔥 You're very close!")
                elif difference <= 10:
                    print("🌡️  You're getting warmer!")
                elif difference <= 20:
                    print("❄️  You're getting colder!")
                else:
                    print("🧊 You're very far!")

                if attempts > 0:
                    print(f"You have {attempts} attempt{'s' if attempts != 1 else ''} left.\n")
                else:
                    total_time = time.time() - game_start_time
                    print(f"\n😢 Out of attempts! The correct number was {number_to_guess}.")
                    print(f"⏱️  Total time: {total_time:.2f} seconds")
                    return False

        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

def main():
    print("\n🎮 WELCOME TO THE NUMBER GUESSING GAME! 🎮\n")

    while True:
        play_game()
        display_high_scores()

        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\n" + "=" * 100)
            print("Thanks for playing! Final High Scores:")
            print("=" * 100)
            for difficulty, scores in high_scores.items():
                if scores["attempts"] != float('inf'):
                    print(f"{difficulty}: {scores['attempts']} attempts in {scores['time']:.2f} seconds")
            print("=" * 100)
            print("Goodbye! 👋\n")
            break
        print("\n")

if __name__ == "__main__":
    main()
