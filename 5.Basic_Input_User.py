# episode input dari user

# data yang dimasukkan pasti str
nama = input("masukkan nama: ")
pekerjaan = input("masukkan pekerjaan: ")
print("nama: ", nama, "type: ", type(nama))
print("pekerjaan: ", pekerjaan, "type: ", type(pekerjaan))

# jika ingin mengambil int,float maka harus dicasting

nama = input("masukkan nama: ")
umur = int(input("masukkan umur: ")) ###
pekerjaan = input("masukkan pekerjaan: ")
ukuran_sepatu = float(input("masukkan ukuran sepatu: ")) ###
print("masukkan umur: ", nama, "type: ", nama)
print("masukkan umur: ", umur, "tipe: ", type(umur))
print("masukkan pekerjaan: ", pekerjaan, "tipe: ", type(pekerjaan))
print("masukkan ukuran sepatu: ", ukuran_sepatu, "tipe: ", type(ukuran_sepatu))

# bagaimana dengan boolean
data = bool(input("masukkan data: ")) # ini akan tetap true
print("masukkan data: ", data)

data = bool(int(input("masukkan data: "))) # jika ingin ada false, maka casting int
print("masukkan data: ", data)