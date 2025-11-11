def to_do_list():
    tasks = []

    while True:
        print("1. add task")
        print("2. remove task")
        print("3. show task")
        print("4. quit")
        choice = input("Enter your choice: ")


    if choice == "1":
        task = input("Enter your task")
        tasks.append(task)
    elif choice == "2":
        task = input("Enter task to remove task")
        if task in tasks:
            tasks.remove(task)
        else:
            print("task not found")
    elif choice == "3":
        print("tasks: ")
        for task in tasks:
            print("- " + task)
    elif choice == "4":
        brake
    else:
        print("Invalid choice")

to_do_list()