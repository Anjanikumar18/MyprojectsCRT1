def login():
 while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == password:
        print("Login successful")
        break
    else:
        print("Username and password must be same.")
