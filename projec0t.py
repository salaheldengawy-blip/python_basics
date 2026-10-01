tasks = []
def add_task():
    try:
        name_task=input ("enter the name of the task : ")
        if name_task=="":
            print("task name cannot be empty")
        else:
            new_task={"name":name_task,"status":"pending"}
            tasks.append(new_task)
            print("Task added successfully")
            return
    except Exception as e:
        print("An error occurred while adding the task:")
def show_tasks():
    if len (tasks) ==0:
        print("task not found")
    else:
        for i,task in enumerate(tasks,start=1):
            print(f"{i}-{task['name']}: {task['status'] }")
        return
def search_task():
    task_name=input("enter the task name to search: ")
    for task in tasks:
        if task["name"]==task_name:
            print(f"task found {task['name']}:{task['status']}")
            return
    print("task not found")
def mark_task_done():
    task_name=input("enter the task name to mark as done: ")
    for task in tasks:
        if task["name"]==task_name:
            task ['status']="done"
            print(f"task {task['name']} :{task['status']} ")
            return
    print("task not found")
           
def remove_task():
    task_name=input("enter the task name to remove: ")
    for task in tasks:
        if task['name']==task_name:
            tasks.remove(task)
            print(f"task {task['name']} removed successfully")
            return
    print("task not found")
            
while True:
    print("==== TO-DO LIST ====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Search Task")
    print("4. Mark Task as Done")
    print("5. Remove Task")
    print("6. Exit")
    choice=input("choose an option: ")

    if choice=="1":
        add_task() 
    elif choice=="2":
        show_tasks()
    elif choice=="3":
        search_task()
    elif choice=="4":
        mark_task_done()
    elif choice=="5":
        remove_task()
    elif choice=="6":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice , Please try again.")
