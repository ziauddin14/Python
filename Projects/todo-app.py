# To-Do List App using File Handling

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print(f"✅ Task '{task}' add ho gaya!")

def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if len(tasks) == 0:
            print("📭 Koi task nahi hai!")
        else:
            print("\n📌 Tumhari To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("⚠️ Abhi tak koi task file nahi bani.")
        

def delete_task(task_number):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if task_number < 1 or task_number > len(tasks):
            print("⚠️ Invalid task number!")
            return

        del tasks[task_number - 1]

        with open("tasks.txt", "w") as file:
            file.writelines(tasks)

        print(f"✅ Task {task_number} delete ho gaya!")
    except FileNotFoundError:
        print("⚠️ Abhi tak koi task file nahi bani.")
    
def menu():
    print("\n--- To-Do List App ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
while True:
    menu()
    choice = input("Enter choice (1-4): ")

    if choice == "4":
        print("To-Do List App band ho gaya. Bye!")
        break

    if choice == "1":
        task = input("Enter task to add: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        try:
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        except ValueError:
            print("⚠️ Invalid input! Sirf number enter karo.")
    else:
        print("Invalid choice! 1 se 4 me se koi select karo.")

# To-Do List App using File Handling
# Yeh app tasks ko file me store karega aur 
# user ko add, show aur delete karne ki permission dega.