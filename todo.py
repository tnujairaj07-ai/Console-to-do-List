def show_menu():
    print("\n---------- To-Do List Menu ----------")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in your list.")
    else:
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f'Task "{task}" added!')

def remove_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to remove: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            print(f'Task "{removed}" removed!')
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
