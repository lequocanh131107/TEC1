def calculate_average_score(filename):
    diemtong = 0
    diemhs = 0
    
    try:
       
        file_path = "Assignment9/" + filename
        
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line and "," in line: 
                    parts = line.split(",") 
                    
                   
                    score = int(parts[1])
                    
                    diemtong += score
                    diemhs += 1
        
        if  diemhs == 0:
            return 0
        return diemtong /  diemhs

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}' trong Assignment9.")
        return None
   

file_name = "grade.txt"
trungbinh = calculate_average_score(file_name)

if trungbinh is not None:
    print(f"Tổng điểm của học sinh: {trungbinh:.2f}")