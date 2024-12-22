import json
import hashlib
import os

USER_FILE = "users.json"
TASK_FILE = "tasks.json"


def main():
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                task_manager(username)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def task_manager(username):
    while True:
        print("\nTask Manager Menu:")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark a Task as Completed")
        print("4. Delete a Task")
        print("5. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            mark_task_completed(username)
        elif choice == "4":
            delete_task(username)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def add_task(username):
    tasks = load_data(TASK_FILE)
    task_id = len(tasks) + 1
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks[task_id] = {"title": title, "description": description, "status": "Pending", "username": username}
    save_data(tasks, TASK_FILE)
    print("Task added successfully!")



def view_tasks(username):
    tasks = load_data(TASK_FILE)
    print("\nTasks:")
    for task_id, task in tasks.items():
        if task["username"] == username:
            print(f"{task_id}: {task['title']} ({task['status']})")


def mark_task_completed(username):
    tasks = load_data(TASK_FILE)
    task_id = input("Enter task ID to mark as completed: ")
    if task_id in tasks and tasks[task_id]["username"] == username:
        tasks[task_id]["status"] = "Completed"
        save_data(tasks, TASK_FILE)
        print("Task marked as completed!")
    else:
        print("Task not found or you do not have permission to modify this task.")

def delete_task(username):
    tasks = load_data(TASK_FILE)
    task_id = input("Enter task ID to delete: ")
    if task_id in tasks and tasks[task_id]["username"] == username:
        del tasks[task_id]
        save_data(tasks, TASK_FILE)
        print("Task deleted successfully!")
    else:
        print("Task not found or you do not have permission to delete this task.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    users = load_data(USER_FILE)
    if username in users.keys() and users[username] == hash_password(password):
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

def hash_password(password):    
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    users = load_data(USER_FILE)
    if username in users.keys():
        print("Username already exists. Please try again.")
    else:
        users[username] = hash_password(password)
        save_data(users, USER_FILE)
        print("Registration successful!")

def load_data(file_name):
    try:
        with open(file_name) as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return {}
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return {}


def save_data(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__" :
    main()