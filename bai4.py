def tuHoanVi(tuSo1, tuSo2):
    
    tuSo1 = tuSo1.replace(" ", "").lower()
    tuSo2 = tuSo2.replace(" ", "").lower()

   
    return sorted(tuSo1) == sorted(tuSo2)


tuNhap1 = input("Enter the first word or phrase: ")
tuNhap2 = input("Enter the second word or phrase: ")


ketQua = tuHoanVi(tuNhap1, tuNhap2)


if ketQua:
    print(f"'{tuNhap1}' and '{tuNhap2}' are anagrams.")
else:
    print(f"'{tuNhap1}' and '{tuNhap2}' are not anagrams.")
