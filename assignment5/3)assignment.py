<<<<<<< HEAD
import re

text = input("Enter a paragraph: ")

numbers = re.findall(r'\d+', text)

total = 0
for num in numbers:
    total += int(num)

=======
import re

text = input("Enter a paragraph: ")

numbers = re.findall(r'\d+', text)

total = 0
for num in numbers:
    total += int(num)

>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
print("Tong cac so cong lai la", total)