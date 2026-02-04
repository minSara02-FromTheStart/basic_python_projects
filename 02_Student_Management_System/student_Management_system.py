
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
    print("Student added successfully!\n")

def View_students():
    if not students:
        print("No students found.\n")
        return
    print("\nList of Students:")
    for student in students:
        print(f"ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Class: {student['Class']}")
    print()



def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            Add_student()
        elif choice == '2':
            View_students()
        elif choice == '3':
            print("Exiting the Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()
        
    
