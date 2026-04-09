numbers = []
while True:
    x = input(" nhap so ( cach de huy):")
    if x == "":
       break
    numbers.append(int(x))
numbers.sort(reverse=True)
print (" 5 so lon nhat la:",numbers[:5])