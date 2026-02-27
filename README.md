# CODSOFT
# Task 1: Taskes: Advanced Python To-Do Application

Most beginner Python To-Do lists are simple terminal scripts that lose all their data the second you close them. **ProTasker** is different. 

Built with a focus on modern UI design and robust data persistence, ProTasker is a fully functional desktop application that utilizes a relational database to keep your tasks organized, prioritized, and securely saved.

## ✨ Key Features

* **Modern, Dark-Mode UI:** Ditched the outdated standard `tkinter` look for a sleek, responsive, and scrollable interface powered by `customtkinter`.
* **Bulletproof Data Persistence:** Tasks are not saved in a fragile text file. ProTasker uses **SQLite3** to maintain a relational database (`tasks.db`), ensuring your data is safe between sessions.
* **Priority Tagging:** Assign High, Medium, or Low priorities to tasks, complete with automatic UI color-coding for quick visual scanning.
* **Smart Sorting:** Checking off a task automatically updates the database and dynamically pushes completed items to the bottom of your list, keeping your active tasks front and center.
* **Clean Architecture:** Built using object-oriented principles, strictly separating the database management logic (`DatabaseHelper`) from the UI logic (`TodoApp`).

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **GUI Framework:** CustomTkinter
* **Database:** SQLite3 (Built-in standard library)

# Task 2: The Pure-Python Calculator

A robust, lightweight command-line calculator built entirely with pure Python. This project demonstrates clean architecture, functional programming concepts, and defensive programming by handling user errors gracefully without relying on any external libraries.

## ✨ Features

* **Zero Dependencies:** Built using 100% pure Python. No `math`, `operator`, or third-party libraries required.
* **Functional Dispatch Table:** Uses a dictionary to map operator symbols (`+`, `-`, `*`, `/`) directly to functions, eliminating the need for long, messy `if/elif/else` statements.
* **Robust Error Handling:** * Catches `ValueError` via a dedicated helper function to ensure only valid numbers are processed.
  * Explicitly handles `ZeroDivisionError` to prevent the program from crashing if a user tries to divide by zero.
* **Smart Number Formatting:** Automatically formats the output to display as an integer if there are no decimals (e.g., shows `5` instead of `5.0`), keeping the interface clean.
* **DRY Principle:** Encapsulates the `try-except` input loop within a reusable `get_valid_float()` function to keep the main execution loop clean and readable.

## 🛠️ Code Structure

The code is organized into three distinct logical layers:

1. **Math Operations:** Standalone functions (`add`, `subtract`, `multiply`, `divide`) that handle the core arithmetic.
2. **Input Validation:** The `get_valid_float` function continuously prompts the user until valid numerical data is entered.
3. **Execution Loop:** The `main` function utilizes a dictionary (`operations`) to instantly execute the chosen mathematical operation in $O(1)$ lookup time.

## 🚀 How to Run

1. Ensure you have Python installed on your system.
2. Save the code to a file named `calculator.py`.
3. Open your terminal or command prompt.
4. Navigate to the folder containing the file.
5. Run the script using the following command:



# Task 3: Custom Complexity Password Generator

A sleek, lightweight, and crash-proof Python command-line utility for generating passwords on the fly. 

Unlike basic password generators that leave character selection entirely to chance, this tool uses smart logic to **mathematically guarantee** that your required character types are included in the final password.

## ✨ Features

* **Zero Dependencies:** Written entirely in pure Python using built-in standard libraries (`random`, `string`). No `pip install` required—just download and run.
* **Smart Character Guarantees:** If you ask for letters, numbers, and symbols, the script physically ensures at least one of each is included before filling the rest randomly.
* **Foolproof Input Handling:** Built-in `try-except` loops mean the program won't crash if you accidentally type letters instead of numbers. It will gently prompt you to try again.
* **Edge-Case Ready:** Handles extremely short passwords, long passwords, and even gracefully handles a requested length of `0`.
* **Pattern Obfuscation:** The final password list is shuffled before being displayed, ensuring that attackers cannot guess the order of the guaranteed character types.

## 🚀 How to Run

Since it requires no external modules, running the script is incredibly simple.

1. Make sure you have Python installed on your system.
2. Open your terminal or command prompt.
3. Navigate to the folder where the script is saved.
4. Run the following command:

```bash


## 👨‍💻 Author

**Krushnal Patil**
*AIML Student & Python Enthusiast*

---
