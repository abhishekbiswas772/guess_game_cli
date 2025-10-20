# 🎮 Number Guessing Game (CLI)

A fun and interactive **Command-Line Number Guessing Game** built in Python!
Challenge yourself in multiple difficulty modes and set new high scores! 🏆

---

## 🚀 Features

- 🧠 **Three difficulty levels**:
  - Easy (10 chances)
  - Medium (5 chances)
  - Hard (3 chances)
- 🔥 **Dynamic hints** (Hot/Cold feedback)
- ⏱️ **Time tracking** and **attempt count**
- 🏆 **High Score System** (per difficulty)
- 🔁 **Play again** functionality with persistent scores
- 💪 **Robust error handling** for smooth gameplay

---

## 🕹️ Gameplay

1. Run the game in your terminal:
   ```bash
   python main.py
   ```

2. Choose a difficulty level (1, 2, or 3).

3. Guess the number between 1 and 100.

4. The game gives feedback like:
   - "🔥 You're very close!"
   - "🌡️ You're getting warmer!"
   - "❄️ You're getting colder!"
   - "🧊 You're very far!"

5. Try to guess the number in the fewest attempts and least time possible!

---

## 📊 High Scores

High scores are tracked for each difficulty based on:
- **Minimum number of attempts**
- **Fastest time** (used as a tiebreaker)

Example output:

```
====================================================================================================
HIGH SCORES
====================================================================================================
Easy: 4 attempts in 15.23 seconds
Medium: No games played yet
Hard: No games played yet
====================================================================================================
```

---

## 🧩 Code Structure

```
main.py
├── GameDifficulty (Enum)     # Defines difficulty levels
├── high_scores (dict)         # Stores high scores per difficulty
├── get_difficulty_name()      # Maps attempts to difficulty name
├── display_high_scores()      # Displays current high scores
├── play_game()                # Main game loop
└── main()                     # Entry point with replay functionality
```

---

## ⚙️ Requirements

- **Python 3.7+**
- No external dependencies required

---

## 🧠 Future Improvements

- 💾 Save and load high scores to a JSON file
- 🌈 Add colored CLI output with `colorama`
- 🧪 Unit tests for core logic
- 🧍‍♂️ Multi-player or leaderboard support

---

## 👨‍💻 Author

**Abhishek Biswas**
Backend Engineer | System Designer | AI Developer

---

## 📖 Inspiration

This project is inspired by [roadmap.sh](https://roadmap.sh/projects/number-guessing-game)