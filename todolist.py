tasks = {}

def add_tasks(task_names):
    for task_name in task_names:
        tasks[task_name] = 'pending'
        print(f'Task "{task_name}" added successfully.')

def complete_task(task_name):
    if task_name in tasks:
        tasks[task_name] = 'completed'
        print(f'Task "{task_name}" marked as completed.')
    else:
        print(f'Task "{task_name}" not found.')

def remove_task(task_name):
    if task_name in tasks:
        del tasks[task_name]
        print(f'Task "{task_name}" removed successfully.')
    else:
        print(f'Task "{task_name}" not found.')

def display_tasks():
    print("\nTasks:")
    for task, status in tasks.items():
        print(f'{task}: {status}')

while True:
    print("\nOptions:")
    print("1. Add Tasks")
    print("2. Complete Task")
    print("3. Remove Task")
    print("4. Display Tasks")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task_names_input = input("Enter task names separated by commas: ")
        task_names = [name.strip() for name in task_names_input.split(',')]
        add_tasks(task_names)
    elif choice == '2':
        task_name = input("Enter the task name to mark as completed: ")
        complete_task(task_name)
    elif choice == '3':
        task_name = input("Enter the task name to remove: ")
        remove_task(task_name)
    elif choice == '4':
        display_tasks()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
