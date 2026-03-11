# Operasi list

data_angka = [1,3,2,6,5,4,7,9,3,5,4,2,7,8]
print(f"data angka adalah: {data_angka}")

# count data(muncul berapa kali)
jumlah_data = data_angka.count(4)
jumlah_data = data_angka.count(5)
print(f"data 4 munculnya: {jumlah_data}")
print(f"data 5 munculnya: {jumlah_data}")

# ambil posisi data (index)
data = ["amba","rusdi","imut","gatot"]
print(data)

data_posisi = data.index("rusdi")
print(f"urutan posisi rusdi: {data_posisi}")

data_posisi = data.index("imut")
print(f"urutan posisi imut: {data_posisi}")

# mengurutkan list
print(f"data angka sebelum diurutkan {data_angka}")
data_angka.sort()
print(f"setelah diurutkan {data_angka}")

print(f"data sebelum sort {data}")
data.sort()
print(f"data sesudah sort {data}")

# balik listnya
data_angka.reverse()
print(data_angka)

data.reverse()
print(data)