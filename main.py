import storage
import auth
import student_service
users = storage.load_users()
students = storage.load_students()
while True:
    student_service.authen()
    pick = input("Choose any number to continue: ")
    if pick == "1":
        username = input("Username: ").lower()
        password = input("Password: ")
        valid = ("!", "@", "#", "$", "%", "^", "&", "*", "(",  ")")
        auth.register_users(users, valid, username, password)
    elif pick == "2":
        username = input("Username: ").lower()
        password = input("Password: ")
        if auth.login(users, username, password):
                    print("login.....")
                    print("login successfully")

                    while True:
                        student_service.main_menu()
                        main_pick = input("Choose any number to continue: ")
                        if main_pick == "1":
                            student = input("Student: ").lower()
                            grade = int(input("Grade: "))
                            student_service.add_student(students, student, grade)
                        elif main_pick == "2":
                            student = input("Student: ").lower()
                            grade = int(input("Grade: "))
                            username = input("Username: ").lower()
                            password = input("Password: ")
                            student_service.update_student(students, users, username, password, student, grade)
                        elif main_pick == "3":
                            student = input("Student: ").lower()
                            username = input("Username: ")
                            password = input("Input your password to continue: ")
                            student_service.delete_student(students, users, student, username, password)
                        elif main_pick =="4":
                            student_service.show_students(students)
                        elif main_pick == "5":
                            search = input("Student: ").lower()
                            student_service.search_students(students, search)
                        elif main_pick == "6":
                            student_service.analysis_report(students)
                        elif main_pick == "7":
                            print("logout........")
                            break
        else:
            print("Invalid credentials")

