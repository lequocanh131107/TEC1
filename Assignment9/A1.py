
count = 0
print("Enter your text ( Ấn enter để kích hoạt lệnh break):")

while True:
    line = input()
    if line == "": 
        break
    if line.strip() != "":
        count += 1

print(f"tổng số dòng là: {count}")