#%% Bài 1
#Khởi tạo, truy xuất qua index
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[0:5])
# %%
#in kết quả phần tử không chia hết cho 2(dùng for)
for i in list:
    if i % 2 != 0:
        print(i)
# %%
#in ra tổng các phần tử trong list(dùng for)
total = 0
for i in list:
    total += i
print(total)

# %%Bài 2
#Tạo mới một List có tên là lst_data, gồm các số chẵn từ 1 đến 12.
lst_data = [i for i in range(1, 13) if i % 2 ==0]
print(lst_data)

# %%
#xóa các số chia hết cho 3 trong lst_data vừa tạo
lst_data = [i for i in lst_data if i % 3 != 0]
print(lst_data)

# %%
# Thêm vào cuối lst_data các số từ 1 đến 3, và thêm vào vị trí index = 3
# một chuỗi các số từ 6 đến 8
lst_data.extend([1, 2, 3])
lst_data[3:3] = [6, 7, 8]
print(lst_data)
# %%
#Nếu các số trong list lst_data chia hết cho 2 hoặc chia hết cho 5 thì cập
#nhật thành số 0
lst_data = [0 if i % 2 == 0 or i % 5 == 0 else i for i in lst_data]
print(lst_data)

# %% List and branching
#Bài 3: cho 1 list hãy trả về các số armstrong bên trong list đó
#Viết hàm xét số Armstrong, hàm trả về 1 nếu phần tử đang xét là số Armstrong, ngược lại trả về 0
import math
def is_armstrong(n):
    chuoi_so = str(n)
    sum = 0
    for i in chuoi_so:
        sum += i**3
    if sum == n:
        return 1
    else:
        return 0

    
# %% test hàm is_armstrong
test_case_1 = [130, 270, 153, 407, 177, 371, 1000, 1634, 370]
result = []
for i in test_case_1:
    if is_armstrong(i) == 1:
        result.append(i)
print(result)

# %% 2D list
width = 2
height = 3
matrix = [[0 for j in range(width)] for i in range(height)]
print(matrix)

# %%
for i in range(height):
    for j in range(width):
        matrix[i][j] = i*width + j
print(matrix)
# %%
