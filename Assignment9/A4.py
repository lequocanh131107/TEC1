def caesar_cipher(filename, n, direction):
    output = ""
    
    if direction == "trai":
        n = -n
        
    try:
       
        with open("Assignment9/" + filename, "r") as f:
            text = f.read()
            for char in text:
                # Công thức ASCII cho chữ HOA ( theo như đề bài thầy minh cute cấp :3)
                if 'A' <= char <= 'Z':
                    output += chr(65 + (ord(char) - 65 + n) % 26)
                # Công thức ASCII cho chữ thường
                elif 'a' <= char <= 'z':
                    output += chr(97 + (ord(char) - 97 + n) % 26)
                # Không phải chữ thì giữ nguyên (số, ...)
                else:
                    output += char
        return output
    except:
        return "file k co ma oi file!"


print(caesar_cipher("time.txt", 6, "phai"))
# em còn 1 cách nữa nhm có vẻ dài hơn nếu thầy muốn em sẽ update lên git ạ