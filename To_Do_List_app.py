#TASKI: TO-DO LIST APPLICATION

import os
from datetime import datetime

# File to store tasks
FILE_NAME = 'tasks.txt'

# Load tasks from file if it exists
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                description, priority, due_date, completed = line.strip().split('|')
                tasks.append({
                    'description': description,
                    'priority': priority,
                    'due_date': due_date,
                    'completed': completed == 'True'
                })
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        for task in tasks:
            line = f"{task['description']}|{task['priority']}|{task['due_date']}|{task['completed']}\n"
            file.write(line)

# Load existing tasks
tasks = load_tasks()

def add_task(description, priority, due_date):
    task = {
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)

def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    else:
        print("Invalid task number")

def mark_task_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
    else:
        print("Invalid task number")

def list_tasks():
    for i, task in enumerate(tasks):
        status = 'Completed' if task['completed'] else 'Pending'
        print(f"{i+1}. {task['description']} - Priority: {task['priority']} - Due: {task['due_date']} - Status: {status}")

def main():
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (high, medium, low): ").lower()
            due_date = input("Enter due date (DD-MM-YYYY): ")
            try:
                datetime.strptime(due_date, '%d-%m-%Y')  # Validate date format
                add_task(description, priority, due_date)
                save_tasks(tasks)
            except ValueError:
                print("Invalid date format. Please enter date in DD-MM-YYYY format.")

        elif choice == '2':
            index = int(input("Enter task number to remove: ")) - 1
            remove_task(index)
            save_tasks(tasks)

        elif choice == '3':
            index = int(input("Enter task number to mark as completed: ")) - 1
            mark_task_completed(index)
            save_tasks(tasks)

        elif choice == '4':
            list_tasks()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

