while True:
    inch = float(input(" Enter inch:"))
    if inch < 0 :
        break
    cm = inch * 2.54
    print(str(inch) + " inch is equal to " + str(cm) + " cm")
    
friends = ["Alice", "Bob", "Charlie", "David"]
print(list(range(len(friends))))