import json

contacts = []
Filename = "04_Contact_Book/contact.json"

def save_contact():
    
    with open(Filename, "w", encoding = "utf-8") as file:
        json.dump(contacts,file,indent = 4)
    print("Saving Contact is Successfull!")

def load_Contact():
    global contacts
    try:
        with open(Filename, "r", encoding = "utf-8") as file:
            
             contacts = json.load(file)
             print("Contacts have been loaded from the file successfully!")
             return contacts
        
    except FileNotFoundError:
        print("File Not found. Please try again.")
        contacts = []
    except json.JSONDecodeError:
        print("File is not Valid")
        contacts = []
    
def Add_NewContact():
    contact = {}
    contact['id'] = input("Enter Id: ")
    contact['name'] = input("Enter Name: ")
    contact['phone'] = input("Enter Phone Number: ")
    contact['email'] = input("Enter Email Address: ")

    contacts.append(contact)
  
    print("Contact Added Succesfully!!")
    save_contact()

def View_Contacts():

    if not contacts:
        print("No contact found.")
        return
    print("All the Exiting Contacts are below: ")
    for contact in contacts:
        print(f"ID: {contact['id']},Name: {contact['name']}, Number: {contact['phone']}, Email: {contact['email']}")
       
def Search_Contact():
    search_id = input("Enter ID to search: ")

    if not contacts:
        print("No contact found")
        return
    
    for contact in contacts:
        if contact['id'] == search_id:
            print("Contact found: ")
            print(f"ID: {contact['id']},Name: {contact['name']}, Number: {contact['phone']}, Email: {contact['email']}")
            return

    print("ID not found")

def delete_contact():
    delete_id = input("Enter the ID you want to delete.")

    if not contacts:
        print("No contact yet")
        return
    for contact in contacts:
        if contact['id'] == delete_id:
            contacts.remove(contact)
            save_contact()
            print("Deleting is  Successful")
            return 
    print("contact is not found")

def update_contact():
    
    if not contacts:
        print("No contact found.")
        return

    update_id = input("Enter ID to update: ")

    for contact in contacts:
        if contact['id'] == update_id:
            print("Leave blank to keep existing value.")
            new_name =input("enter new name: ")
            new_phone =input("enter new_phone: ")
            new_email = input("enter new_email: ")
            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            save_contact()
            print("Contact updated successfully!")
            return

    print("ID not found. No contact updated.")


def main():
    
    while True:
        print("Welcome to the Contact Book")
        print("_______________________________")
        print("1.Load Previous Contacts")
        print("2.Add New Contact")
        print("3.View All Contacts")
        print("4.Search Contact")
        print("5.Update Contact")
        print("6.Delete Contact")
        print("7.Exit")
        print()
        option = input("Press the option you want to work on: ")
        if option == '1':
            load_Contact()
        elif option == '2':
            Add_NewContact()
        elif option == '3':
            View_Contacts()
        elif option == '4':
            Search_Contact()
        elif option =='5':
            update_contact()
        elif option == '6':
            delete_contact()
        elif option == '7':
            print("Existing succesfully from the contact book")            
            break
        else:
            print("Invalid choice. Please try again")
main()

