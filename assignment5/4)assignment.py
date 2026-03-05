import re

text = input("Enter a sentence: ")

print(re.sub(r'\b\d{10}\b', "[REDACTED]",
      re.sub(r'\+84\d+', "[REDACTED]", text)))