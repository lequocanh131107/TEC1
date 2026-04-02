
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
    print(" Error: please enter a valid integer")