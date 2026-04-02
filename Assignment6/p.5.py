<<<<<<< HEAD
def xoasole(numbers):
    new_list = []

    for num in numbers:
        if num % 2 == 0:    
            new_list.append(num)

    return new_list


numbers = []

print(" nhap so nguyen va khong nhap j de dung):")

while True:
    x = input("Number: ")

    if x == "":
        break

    numbers.append(int(x))


result = xoasole(numbers)

print("danh sach cu:", numbers)
=======
def xoasole(numbers):
    new_list = []

    for num in numbers:
        if num % 2 == 0:    
            new_list.append(num)

    return new_list


numbers = []

print(" nhap so nguyen va khong nhap j de dung):")

while True:
    x = input("Number: ")

    if x == "":
        break

    numbers.append(int(x))


result = xoasole(numbers)

print("danh sach cu:", numbers)
>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
print("List khong co so le:", result)