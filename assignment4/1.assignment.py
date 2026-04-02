<<<<<<< HEAD
numbers = []

while True:
    user_input = input("Enter a number : ")
    
    if user_input == "":
        break
    
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Only numbers.")

if len(numbers) < 5:
    print("You entered fewer than five numbers.")
else:
    numbers.sort(reverse=True)
    print("5 largest numbers are:")
    for num in numbers[:5]:
=======
numbers = []

while True:
    user_input = input("Enter a number : ")
    
    if user_input == "":
        break
    
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Only numbers.")

if len(numbers) < 5:
    print("You entered fewer than five numbers.")
else:
    numbers.sort(reverse=True)
    print("5 largest numbers are:")
    for num in numbers[:5]:
>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
        print(num)