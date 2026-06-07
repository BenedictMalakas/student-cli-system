import json
def load_users():
    try:
        with open("users.json", "r")as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def save_users(users):
    with open("users.json", "w")as file:
        json.dump(users, file)
def load_students():
    try:
        with open("students.json", "r")as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def save_students(students):
    with open("students.json", "w")as file:
        json.dump(students, file)