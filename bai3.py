def dao_nguoc_so_nguyen(num):
   
    ket_qua = 0

   
    while num > 0:
        
        chu_so = num % 10

       
        ket_qua = ket_qua * 10 + chu_so

        
        num = num // 10

    return ket_qua


so_nguyen_nhap = int(input("Nhập một số nguyên: "))


so_nguyen_dao_nguoc = dao_nguoc_so_nguyen(so_nguyen_nhap)


print(f"Số nguyên đảo ngược của {so_nguyen_nhap} là {so_nguyen_dao_nguoc}.")
