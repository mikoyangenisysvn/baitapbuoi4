def chuoi_palindrome(s):
    
    s = s.lower().replace(" ", "")

    
    for i in range(len(s) // 2):
        
        if s[i] != s[len(s) - 1 - i]:
            return False

   
    return True


input_string = input("Nhập chuỗi cần kiểm tra: ")
result = chuoi_palindrome(input_string)

if result:
    print(f"'{input_string}' là chuỗi palindrome.")
else:
    print(f"'{input_string}' không là chuỗi palindrome.")
