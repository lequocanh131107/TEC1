class Car:

    def __init__(car, biensoxe, tocdotoida):
        car.biensoxe = biensoxe
        car.max_speed = tocdotoida
        car.tocdohientai = 0
        car.khoangcachdiduoc = 0


car = Car("ABC-123", 142)

print("biensoxela:", car.biensoxe)
print("toc do toi da cua xe la:", car.max_speed)
print("toc do hien tai cua xe la:", car.tocdohientai)
print("khoang cach xe di duoc:", car.khoangcachdiduoc)