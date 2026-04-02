<<<<<<< HEAD
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
=======
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
>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
