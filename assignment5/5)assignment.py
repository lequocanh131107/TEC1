
import random

N = int(input("chon diem ngau nhien: "))

inside = 0

for i in range(N):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y <= 1:
        inside += 1

pi = 4 * inside / N

print("gtri uoc luong cua pi:", pi)