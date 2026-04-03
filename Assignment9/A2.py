
def find_keyword_lines(filename, keyword):
    line_numbers = []
    current_line = 1
    
    try:
        
        with open("Assignment9/" + filename, "r") as file:
            for line in file:
                
                if keyword in line:
                    line_numbers.append(current_line)
                current_line += 1
        return line_numbers
        
    except FileNotFoundError:
        print(f"Error: Khong tim thay file '{filename}' trong thu muc Assignment9.")
        return []


file_to_search = "time.txt" 
tu_can_tim = "qanh"
results = find_keyword_lines(file_to_search,tu_can_tim )

if results:
    print(f"Tu khoa '{tu_can_tim}' xuat hien tai cac dong: {results}")
else:
    print(f"Khong tim thay tu khoa.")
