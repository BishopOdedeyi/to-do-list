# today i will be creating a to do list using python

# Things i will be including in the to do list
# 1. Add Task
# 2. View Task
# 3. Mark Task as completed
# 4. Remove Task
# 5. Exit App

# create a list to hold the task
task_list = []

# Add task function
def add_task():
    task_value = str(input("Enter your task : "))
    if task_value == "":
        return "Task can't be empty"
    else:
        task = "[ ] " + task_value
        task_list.append(task)

# function to view task
def view_tasks():
    id = 0
    for task in task_list:
        id += 1
        print(str(id) + ". " + task)

    id = 0

# function to mark tasj as complete
def complete_task():
    id = 0
    for task in task_list:
        id += 1
        print(str(id) + ". " + task)

    id = 0
    try:
        user_choice = int(input("Enter the id of the task you would like to complete : "))
        pr = task_list[user_choice].replace("[ ]", "[x]")
        task_list.insert(user_choice, pr)
        print("Task has been completed")
    except ValueError:
        print("The id has to be a number")

# function to remove task
def remove_task():
    id = 0
    for task in task_list:
        id += 1
        print(str(id) + ". " + task)

    id = 0
    user_choice = int(input("Enter the id of the task you would love to delete : "))
    to_be_removed = task_list[user_choice]
    task_list.remove(to_be_removed)


print("Welcome to the to-do list manager")
help_menu = '''

    1. Add Task
    2. View Task
    3. Mark Task as completed
    4. Remove Task
    5. Exit App

    '''
print(help_menu)

while True:
    choice = int(input("Please enter the no of what you would love to do : "))
    if choice == 1:
        add_task()
    elif choice ==2:
        view_tasks()
    elif choice == 3:
        complete_task()
    elif choice == 4:
        remove_task()
    elif choice == 5:
        break
    else:
        print("I said i wanted numbers not letters")
