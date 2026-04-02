<<<<<<< HEAD

try:
 n = int(input("Enter an integer: "))
 is_prime = True
 if n < 2: 
    is_prime = False
 else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
 if is_prime:
    print(f"{n} is a prime number")
 else:
    print(f"{n} is not a prime number")
except ValueError: 
=======

try:
 n = int(input("Enter an integer: "))
 is_prime = True
 if n < 2: 
    is_prime = False
 else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
 if is_prime:
    print(f"{n} is a prime number")
 else:
    print(f"{n} is not a prime number")
except ValueError: 
>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
    print(" Error: please enter a valid integer")