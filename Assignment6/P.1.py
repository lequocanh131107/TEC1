<<<<<<< HEAD
numbers = []
while True:
    x = input("Enter a number (empty to quit): ")
    if x == "":
        break   
    numbers.append(int(x))
numbers.sort(reverse=True)
print("Five greatest numbers:")
=======
numbers = []
while True:
    x = input("Enter a number (empty to quit): ")
    if x == "":
        break   
    numbers.append(int(x))
numbers.sort(reverse=True)
print("Five greatest numbers:")
>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
print(numbers[:5])