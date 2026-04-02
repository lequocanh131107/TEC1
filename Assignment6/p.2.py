seasons = ("winter", "spring", "summer", "autumn")
month = int(input("Enter month 1-12: "))
 

if month == 12 or month <= 2:
    print("seasons winter")
elif month <= 5:
    print("seasons spring" )
elif month <= 8:
    print("seasons summer")
else:
    print("seasons autumn")