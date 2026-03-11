# Perulangan (loop)

# for kondisi:
#   aksi

# penggunaan dengan list
angka_list = [0,1,2,3,4] # [] ini adalah list
print(angka_list)

for i in angka_list:
    print(f"i sekarang -> {i}")
print("akhiri program")

# penggunaan dengan range
angka_range = range(1,5) # koma adalah pembatas

for i in angka_range:
    print(f"i sekarang -> {i}")
print("akhiri program")

# penggunaan dengan string
data_str = "saya imut rizzman"
for i in data_str:
    print(i)

