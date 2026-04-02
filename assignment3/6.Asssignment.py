<<<<<<< HEAD
def get_middle_character(text):
    length = len(text)

    middle = length // 2
    
    if length % 2 == 0:
        return text[middle - 1 : middle + 1]
    else:
        return text[middle]

user_input = input("Enter text: ")
result = get_middle_character(user_input)
=======
def get_middle_character(text):
    length = len(text)

    middle = length // 2
    
    if length % 2 == 0:
        return text[middle - 1 : middle + 1]
    else:
        return text[middle]

user_input = input("Enter text: ")
result = get_middle_character(user_input)
>>>>>>> 26e297e939b2fb547af87325b46d2e333a93b1f7
print(f"the result is: {result}")