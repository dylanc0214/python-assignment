# Main menu
# Users need to choose the option (Admin, Student, Teacher, Staff)
def main_menu():
    # Can always ask the users
    while True:

        # Show the Options
        print("-----Welcome-----")
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
            # Enter Login Page First
            teacher_login()
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
# Student Menu
def student_menu():
    print("-----Student Menu-----")

# Teacher Login
# Teacher must login with their ID and Password
def teacher_login():
    print("-----Teacher Login-----")
    # ID and Password
    teacher_id = input("Enter your Teacher ID: ").lower()
    password = input("Enter your Password: ")

    if teacher_id == "alan" and password == "A1an":
        print("Login successful!")

        # If all correct, then will enter Teacher Menu
        teacher_menu(teacher_id)
    else:
        print("Invalid Teacher ID or Password. Please try again.")

# Teacher Menu
def teacher_menu(teacher_id):
    while True:
        # Print out the Teacher Menu with ID
        print(f"-----Teacher Menu (ID: {teacher_id})-----")
        print("1. Course Management")
        print("2. Enroll or Remove Students")
        print("3. Record Grades and Feedback")
        print("4. Track Attendance")
        print("5. Generate Reports")
        print("6. Back to Main Menu")

        # Teacher must enter their choice
        choice = int(input("Enter your choice: "))

        # Course Management
        if choice == 1:
            course_management()
        # Student Enrolment
        elif choice == 2:
            student_enrolment()
        # Grading and Assessment
        elif choice == 3:
            grade_assessment()
        # Attendance Tracking
        elif choice == 4:
            attendance_tracking()
        # Report Generation
        elif choice == 5:
            report_generation()
        # Back to Menu
        elif choice == 6:
            main_menu()
        # If users type other than 1, 2, 3, 4, 5, 6 then will proceed this
        else:
            print("Invalid choice")

# Course Management Menu
def course_management():
    # Print out the Course Management Menu
    print("-----Course Management Menu-----")
    print("1. Create a New Course")
    print("2. Update an Existing Course")
    print("3. Delete a Course")
    print("4. View All Courses")
    print("5. Back to Main Menu")

    # Enter the choice
    choice = int(input("Enter your choice: "))

    # Create Course
    if choice == 1:
        course_name = input("Enter Course Name: ")
        course_id = input("Enter Course ID: ")
        instructor = input("Enter Instructor Name: ")

        # ChatGPT (Investigate Later On
        # with open("courses.txt", "a") as file:
        #     file.write(f"{course_id},{course_name},{instructor}\n")
        # print("Course created successfully.")
    elif choice == 2:
        course_id = input("Enter Course ID: ")
        updated_name = input("Enter Updated Name: ")
        updated_instructor = input("Enter Updated Instructor Name: ")
        # ChatGPT (Investigate Later On)
        # with open("courses.txt", "r") as file:
        #     lines = file.readlines()
        # with open("courses.txt", "w") as file:
        #     for line in lines:
        #         if line.startswith(course_id + ","):
        #             file.write(f"{course_id},{updated_name},{updated_instructor}\n")
        #         else:
        #             file.write(line)
        # print("Course updated successfully.")
        return True

    elif choice == 5:
        main_menu()
    else:
        print("Invalid choice")
# Student Enrolment Menu
def student_enrolment():
    print("-----Student Enrolment Menu-----")
    print("1. Enrol a student")
    print("2. Remove a student")
    print("3. Back to Main Menu")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")

        # ChatGPT (Investigate Later On)
        # with open("enrollments.txt", "a") as file:
        #     file.write(f"{student_id},{course_id}\n")
        # print("Student enrolled successfully.")
        return True

    elif chocie == 2:
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")

        # ChatGPT (Investigate Later On)
        # with open("enrollments.txt", "r") as file:
        #     lines = file.readlines()
        # with open("enrollments.txt", "w") as file:
        #     for line in lines:
        #         if line.strip() != f"{student_id},{course_id}":
        #             file.write(line)
        # print("Student removed successfully.")
        return True

    elif choice == 3:
        main_menu()
    else:
        print("Invalid choice")
# Grading and Assessment
def grade_assessment():
    print("-----Grade Assessment Menu-----")
    print("1. Grade a student")
    print("2. Back to Main Menu")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        grade = input("Enter grade: ")

        # ChatGPT (Investigate Later On)
        # with open("grades.txt", "a") as file:
        #     file.write(f"{student_id},{course_id},{grade}\n")
        # print("Grades recorded successfully.")
        return True

    elif choice == 2:
        main_menu()
    else:
        print("Invalid choice")
# Attendance Tracking
def attendance_tracking():
    print("-----Attendance Tracking Menu-----")
# Report Generation
def report_generation():
    print("-----Report Generation Menu-----")

# Staff Menu
def staff_menu():
    print("-----Staff Menu-----")
# Admin Menu
def admin_menu():
    print("-----Admin Menu-----")

# Start the program
main_menu()