import json
print("Welcome to the Student Management System!!!")
print("--------------------------------------------")

students = []
def Add_student():
    student = {}
    student['ID'] = input("Enter Student ID: ")
    student['Name'] = input("Enter Student Name: ")
    student['Age'] = input("Enter Student Age: ")
    student['Class'] = input("Enter Student Class: ")
    students.append(student)
    print("Student added successfully!")

def View_students():
    if not students:
        print("No students found.")
        return
    print("List of Students:")
    for student in students:
        print(f"ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Class: {student['Class']}")
    
    print()

def Search_student():
    search_id = input("Enter Student ID to search: ")

    if not students:
        print("No students found.\n")
        return

    for student in students:
        if student['ID'] == search_id:
            print("\nStudent Found:")
            print(f"ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Class: {student['Class']}\n")
            return

    print("Student not found.\n")

def Update_student():
    update_id = input("Enter the Student ID you want to update: ")
    if not students:
        print("No students yet")
        return
    for student in students:
        if student['ID'] == update_id:
            print("Student found. Proceed to update: ")
            new_name = input(f"Enter new name (current: {student['Name']:}): ")
            new_age = input(f"Enter new age (current: {student['Age']}): ")
            new_class = input(f"Enter new class (current: {student['Class']}): ")

            if new_name:
                student['Name'] = new_name
            if new_age:
                student['Age'] = new_age
            if new_class:
                student['Class'] = new_class
            print("Student details has been updated successfully!")
            return
    print("Student not found.")
                         

def Delete_student():
    delete_id = input("Enter the student ID you want to delete: ")
    if not students:
        print("No Students yet.")
        return
    for student in students:
        if student['ID'] == delete_id:
            students.remove(student)
            print("Student has been deleted successfully!")
            return
    print("Student not found.")

def Save_data():
    filename = input("Enter the file name: ")
    with open(filename, 'w', encoding = "utf-8") as file:
        json.dump(students,file,indent=4)
    print("Student data has been saved to the file successfully!")

def Load_data():
    filename = input("Enter the file name to load from: ")
    try:
        with open(filename, 'r', encoding = 'utf-8') as file:
            global students
            students = json.load(file)
        print("Student data has been loaded from the file successfully!")

    except FileNotFoundError:
        print("File not found. Please try again.")
    except json.JSONDecodeError:
        print("File is not valid.")


def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save student data to a file")
        print("7.Load student data from a file")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            Add_student()
        elif choice == '2':
            View_students()
        elif choice == '3':
            Search_student()
        elif choice == '4':
            Update_student()
        elif choice == '5':
            Delete_student()
        elif choice == '6':
            Save_data()
        elif choice == '7':
            Load_data()
        elif choice == '8':
            print("Exiting the Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()
        
    
