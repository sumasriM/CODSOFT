def add_task(tasks):
    task = input("Enter a task to add: ")
    tasks.append(task)
def update_task(tasks):
    if not tasks:
        print("No tasks to update.")
        return
    print("Current tasks:")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")
    task_index = int(input("Enter the index of the task to update: ")) - 1
    if 0 <= task_index < len(tasks):
        new_task = input("Enter the new task name: ")
        tasks[task_index] = new_task
    else:
        print("Invalid task index.")
def complete_task(tasks, completed_tasks):
    if not tasks:
        print("No tasks to complete.")
        return
    print("Current tasks:")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")
    task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        completed_task = tasks.pop(task_index)
        completed_tasks.append(completed_task)
    else:
        print("Invalid task index.")
def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    print("Current tasks:")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")
    task_index = int(input("Enter the index of the task to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    else:
        print("Invalid task index.")
def show_tasks(tasks, completed_tasks):
    print("Current tasks:")
    if tasks:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
    else:
        print("None")
    print("\nCompleted tasks:")
    if completed_tasks:
        for i in range(len(completed_tasks)):
            print(f"{i + 1}. {completed_tasks[i]}")
    else:
        print("None")
def main():
    tasks = []
    completed_tasks = []
    print("To-Do List Application")
    print("1. Add a task")
    print("2. Update a task")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Show existing tasks")
    print("6. Exit")
    while True:
        try:
            command = int(input("Enter command number: "))
            if command == 1:
                add_task(tasks)
            elif command == 2:
                update_task(tasks)
            elif command == 3:
                complete_task(tasks, completed_tasks)
            elif command == 4:
                delete_task(tasks)
            elif command == 5:
                show_tasks(tasks, completed_tasks)
            elif command == 6:
                print("Exiting the application.")
                break
            else:
                print("Invalid command number. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid command number.")
main()
