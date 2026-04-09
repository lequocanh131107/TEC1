import re
code = input("Enter a course code: ")
pattern = r'^[A-Z]{2,3}\d{3}$'
if re.match(pattern, code):
    print(True)
else:
    print(False)