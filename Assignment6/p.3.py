<<<<<<< HEAD
names = set()

while True:
    name = input("Enter a name: ")

    if name == "":
        break

    if name in names:
        print(" ten da duoc su dung")
    else:
        print(" ten duoc chap nhan")
        names.add(name)

print("\n danh sach te duoc nhap nhu sau:")

for n in names:
=======
names = set()

while True:
    name = input("Enter a name: ")

    if name == "":
        break

    if name in names:
        print(" ten da duoc su dung")
    else:
        print(" ten duoc chap nhan")
        names.add(name)

print("\n danh sach te duoc nhap nhu sau:")

for n in names:
>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
    print(n)