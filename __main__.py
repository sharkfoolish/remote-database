from console import Console
from student import Student


def executeCommand(cmd):
    if cmd == "1":
        print("\nAdd a new data to the student table.")
        name = input("\nPlease enter name of data: ")
        gender = input("Please enter gender of data: ")
        email = input("Please enter email of data: ")
        student.create(name, gender, email)
        print("\nSuccessfully added data to the student table.")
    elif cmd == "2":
        print("\n[Get all the data from the student table.]")
        student.search()
    elif cmd == "3":
        print("\n[Get one of data from the student table.]")
        student.retrieve(input("\nPlease enter id of data: "))
    elif cmd == "4":
        print("\nUpdate a data in the student table.")
        id = input("\nPlease enter id of data: ")
        email = input("Please enter new email of data: ")
        student.update(id, email)
        print("\nSuccessfully updated data in the student table.")
    elif cmd == "5":
        print("\nDelete a data in the student table.")
        id = input("\nPlease enter id of data: ")
        student.delete(id)
        print("\nSuccessfully delete data in the student table.")
    else:
        print("Invalid command")
    input("\nPress Enter to continue")


if __name__ == "__main__":
    student = Student()
    console = Console()
    while True:
        console.displayOptions()
        command = console.getCommand()
        if command == '6':
            print('\nBye!')
            student.connection.close()
            break
        else:
            executeCommand(command)
