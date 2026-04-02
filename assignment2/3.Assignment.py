<<<<<<< HEAD
biologicalsex = str(input("Enter your biological sex: "))
hemoglobinvalue = float(input("Enter your hemoglobin value in g/L: "))
if biologicalsex == "male":
    if hemoglobinvalue < 134:
        print ("the person 's hemoglobin level is low")
    elif hemoglobinvalue > 167:
        print("the person 's hemoglobin level is high")
    else:
        print("the person 's hemoglobin level is normal")
elif biologicalsex == "female":
    if hemoglobinvalue < 117:
        print ("the person 's hemoglobin level is low")
    elif hemoglobinvalue > 155:
        print("the person 's hemoglobin level is high")
    else: 
        print("the person 's hemoglobin level is normal")
else:
=======
biologicalsex = str(input("Enter your biological sex: "))
hemoglobinvalue = float(input("Enter your hemoglobin value in g/L: "))
if biologicalsex == "male":
    if hemoglobinvalue < 134:
        print ("the person 's hemoglobin level is low")
    elif hemoglobinvalue > 167:
        print("the person 's hemoglobin level is high")
    else:
        print("the person 's hemoglobin level is normal")
elif biologicalsex == "female":
    if hemoglobinvalue < 117:
        print ("the person 's hemoglobin level is low")
    elif hemoglobinvalue > 155:
        print("the person 's hemoglobin level is high")
    else: 
        print("the person 's hemoglobin level is normal")
else:
>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
    print("Invalid biological sex entered")