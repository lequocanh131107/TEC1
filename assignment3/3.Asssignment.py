<<<<<<< HEAD
largest = None
smallest = None
while True:
    number_choosed = input("Enter a number: ")
    if number_choosed == " ":
        break
    number = float(number_choosed)
    if largest is None or number > largest:
        largest = number
    if smallest is None or number < smallest:
        smallest = number
print("Largest number is:", largest)
=======
largest = None
smallest = None
while True:
    number_choosed = input("Enter a number: ")
    if number_choosed == " ":
        break
    number = float(number_choosed)
    if largest is None or number > largest:
        largest = number
    if smallest is None or number < smallest:
        smallest = number
print("Largest number is:", largest)
>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
print("Smallest number is:", smallest)