# operasi dan manipulasi string

# 1. menyambung string (concatenate). + " " +
nama_pertama = "abdul"
nama_tengah = "tukang"
nama_akhir = "galon"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string. len
panjang = len(nama_lengkap)
print("panjang namanya", nama_lengkap + " = " + str(panjang))

# 3. operator untuk string
# mengecek apakah ada komponen char atau string di string
V = "galon"
status = V in nama_lengkap
print(V + " ada di " + nama_lengkap + " = " + str(status))
v = "Galon"
status = v not in nama_lengkap
print(v + " tidak ada di " + nama_lengkap + " = " + str(status))

#mengulang string
print("abdul"*10)
print(10*"abdul")

#indexing (dimulai dari angka 0)
print("index ke-17 : " + nama_lengkap[17])
print("index ke-11 : " + nama_lengkap[11])
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
#index dengan angka negatif akan dimulai dari nama huruf paling akhir (start mulai dari -1)
print("index ke-(-17) : " + nama_lengkap[-17])
print("index ke-(-4) : " + nama_lengkap[-4])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-5) : " + nama_lengkap[-5])
#range
print("index ke-[0:5] : " + nama_lengkap[0:5])
print("index ke-[2:11] : " + nama_lengkap[2:12])
#jeda
print("index ke-[1,3,5,7,9] : " + nama_lengkap[1:9:2])
#item paling kecil 
print("item paling kecil : " + min(nama_lengkap))
#item paling gedeee
print("item paling gedeee : " + max(nama_lengkap))

ascii_code = ord("r")
print("ASCII code dari huruf r adalah : " + str(ascii_code))

data = 144
print("char untuk ascii code dari 144 adalah : " + chr(data))

# 4. operator dalam bentuk method
data = "abdul akan makan bayam dan agar agar"
jumlah = data.count("a")
print("jumlah a pada " + data + " = " + str(jumlah))
