# Daily Task Manager

## Student Information

- **Name:** Abhishek Kumar
- **Class/Section:** B.TECH / K
- **Roll Number:** RU-26-02064

---

## 1. Project Description

The Daily Task Manager is a Python-based application developed to help users organize and manage their daily tasks.

The application provides a simple menu-driven interface that allows users to add new tasks, view tasks according to priority, display pending tasks, and mark tasks as completed.

Task information is stored in a text file (`tasks.txt`) using file handling, allowing existing tasks to be loaded when the program starts.

This project demonstrates the practical implementation of Python programming concepts and problem-solving techniques.

## 2. Project Objectives

- To develop a simple daily task management application.
- To understand and implement Python programming concepts.
- To practice file handling using text files.
- To organize tasks according to their priority.
- To track pending and completed tasks.
- To improve programming and problem-solving skills.

## 3. Features

1. **Add Task:** Allows users to add a new task with a title, priority, and due date.
2. **View Tasks by Priority:** Displays tasks in High, Medium, and Low priority order.
3. **Show Pending Tasks:** Displays all tasks that have not yet been completed.
4. **Complete Task:** Allows users to mark a task as completed using its Task ID.
5. **Automatic Task ID:** Generates a Task ID for each newly added task.
6. **Input Validation:** Checks priority values and date formats.
7. **File Handling:** Saves task information in `tasks.txt` and loads it when the program starts.
8. **Pending Task Count:** Displays the remaining number of pending tasks after completing a task.

## 4. Technologies Used

- **Programming Language:** Python 3
- **Code Editor:** Visual Studio Code
- **File Storage:** Text File (`tasks.txt`)
- **Python Modules:** `os` and `datetime`

## 5. Requirements

- Python 3.x
- Visual Studio Code or another Python-compatible editor.
- No external libraries are required. The project uses Python's built-in modules.

## 6. How to Run the Project

Follow these steps to run the project:

1. Install Python 3 on your computer.
2. Install or open Visual Studio Code.
3. Download or clone this repository.
4. Open the project folder in Visual Studio Code.
5. Make sure `DailyTask_manager.py` and `tasks.txt` are in the same folder.
6. Open the VS Code terminal.
7. Execute the following command:

```bash
python DailyTask_manager.py
```

8. Select an option from the displayed menu.
9. Follow the instructions to manage your tasks.

## 7. Application Menu

The application provides the following menu options:

```text
1. Add
2. View by priority
3. Show pending
4. Complete
5. Exit
```

## 8. Task File Format

The project stores task information in `tasks.txt`.

Each task contains five fields:

- Task ID
- Task Title
- Priority
- Due Date
- Status

The fields are separated using the pipe (`|`) symbol.

**Example:**

```text
T101|Submit report|High|2026-10-15|Done
T102| Buy milk|Low|2026-10-11|Pending
T103|Call bank|Medium|2026-10-12|Pending
```

The program loads saved tasks when it starts and updates the text file when tasks are added or completed.

## 9. Project Structure

```text
Daily-Task-Manager/
│
├── DailyTask_manager.py
├── tasks.txt
├── README.md
├── SUMMARY.md
│
└── screenshots/
    ├── Daily task  manager.png
    ├── Daily task  manager1.png
    ├── Daily task  manager2.png
    ├── Daily task  manager3.png
    ├── Daily task  manager4.png
    ├── Daily task  manager5.png
    └── Daily task  manager6.png
```

## 10. Working Test Cases / Screenshots

The following seven test cases demonstrate the working features, input validation, and output of the Daily Task Manager application.

### Test Case 1 – Invalid Date and Task ID Not Found

**Description:**

This test case demonstrates input validation when an incorrect date format is entered while adding a task. It also demonstrates the handling of a Task ID that does not exist.

**Input:**
- Priority: High
- Due date: 15-10-2026 (incorrect format)
- Task ID: T999

**Output:**
- Invalid date. Use YYYY-MM-DD.
- Task T999 not found.

**Screenshot:**

![Test Case 1](screenshots/Daily%20task%20%20manager.png)

---

### Test Case 2 – Invalid Priority and Date Validation

**Description:**

This test case demonstrates how the application rejects an invalid priority and an incorrectly formatted due date.

**Input:**
- Task title: Pay bill
- Priority: Urgent
- Due date: 15-10-2026

**Output:**
- Invalid priority. Enter High, Medium or Low.
- Invalid date. Use YYYY-MM-DD.

**Screenshot:**

![Test Case 2](screenshots/Daily%20task%20%20manager1.png)

---

### Test Case 3 – Successfully Adding a Task

**Description:**

This test case demonstrates the successful addition of a new task with its title, priority, and due date. The application automatically generates a Task ID and saves the task in the text file.

**Input:**
- Task title: Submit report
- Priority: High
- Due date: 2026-10-15

**Output:**
- Task added.

**Screenshot:**

![Test Case 3](screenshots/Daily%20task%20%20manager2.png)

---

### Test Case 4 – Viewing Tasks by Priority

**Description:**

This test case demonstrates how the application displays existing tasks according to their priority, starting with High, followed by Medium and Low. It also demonstrates the rejection of an invalid priority while adding another task.

**Input:**
- Select option 2 to view tasks by priority.
- Select option 1 to add another task.
- Enter an invalid priority: Urgent.

**Output:**
- Tasks are displayed in priority order.
- Invalid priority. Enter High, Medium or Low.

**Screenshot:**

![Test Case 4](screenshots/Daily%20task%20%20manager3.png)

---

### Test Case 5 – No Pending Tasks Available

**Description:**

This test case demonstrates the application's response when there are no pending tasks available.

**Input:**
- Select option 3 (Show pending).

**Output:**
- No pending tasks. You are all caught up!

**Screenshot:**

![Test Case 5](screenshots/Daily%20task%20%20manager4.png)

---

### Test Case 6 – Completing a Task

**Description:**

This test case demonstrates how a user can mark an existing task as completed by entering its Task ID. The application updates the task status and displays the remaining number of pending tasks.

**Input:**
- Select option 4 (Complete).
- Enter Task ID: T101.

**Output:**
- Task T101 marked as done.
- Pending tasks: 2

**Screenshot:**

![Test Case 6](screenshots/Daily%20task%20%20manager5.png)

---

### Test Case 7 – Displaying Remaining Pending Tasks

**Description:**

This test case demonstrates the completion of Task T101 followed by displaying the remaining pending tasks. It verifies that completed tasks are excluded from the pending task list.

**Input:**
- Complete Task ID: T101.
- Select option 3 (Show pending).

**Output:**
- Task T101 marked as done.
- Pending tasks: 2
- Displays the remaining pending tasks:
  - T102 – Buy milk – Low
  - T103 – Call bank – Medium

**Screenshot:**

![Test Case 7](screenshots/Daily%20task%20%20manager6.png)

---

## 11. Python Concepts Learned

The following Python concepts are demonstrated in this project:

- Variables and data types
- Lists and dictionaries
- User input and output
- Functions
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while` and `for`)
- File handling (`open`, `read`, `write`)
- Exception handling (`try` and `except`)
- Built-in modules (`os` and `datetime`)
- Sorting using `sorted()` and `lambda`
- Data validation and problem-solving

## 12. Conclusion

The Daily Task Manager project demonstrates the practical application of Python programming concepts in developing a simple task management system.

It provides useful functionality for adding tasks, viewing tasks according to priority, displaying pending tasks, and marking tasks as completed.

The project also provides practical experience with functions, conditional statements, loops, lists, dictionaries, file handling, exception handling, and input validation.

Through this project, I gained a better understanding of Python programming and learned how to develop a menu-driven application to solve a real-world problem.

---

**Project Title:** Daily Task Manager

**Submitted By:** Abhishek Kumar

**Class/Section:** B.TECH / K

**Roll Number:** RU-26-02064
