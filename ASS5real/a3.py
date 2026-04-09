names = set()
while True:
    name = input("nhap ten:")
    if name == "":
        break
    if name in names:
        print ("no")
    else:
        print ("ok")
        names.add(name)
    print("\n danh sach te duoc nhap nhu sau:")
    for n in names:
        print(n)
