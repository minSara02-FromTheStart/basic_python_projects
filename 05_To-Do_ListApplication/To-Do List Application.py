tasks = []
def add_task():
    task_description = input("Enter the description of the task: ")
    task = {
        "Task Description": task_description,
        "Complete": False
    }
    tasks.append(task)
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
#def save_task():




def main():
    while True:
         print("Welcome to your To-Do List")
         print("---------------------------")

         print("1.Add Task ")

         print("2.View Tasks ")

         print("3.Mark Task as Completed ")

         print("4.Delete Task ")

         print("5.Save/Load Tasks to File ")

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
         elif option == '10':
             break
         else:
            print("Invalid Option. Please Try Again.")
main()
        