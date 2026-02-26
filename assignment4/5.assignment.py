def filter_even_numbers(input_list):
    even_numbers = [] # This is the empty box for even numbers
    
    for num in input_list:
        if num % 2 == 0: # If the number is even (divisible by 2)
            even_numbers.append(num)
            
    return even_numbers
original_list = [56, 27, 38, 43, 53, 66, 79, 89, 90, 10]
reduced_list = filter_even_numbers(original_list)
print(f"Original list: {original_list}")
print(f"Reduced list (even numbers): {reduced_list}")