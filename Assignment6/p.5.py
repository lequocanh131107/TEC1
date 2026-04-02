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
print("List khong co so le:", result)