season = ("spring","summer", "autumn", "winter")
month = int(input("nhap cac thang 1 - 12:"))
if month == 12 or month <= 2:
    print ("dong")
elif month < 5:
    print("xuan")
elif month < 8:
    print ("ha")
else:
    print ("thu")

