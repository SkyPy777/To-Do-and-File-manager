
my_list = []

def add_task(task):
    my_list.append(task)
    print(f"Task '{task}' added successfully.")

def view_tasks():
    if not my_list:
        print("List is empty.")
    else:
        print("\nMy_list:")
        for index, task in enumerate(my_list, start=1):
            print(f"\t{index} : {task}")

def remove_task(task_number):
    if 1 <= task_number <= len(my_list):
        removed_task = my_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed!")
    else:
        print("Enter a valid task number.")

import os

def create_file(file_name):
    file = open(file_name, 'w')
    print(f"File '{file_name}' created.")
    file.close()

def read_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"\nContents of '{file_name}':\n{content}")
    else:
        print(f"File '{file_name}' not found.")

def append_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content + '\n')
    print(f"\nContent added to '{file_name}'.")

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"\nFile '{file_name}' deleted.")
    else:
        print(f"File '{file_name}' not found.")

while True:
    print("\nWelcome to To-Do and File manager.")
    print("\nOptions:")
    print("\t1. To-Do List")
    print("\t2. File Management")
    print("\t3. Quit")

    choice = input("\nEnter your choice (1/2/3): ")

    if choice == '1':
        print("\nWelcome to the To-Do List Menu:")
        print("Select the Options given below.")
        print("Options:")
        print("\t1. Add item")
        print("\t2. View tasks")
        print("\t3. Remove a task")
        print("\t4. Back to Main Menu")
        while True:
            choice = input("\nEnter your choice (1/2/3/4): ")

            if choice == '1':
                task = input("\nEnter the task to add: ")
                add_task(task)
            elif choice == '2':
                view_tasks()
            elif choice == '3':
                task_number = int(input("\nEnter the task number to remove: "))
                remove_task(task_number)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please select a valid option.")

    elif choice == '2':
        print("\nWelcome to the File Management Menu:")
        print("Choose the options below")
        print("\nOptions:")
        print("\t1. Create File")
        print("\t2. Read File")
        print("\t3. Append to File")
        print("\t4. Delete File")
        print("\t5. Back to Main Menu")
        while True:
            sub_choice = input("\nEnter your choice (1/2/3/4/5): ")

            if sub_choice == '1':
                file_name = input("Enter the file name: ")
                create_file(file_name)
            elif sub_choice == '2':
                file_name = input("Enter the file name: ")
                read_file(file_name)
            elif sub_choice == '3':
                file_name = input("Enter the file name: ")
                content = input("Enter content to append: ")
                append_file(file_name, content)
            elif sub_choice == '4':
                file_name = input("Enter the file name: ")
                delete_file(file_name)
            elif sub_choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == '3':
        print("\nGoodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
