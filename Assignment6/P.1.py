numbers = []
while True:
    x = input("Enter a number (empty to quit): ")
    if x == "":
        break   
    numbers.append(int(x))
numbers.sort(reverse=True)
print("Five greatest numbers:")
print(numbers[:5])