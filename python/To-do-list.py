tasks = []
def Add():
     no_tasks = int(input("How may task you want to add: "))
     for i in range(no_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")
def view():
     print("\nTasks:")
     for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index + 1}. {task['task']} - {status}")
def task_Doneornot():
    task_index = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
    else:
                print("Invalid task number.")
def remove():
    if len(tasks) == 0:
        print("no tasks to remove")
    else:
        choice = int(input("Enter the task number to remove:"))
        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print("Task removed successfully")
        else:
            print("Invalid task number")
def main():
    while True:
        print("\n ********* To-Do-List ********")
        print("1. Add task")
        print("2. view task")
        print("3. Remvo task")
        print("4. Mark Task as Done")
        print("5. Quit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            Add()
        elif choice == 2:
            view()
        elif choice == 3:
            remove()
        elif choice == 4:
            task_Doneornot()
        elif choice == 5:
            print("you are exited the To-Do-List")
            break
        else:
            print("Invalid choice. please try again.")
if __name__ == "__main__":
    main()
    
