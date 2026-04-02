<<<<<<< HEAD
import re

color = input("Enter a hex color: ")

pattern = r'^#[0-9a-fA-F]{6}$'

if re.match(pattern, color):
    print("Valid hex color")
else:
=======
import re

color = input("Enter a hex color: ")

pattern = r'^#[0-9a-fA-F]{6}$'

if re.match(pattern, color):
    print("Valid hex color")
else:
>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
    print("Invalid hex color")