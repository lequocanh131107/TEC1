def calculate_sum(numbers_list):
    total = 0
    for num in numbers_list:
        total = total + num 
    return total
mine_numbers = [11, 22, 33, 44,55 ]
result = calculate_sum(mine_numbers)
print(f"The sum of the numbers is: {result}")