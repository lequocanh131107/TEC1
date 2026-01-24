cabinclass =input("Enter your cabin class: ")
if cabinclass == "LUX":
    print("upper-deck cabin with a balcony")
elif cabinclass == "A":
    print("above the car seck, equipped with a window")
elif cabinclass == "B":
    print("windowless cabin above the car deck")
elif cabinclass == "C":
    print("windowless cabin below the car deck")
else:
    print("invalid cabin class")