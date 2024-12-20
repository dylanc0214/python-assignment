# Main menu
# Users need to choose the option (Admin, Student, Teacher, Staff)
def main_menu():
    while True:

        # Show the Options
        print("--------------")
        print("1. Student")
        print("2. Teacher")
        print("3. Staff")
        print("4. Administrator")
        print("5. Exit")

        # Let users type the choices
        choice = int(input("Enter your choice: "))

        # Student
        if choice == 1:
            student_menu()
        # Teacher
        elif choice == 2:
            teacher_menu()
        # Staff
        elif choice == 3:
            staff_menu()
        # Admin
        elif choice == 4:
            admin_menu()
        # Exit
        elif choice == 5:
            break
        # If users type other than 1, 2, 3, 4, 5 then will proceed this
        else:
            print("Invalid choice")

def student_menu():

def teacher_menu():

def staff_menu():

def admin_menu():