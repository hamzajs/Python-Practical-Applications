"""
Simple database-based task manager.

This program allows a user to create, read, update, and delete tasks stored in a
SQLite database. It provides a basic command-line interface for managing user-specific
work items using a unique user ID.
"""

import sqlite3
from pathlib import Path

# Create a new task for the current user.
def add_task(user_id, crsr, conn):
    task_name = input("Enter Task Name: ")
    task_desc = input("Enter Task Description: ")
    crsr.execute("INSERT INTO Tasks VALUES (?, ?, ?)", (user_id, task_name, task_desc))
    conn.commit()

# Retrieve and display all tasks belonging to the specified user.
def read_tasks(user_id, crsr):
    crsr.execute("SELECT * FROM Tasks WHERE user_id = ?", (user_id,))
    answer = crsr.fetchall()
    for i in answer:
        print(i)

# Update an existing task name and description for the current user.
def update_task(user_id, crsr, conn):
    task_name = input("Enter Task Name you want to update: ")
    new_task_name = input("Enter NEW Task Name: ")
    new_task_desc = input("Enter NEW Task Description: ")
    crsr.execute("UPDATE Tasks SET task_name = ?, description = ? WHERE task_name = ? and user_id = ?", (new_task_name, new_task_desc, task_name, user_id))
    conn.commit()

# Delete a task for the current user by task name.
def delete_task(user_id, crsr, conn):
    task_name = input("Enter Task Name you want to delete: ")
    crsr.execute('DELETE FROM Tasks WHERE task_name = ? and user_id = ?', (task_name, user_id))
    conn.commit()

# Display the available operations to the user.
commands = """
a - Create: Add a new task.
s - Read: Show all tasks.
u - Update: Modify an existing task.
d - Delete: Remove a task.
q - Quit the app.
====*********************====
Please choose an option:
"""

# Get the user ID and the selected command from the user.
user_id = input("Please input your User ID: ").strip()

if not user_id.isdigit():
    print("Error: User ID must be a number!")
    exit()

user_id = int(user_id)

user_command = input(commands).strip().lower()

sqliteConnection = None

try:
    # Connect to the SQLite database stored on the Desktop.
    sqliteConnection = sqlite3.connect(Path.home() / Path('Desktop', 'ToDoApp.db'))
    crsr = sqliteConnection.cursor()

    # Ensure the Tasks table exists before executing database operations.
    sql_command = """CREATE TABLE if not exists Tasks( 
    user_id INTEGER, 
    task_name VARCHAR(20), 
    description TEXT(100)
    )"""

    crsr.execute(sql_command)

    # Execute the action selected by the user.
    if user_command == 'a':
        add_task(user_id, crsr, sqliteConnection)
    elif user_command == 's':
        read_tasks(user_id, crsr)
    elif user_command == 'u':
        update_task(user_id, crsr, sqliteConnection)
    elif user_command == 'd':
        delete_task(user_id, crsr, sqliteConnection)
    elif user_command == 'q':
        exit()
    else:
        print("False Command!!")

except sqlite3.Error as e:
    # Handle database connection failures gracefully.
    print(f"Error: {e}.")

finally:
    if sqliteConnection is not None:
        sqliteConnection.close()