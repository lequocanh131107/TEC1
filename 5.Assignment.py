import math
pizzaDiameter1 = float(input("Enter the diameter of the first pizza in cm: "))
pizzaPrice1 = float(input("Enter the price of the first pizza: "))
pizzaDiameter2 = float(input("Enter the diameter of the second pizza in cm: "))
pizzaPrice2 = float(input("Enter the price of the second pizza: "))

Area1 = math.pi * (pizzaDiameter1 / 2) ** 2
Area2 = math.pi * (pizzaDiameter2 / 2) ** 2

ratio1 = Area1 / pizzaPrice1
ratio2 = Area2 / pizzaPrice2

if ratio1 > ratio2:
    print("The first pizza offers better deal.")
elif ratio2 > ratio1:
    print("The second pizza offers better deal.")
else:
    print("Both pizzas offer the same deal.")