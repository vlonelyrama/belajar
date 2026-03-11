# list di dalam list
data_1 = [1,2,3]
data_2 = [4,5,6]

list_3 = [data_1,data_2]
print(list_3)

# contoh penggunaan
peserta_1 = ["amba",25,"pria"]
peserta_2 = ["rusdi",27,"pria"]
peserta_3 = ["si imut",22,"wanita"]

list_peserta = [peserta_1,peserta_2,peserta_3]
print(f"ini list peserta : {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")

# permasalahan dengan reference
list_copy = list_peserta.copy()
print(f"peserta {list_copy}")
peserta_1[0] = "gatot"
print(f"peserta {list_copy}")
print(f"peserta {list_peserta}")