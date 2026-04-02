<<<<<<< HEAD
import re

text = input("Enter a sentence: ")

print(re.sub(r'\b\d{10}\b', "[REDACTED]",
=======
import re

text = input("Enter a sentence: ")

print(re.sub(r'\b\d{10}\b', "[REDACTED]",
>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
      re.sub(r'\+84\d+', "[REDACTED]", text)))