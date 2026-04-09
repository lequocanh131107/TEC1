
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
    print(n)