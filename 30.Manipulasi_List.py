# Operasi manipulasi list

# index  0(-4)   1(-3)   2(-2)    3(-1)
data = ["imut","rusdi","nassir","yesking"]

# menggambil data dari list
data_0 = data[0]
print(f"data pertama adalah: {data_0}")

data_akhir = data[-1]
print(f"data terakhir adalah: {data_akhir}")

data_nassir = data[-2]
print(f"data urutan ke -2: {data_nassir}")

# mengambil panjang data dalam list
panjang_data = len(data)
print(f"panjang data adalah: {panjang_data}")

# manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum open member: {data}")
data.insert(1,"Amba")
print(f"data sesudah open member: {data}")

# memambah diakhir list
data.append("mas gatot")
print(f"data penambahan member: {data}")

# menambahkan list dengan list
data_baru = ["mas fuad","mr ironi,","kumalala","mas faiz"]
data.extend(data_baru)
print(f"member baru rombongan: {data}")

# merubah data
# kita ubah data ke 9 menjadi rehan wangsaf
data[8] = "rehan wangsaf"
print(f"pergantian member baru: {data}")

# remove data
data.remove("rehan wangsaf")
print(f"rehan keluar: {data}")
# penulisan harus sesuai, jika tidak maka error

# remove data paling belakang
data.pop()
print(f"kurang jomok: {data}")