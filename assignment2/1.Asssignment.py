fishlength = float(input("Enter the length of the fish in cm: "))
fishneededlength = 42- fishlength
if fishlength < 42:
    print("The fish is too small to keep, need", fishneededlength, "cm more to keep it.")
else:
    print("The fish can be kept.")