def reverse_in_place(lst):
    dau = 0
    cuoi = len(lst) - 1

    while dau < cuoi:
        
        lst[dau], lst[cuoi] = lst[cuoi], lst[dau]

        
        dau = dau + 1
        cuoi = cuoi - 1


# Nhập một danh sách bất kỳ
input_string = input("Nhập danh sách theo cú pháp [1,2,3,...] ")
my_list = eval(input_string)

reverse_in_place(my_list)

# In kết quả
print(my_list)


