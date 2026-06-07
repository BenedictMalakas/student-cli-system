
import storage
def authen():
    print("1.Register\n2.Login\n3.Exit" )

def main_menu():
    print("1. Add Student\n2. Update Student\n3. Delete Student\n4. Show Students\n5. Search Student\n6. Analysis Report\n7. Logout")
    
def validate_grade(grade):
    if grade > 100 or grade <= 0 :
       return False
    else:
         return True
    
def student_exist(students, student):
    if student in students:
        return True
    else:
        return False

def add_student(students, student, grade):
    if student_exist(students, student):
        print("Student already exist!")
    else:
        if validate_grade(grade):
            students[student]=grade
            storage.save_students(students)
            print("Student successfully added")
        else:
            print("input your real grade")
def update_student(students, users, username, password, student, grade):
    if username in users and password == users[username]:
        if student_exist(students, student):
            if validate_grade(grade):
                students[student] = grade
                storage.save_students(students)
                print("Student updated successfully!")
        else:
            print("student not found!")
    else:
        print("Incorrect credentials!")
def delete_student(students, users, student, username, password):
        if username in users and password == users[username]:
            if student_exist(students, student):
                del students[student]
                storage.save_students(students)
                print("Student deleted successfully")
            else:
                print("Student not exist!")
        else:
            print("incorrect password!")
def show_students(students):
    count = 0
    result = ""
    if students != {}:
        for student in students:
            count+=1
            result+= (f"{count}. {student} - {students[student]}\n")
        print(result)
    else:
        print("No students to show")
def search_students(students, search):
    found = False
    for student in students:
        if search == student:
            found = True

    if found:
        print(f"{search} Grade is {students[search]}")
    else:
        print("student not exist")
def analysis_report(students):
    passed = 0
    failed = 0
    if students != {}:
        for student in students:
            if students[student] >=75:
                passed+=1
            elif students[student] < 75: 
                failed+=1
        print(f"No of students that passed- {passed}\nNo of students that failed- {failed}\nStudent who got the highest grade- {max(students, key=students.get)} - {max(students.values())}\nStudent who got the lowest grade- {min(students, key=students.get)} - {min(students.values())}")          
    
    else:
        print("No student to show")
