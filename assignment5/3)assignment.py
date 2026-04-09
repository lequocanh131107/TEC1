
import re

text = input("Enter a paragraph: ")

numbers = re.findall(r'\d+', text)

total = 0
for num in numbers:
    total += int(num)

print("Tong cac so cong lai la", total)