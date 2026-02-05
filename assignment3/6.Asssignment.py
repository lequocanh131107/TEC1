def get_middle_character(text):
    length = len(text)

    middle = length // 2
    
    if length % 2 == 0:
        return text[middle - 1 : middle + 1]
    else:
        return text[middle]

user_input = input("Enter text: ")
result = get_middle_character(user_input)
print(f"the result is: {result}")