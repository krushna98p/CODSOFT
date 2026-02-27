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
