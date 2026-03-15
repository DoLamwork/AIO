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

# %% Bai 4: List and Branching tìm có nhiều kẹo nhất
# Hàm nhập input
def nhap_danh_sach_keo():
    chuoi_nhap = input()
    danh_sach_chuoi = chuoi_nhap.split()

    candies = []
    for value in danh_sach_chuoi:
        candies.append(int(value))
    return candies    

#%% Nhap input pro
def nhap_danh_sach_keo():
    candies = [int(so) for so in input("nhap danh sach: ").split()]
    extra_candies = int(input("nhap extra: "))
    return candies, extra_candies

#%%Tim max
def tim_max(candies, extra_candies):
    record = max(candies)
    result = [(keo + extra_candies) >= record for keo in candies]
    return result

#%% Lap rap
danh_sach_keo, extra = nhap_danh_sach_keo()
print(f"Mang keo: {danh_sach_keo} | Keo thuong: {extra}")
ket_qua = tim_max(danh_sach_keo, extra)
print(ket_qua)
# %% Test
#Test 1
tc1_candies = [2, 3, 5, 1, 3]
tc1_extra = 3
tc1_expected = [True, True, True, False, True]

# Test Case 2
tc2_candies = [4, 2, 1, 1, 2]
tc2_extra = 1
tc2_expected = [True, False, False, False, False]

assert tim_max(tc1_candies, tc1_extra) == tc1_expected
assert tim_max(tc2_candies, tc2_extra) == tc2_expected

# %% [markdown]
# # ==========================================
# # BÀI 5: COMPUTING MEDIAN FOR A LIST OF NUMBERS
# # ==========================================
# %%
#Tao list
lst_data = [i for i in range(1,11)]
print(lst_data)
# %%
#Tinh mean cho so le va so chan, khong dung numpy
def mean(list):
    sum = 0
    for value in list:
        sum += value
    mean = sum/len(list)
    return mean

# %%so chan, so le
so_chan = [i for i in lst_data if i%2 == 0 ]
so_le = [x for x in lst_data if x%2 != 0]

# %%
mean_so_chan = mean(so_chan)
mean_so_le = mean(so_le)
print(f"Mean le: {mean_so_le} - Mean chan: {mean_so_chan}")
# %% Tinh med
def med(list):
    list_sorted = sorted(list)
    mid_index = len(list)//2
    if len(list)%2 != 0:
        return list[mid_index]
    else:
        left_mid_index = mid_index - 1
        right_mid_index = mid_index + 1
        return (list[left_mid_index] + list[right_mid_index]) /2

# %%
med_lst_data = med(lst_data)
print(med_lst_data)
# %%
med_so_chan = med(so_chan)
print(med_so_chan)
# %% [markdown]
# # ==========================================
# # BÀI 7: BAG OF WORD NLP
# # ==========================================
#%%input
corpus = ["Tôi thích môn Toán", "Tôi thích AI", "Tôi thích âm nhạc"]
cau_moi = "Tôi thích AI thích Toán"
# %%Cắt tất cả các câu trong corpus thành chữ rời rạc và gom vào 1 list
tat_ca_tu = []
for cau in corpus:
    tat_ca_tu.extend(cau.split())
print(tat_ca_tu)
# %% Lọc trùng lặp bằng set() và sắp xếp A-Z bằng sorted()
bag_of_word = sorted(list(set(tat_ca_tu)))
print(bag_of_word)
# %% TẠO VECTOR CHO CÂU MỚI
tokens_cau_moi = cau_moi.split()
# Dùng List Comprehension để đếm số lần xuất hiện của mỗi từ
vector = [tokens_cau_moi.count(tu) for tu in bag_of_word]
print(vector)
# %%
