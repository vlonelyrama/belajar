data_1 = [1,2,3]
data_2 = [4,5,6]

semua_data = [data_1,data_2]
semua_data_copy = semua_data.copy()
print(f"semua data {semua_data}")
print(f"data copy {semua_data_copy}")

# mengambil nested list
data = semua_data[0][1]
print(data)

# addres semua data
print(f"addres semua data {hex(id(semua_data))}")
print(f"addres data copy {hex(id(semua_data_copy))}")

# addres setiap data, masih samaa
print(f"addres dari no urut 1")
print(f"addres no urut 1 {hex(id(semua_data[0]))}")
print(f"addres no urut 1 copy {hex(id(semua_data_copy[0]))}")

# kita gunakan deep copy

from copy import deepcopy
semua_data = [data_1,data_2]
semua_data_deep = deepcopy(semua_data)
print(f"addres semua data {hex(id(semua_data))}")
print(f"addres data copy {hex(id(semua_data_deep))}")

print(f"addres no urut 1 {hex(id(semua_data[0]))}")
print(f"addres no urut 1 copy {hex(id(semua_data_deep[0]))}")