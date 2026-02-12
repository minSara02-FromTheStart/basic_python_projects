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
#def mark_task():
#def delete_task():






def main():
    while True:
         print("Welcome to your To-Do List")
         print("---------------------------")

         print("1.Add Task ")

         print("2.View Tasks ")

         print("3.Mark Task as Completed ")

         print("4.Delete Task ")

         print("5.Load Tasks to File ")

         print("6.Priority Levels ")

         print("7.Due Date ")

         print("8.Edit Task ")

         print("9.Filter Tasks ")

         print("10.Exit Program ")
         print()
    
         option = (input("Please choose you desire option: "))
         if option == '1':
            add_task()
         elif option =='2':
            view_task()
         elif option == '5':
             load_task()
         elif option == '10':
             break
         else:
            print("Invalid Option. Please Try Again.")
main()
        