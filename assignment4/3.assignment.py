cities = []
for i in range(5):
    name = input(f"Enter the name of city {i+1}: ")
    cities.append(name)
    print("""List of cities in order:""")
    for city in cities:
        print(city)