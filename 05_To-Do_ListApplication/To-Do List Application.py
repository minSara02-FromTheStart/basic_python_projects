import json

tasks = []
FileName = ("05_To-Do_ListApplication/To-Do_list.json")
def save_task():
    with open(FileName, "w", encoding = "utf-8") as File:
        json.dump(tasks,File,indent=4)
    print("Task saves successfully.")

def load_task():
    global tasks
    try:
        with open(FileName, "r", encoding = "utf-8") as File:
            tasks = json.load(File)
        print("Tasks Loaded Successfully.")
    except FileNotFoundError:
        tasks = []
        print("No Task Found. Start Fresh")

def add_task():
    task_description = input("Enter the description of the task: ")
    task = {
        "Task Description": task_description,
        "Complete": False
    }
    tasks.append(task)
    save_task()
    print("Task added successfully")

def view_task():
    if not tasks:
        print("No Task Yet")
        return
    for idx,task in enumerate(tasks, start = 1):
        if task["Complete"]:
            status = "Done"
        else:
            status = "Pending"
   
        print (f"{idx}.{task['Task Description']} [{status}]")
def mark_task():
    if not tasks:
        print("No task yet.")
        return
    view_task()
    try:
        task_no = int(input("Enter the task number you want to mark as complete: "))
        if 1<=task_no<=len(tasks):
            tasks[task_no - 1]["Complete"] = True
            save_task()
            print("Task marked as completed")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    if not tasks:
        print("no task yet.")
        return
    view_task()

    try:
        delete_no = int(input("Enter the task number you want to delete: "))
        if 1<= delete_no <= len(tasks):
            deleted = tasks.pop(delete_no-1)
            save_task()
            print("Task deleted")
        else:
            print("Invalid Choice. Please Try again")
    except ValueError:
        print("Please enter a valid number.")

def edit_task():
    if not tasks:
        print("no task yet")
        return
    view_task()
    try:
        edit_no = int(input("enter the task you want to edit: "))
        if 1<= edit_no <= len(tasks):
            task = tasks[edit_no - 1]
            new_description = input("Enter new description(blank if you want to keep the same):  ")
            new_Complete = input("Enter complete or not(yes/No): ").strip().lower()
            if new_description:
                task["Task Description"] = new_description
            if new_Complete == "yes":
                task["Complete"] = True
            elif new_Complete == "no":
                task["Complete"] = False
            save_task()
            print("Editing Done")
        else:
            print("Invalid choice")
    except ValueError:
        print("Please Enter an Valid Choice")


def main():
    load_task()
    while True:
         print("Welcome to your To-Do List")
         print("---------------------------")

         print("1.Add Task ")

         print("2.View Tasks ")

         print("3.Mark Task as Completed ")

         print("4.Delete Task ")

         print("5.Edit Task ")

         print("6.Exit Program  ")

         print()
    
         option = (input("Please choose you desire option: "))
         if option == '1':
            add_task()
         elif option =='2':
            view_task()
         elif option == '3':
             mark_task()
         elif option == '4':
             delete_task()
         elif option == '5':
             edit_task()
         elif option == '6':
             break    
         else:
            print("Invalid Option. Please Try Again.")
main()
        