# 🎯 Hangman Game – Python

A simple **command-line Hangman Game** built using Python. The player has a limited number of chances to guess the hidden word, one letter at a time.

This project is designed as a beginner-friendly Python project to practice **loops, conditions, strings, user input, and basic game logic**.

## 📌 Features

* 🎮 Interactive command-line gameplay
* 🔤 Guess the hidden word one letter at a time
* ❤️ 5 chances to guess the word
* ✅ Displays correctly guessed letters
* ❌ Reduces chances for incorrect guesses
* 🏆 Displays a winning message when the word is completely guessed
* 💀 Displays the correct word when all chances are used

## 🛠️ Technologies Used

* **Python 3**
* Command Line / Terminal

## 📂 Project Structure

```text
hangman_game/
│
├── main.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/subamscode/hangman_game.git
```

### 2. Navigate to the project directory

```bash
cd hangman_game
```

### 3. Run the Python program

```bash
python main.py
```

## 🎮 How to Play

1. Start the game.
2. The program displays the hidden word using underscores (`_`).
3. Enter one letter as your guess.
4. If the letter exists in the word, it will be revealed.
5. If the letter is incorrect, one chance is deducted.
6. You have a maximum of **5 chances**.
7. Guess the complete word before your chances reach zero to win.

## 💻 Example

```text
Welcome to Hangman Game
You have 5 chances to guess the word

Word: ______
Guess a letter: p

Word: p_____
Guess a letter: y

Word: py____
Guess a letter: t

Word: pyt___
Guess a letter: h

Word: pyth__
Guess a letter: o

Word: pyth_o
Guess a letter: n

Word: python
You Win!
```

## 🧠 Concepts Practiced

This project demonstrates several basic Python programming concepts:

* Variables
* Strings
* `while` loops
* `for` loops
* `if-else` conditions
* User input using `input()`
* String concatenation
* Membership operators (`in`, `not in`)
* `.lower()` string method
* `break` statement

## 🔮 Future Improvements

Possible improvements for future versions:

* Add multiple words instead of a fixed word
* Select words randomly
* Add difficulty levels
* Display Hangman graphics
* Prevent repeated guesses
* Add a score system
* Add hints
* Create a graphical user interface using **Tkinter** or **Pygame**

  🎯 Learning Goal

The main goal of this project is to strengthen my Python fundamentals and problem-solving skills by building a project from scratch.

As I continue learning Python, I plan to gradually apply concepts such as functions, modules, file handling, exception handling, OOP, testing, and external libraries to make the project more complete and maintainable.

## 👨‍💻 Author

**Subham Nayak**

GitHub: [subamscode](https://github.com/subamscode)

## 📄 License

This project is created for **learning and my self practice purposes**.

