import os
from datetime import datetime

FILE = "tasks.txt"
tasks = []

def load():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                p = line.strip().split("|")
                if len(p) == 5:
                    tasks.append({
                        "id": p[0], "title": p[1], "priority": p[2],
                        "due": p[3], "status": p[4]
                    })

def save():
    with open(FILE, "w") as f:
        for t in tasks:
            f.write("|".join([t["id"], t["title"], t["priority"],
                              t["due"], t["status"]]) + "\n")

def add():
    title = input("Title: ")
    priority = input("Priority: ").capitalize()

    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority. Enter High, Medium or Low.")
        return

    due = input("Due (YYYY-MM-DD): ")

    try:
        datetime.strptime(due, "%Y-%m-%d")
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return

    num = 101 + len(tasks)
    tasks.append({
        "id": "T" + str(num),
        "title": title,
        "priority": priority,
        "due": due,
        "status": "Pending"
    })
    save()
    print("Task added.")

def view():
    order = {"High": 1, "Medium": 2, "Low": 3}
    for t in sorted(tasks, key=lambda x: order[x["priority"]]):
        print(t["id"], "|", t["title"], "|", t["priority"], "|", t["due"])

def pending():
    p = [t for t in tasks if t["status"] == "Pending"]
    if not p:
        print("No pending tasks. You are all caught up!")
    else:
        for t in p:
            print(t["id"], "|", t["title"], "|", t["priority"], "|", t["due"])

def complete():
    tid = input("Task ID: ")
    for t in tasks:
        if t["id"] == tid:
            t["status"] = "Done"
            save()
            print("Task", tid, "marked as done.")
            print("Pending tasks:", sum(x["status"] == "Pending" for x in tasks))
            return
    print("Task", tid, "not found.")

load()

while True:
    print("\n1. Add  2. View by priority  3. Show pending  4. Complete  5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        pending()
    elif choice == "4":
        complete()
    elif choice == "5":
        break
    else:
        print("Invalid option.")