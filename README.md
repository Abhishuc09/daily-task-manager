Task Manager

Student Details

- Name: Abhishek Kumar
- Class: B.Tech CSE
- Section: K
- Roll Number: RU-26-02064

Project Description

Task Manager is a Python-based project designed to help users manage their tasks. The program allows users to add, view, update, and delete tasks. Each task contains information such as task ID, task name, priority, due date, and status.

The project demonstrates basic Python programming concepts including variables and data types, conditional statements, loops, functions, lists/dictionaries, file handling, and error handling.

Features

- Add a new task
- View existing tasks
- Update task information
- Delete tasks
- Manage task status
- Store task data in a file
- Handle invalid user input
- Display clear messages and results

Technologies Used

- Python 3
- File handling for storing task information
- No external Python libraries are required

Python Concepts Used

- Variables and data types
- Conditional statements ("if", "elif", "else")
- Loops
- Functions
- Lists and dictionaries
- File handling
- Error handling using "try" and "except"

How to Run the Project

1. Install Python 3.
2. Open the Task Manager project folder in VS Code.
3. Open the VS Code terminal.
4. Run the program:

python task_manager.py

If your system uses "python3", run:

python3 task_manager.py

5. Follow the options displayed by the program.

Sample Input and Output

Adding a Task

Input:

Enter task title: Submit report
Enter priority: High
Enter due date: 2026-10-15

Output:

Task added successfully.

Viewing Tasks

Output:

T101 | Submit report | High | 2026-10-15 | Pending

Updating a Task

Input:

Enter task ID: T101

Output:

Task updated successfully.

Deleting a Task

Input:

Enter task ID: T101

Output:

Task deleted successfully.

Screenshots

Screenshots of the working test cases are included in the "Screenshots" folder of this repository.

The screenshots demonstrate the assigned test cases and their corresponding outputs.

Project Files

Task Manager/
│
├── task_manager.py
├── tasks.txt
├── README.md
├── Summary.md
└── Screenshots/
    ├── test_case_1.png
    ├── test_case_2.png
    ├── test_case_3.png
    └── ...

Conclusion

The Task Manager project demonstrates the practical use of Python programming concepts to create a simple task management application. It provides practical experience with user input, functions, conditions, loops, file handling, and error handling while solving a real-world problem.