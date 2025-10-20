# 🎮 Number Guessing Game (CLI)

A fun and interactive **Command-Line Number Guessing Game** built in Python!  
Challenge yourself in multiple difficulty modes and set new high scores! 🏆


## 🚀 Features

- 🧠 **Three difficulty levels**:
  - Easy (10 chances)
  - Medium (5 chances)
  - Hard (3 chances)
- 🔥 **Dynamic hints** (Hot/Cold feedback)
- ⏱️ **Time tracking** and **attempt count**
- 🏆 **High Score System** (per difficulty)
- 💪 **Robust error handling** for smooth gameplay


## 🕹️ Gameplay

1. Run the game in your terminal:
   ```bash
   python main.py


Choose a difficulty level (1, 2, or 3).

Guess the number between 1 and 100.

The game gives feedback like:

"🔥 You're very close!"

"❄️ You're getting colder!"

Try to guess the number in the fewest attempts and least time possible!

📊 High Scores

High scores are tracked for each difficulty based on:

Minimum number of attempts

Fastest time (used as a tiebreaker)

Example output:

========================================
HIGH SCORES
========================================
Easy: 4 attempts in 15.23 seconds
Medium: No games played yet
Hard: No games played yet
========================================

🧩 Code Structure
guess_game.py
├── GameDifficulty (Enum)
├── high_scores (dict)
├── get_difficulty_name()
├── display_high_scores()
├── play_game()
└── main()

⚙️ Requirements

Python 3.7+

No external dependencies

(Optional for colored output):

pip install colorama

🧠 Future Improvements

💾 Save and load high scores to a JSON file

🌈 Add colored CLI output

🧪 Unit tests for core logic

🧍‍♂️ Multi-player or leaderboard support

👨‍💻 Author

Abhishek Biswas
Backend Engineer | System Designer | AI Developer


This project is inspired from this website called roadmap.sh   
`url
https://roadmap.sh/projects/number-guessing-game
`