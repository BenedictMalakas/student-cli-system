
import storage
def register_users(users, valid, username, password,):
    valid = ("!", "@", "#", "$", "%", "^", "&", "*", "(",  ")")
    if username in users:
        print("username already exist!")
    else:
        has_valid = False
        for char in password:
            if char in valid:
                has_valid = True

        if has_valid and len(password) >=8:
            print("registered successfully!")
            users[username] = password
            storage.save_users(users)
        else:
            print("The password must have special characters and be at least 8 characters long")
def login(users, username="admin", password="admin!!!"):
    if username in users and password == users[username]:
       return True
    else:
       return False