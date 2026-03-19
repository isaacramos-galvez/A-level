import sqlite3 as sql
from datetime import datetime as time

connection = sql.connect('Task List Data Base.db')

# A list of Tasks with the next task to complete at the end.
query_start = """
Select *
from Tasks
"""
task_list = [query_start]
print(task_list)
cursor = connection.cursor()
cursor.execute(query_start)
for row in cursor:
    print(f'{row[0]}')

def remove_completed_tasks():
    warning = input("Warning this is permanent are you sure you want to do this?")
    if warning == "yes":
        query = """delete from Tasks
        where completed = 1"""
        return query
    else: pass


# Add a new task to the front of the list
def add_task():
    task_description = input("Describe the task")
    task_completed = input("Is the task completed? 0 for no 1 for yes")
    task_due_date = input("When is the task due?")
    query = """Insert Into Tasks(description, completed, DueDate)
    Values (task_description, task_completed, task_due_date)"""
    return query

def display_next_due_task():
    query = """select Tasks.DueDate"""
    today = time.today()
    task_due = time.tasksDueDate()
    due_date_str = task_due.strftime("%y-%m-%d %h:%m:%s")
    current_time

def edit_existing_task():
    what_change = input("What do you want to change?")
    if what_change == "Name":
        change = input("What do you want to change it to?")
        query = """update Tasks
        set name = 'change'"""
        return query
    elif what_change == "Description":
        change = input("What do you want to change it to?")
        query = """update Tasks
        set Description = 'change'"""
        return query


 
# Display the last task in the list
def display_top_task():
    query = """Select * 
    from Tasks    
    where task ID = 0"""
    return query

# Display the top task and then remove it from the end of the list
def complete_top_task():
    query = """ update Tasks
    set Completed = 1 
    where taskID = 0"""
    return query

# Display a menu of options and collect the users choice
def menu():
    print("""
    1. Add a task
    2. Display all Tasks
    3. Display the next task
    4. Complete the next task
    5. Quit
    """)
    user_input = input("What would you like to do? ")
    if user_input == '1':
        # Add a task
        add_task()
    elif user_input == '2':
        # Display all Tasks

    elif user_input == '3':
        # Display the next task
        display_top_task()
    elif user_input == '4':
        # Complete the next task
        complete_top_task()
    elif user_input == '5':
        # Quit
        return False
    return True

running = True
while running:
    running = menu()