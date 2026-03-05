import re

color = input("Enter a hex color: ")

pattern = r'^#[0-9a-fA-F]{6}$'

if re.match(pattern, color):
    print("Valid hex color")
else:
    print("Invalid hex color")