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
print("Smallest number is:", smallest)