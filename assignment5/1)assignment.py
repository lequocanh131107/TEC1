<<<<<<< HEAD
import re
code = input("Enter a course code: ")
pattern = r'^[A-Z]{2,3}\d{3}$'
if re.match(pattern, code):
    print(True)
else:
    print(False)

=======
import re
code = input("Enter a course code: ")
pattern = r'^[A-Z]{2,3}\d{3}$'
if re.match(pattern, code):
    print(True)
else:
    print(False)

>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
