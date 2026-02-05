failed_count = 0
while True:
    username = input("Username: ")
    password = input("Password: ")

    if username == "python" and password == "rules":
        print("Login Successful!")
        break
    else:
        print("Incorrect! Please try again.")
    failed_count = failed_count + 1
    if failed_count == 5:
        print("The correct username is python and password rules.")
