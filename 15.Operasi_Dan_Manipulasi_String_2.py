# operator dalam bentuk methods

# merubah case dari string
# upper case (huruf besar)
sapaan = "woy brooo!"
sapaan = sapaan.upper()
print("upper = " + sapaan)

# lower case (huruf kecil)
narsis = "GwE GanTenNnk PaRAaHhHh SiH"
narsis = narsis.lower()
print("lower = " + narsis)

print("="*20)
#pengecekan dengan is x method
# pengecekan lower case
sapaan = "heiii dudee"
apakah_lower = sapaan.islower() # hasilnya bool
print(sapaan + " is lower = " + str(apakah_lower))
apakah_upper = sapaan.isupper() # hasilnya bool
print(sapaan + " is upper = " + str(apakah_upper))

# isalpha() <--- untuk mengecek huruf
nama = "misterydude"
cek_nama = nama.isalpha() 
print(nama + " is alpha = " + str(cek_nama))
nama = "thundercock69"
cek_nama = nama.isalpha()
print(nama + " is alpha = " + str(cek_nama))

# isalnum() <--- untuk mengecek huruf dan angka
pw = "n4t3higg3rs0n"
cek_pw = pw.isalnum()
print(pw + " is alnum = " + str(cek_pw))
pw = "natehiggerson"
cek_pw = pw.isalnum()
print(pw + " is alnum = " + str(cek_pw))

# isdecimal() <--- untuk mengecek angka
angka = "227490"
cek_angka = angka.isdecimal()
print(angka + " is decimal = " + str(cek_angka))
angka = "10a48.95ff"
cek_angka = angka.isdecimal()
print(angka + " is decimal = " + str(cek_angka))

# isspace() <---untuk mengecek spasi, tab, newline
space = " "
cek_space = space.isspace()
print(space + " is space = " + str(cek_space))
apaan_ya = "abdul balak"
cek_apaan_ya = apaan_ya.isspace()
print(apaan_ya + " is space = " + str(cek_apaan_ya))

# istitle() <--- untuk mengecek semua kata dimulai dengan huruf besar
judul = "Superman Legacay Dc Comics"
cek_judul = judul.istitle() # hasilnya bool
print(judul + " is title = " + str(cek_judul))
judul = "spiderman brand new day"
cek_judul = judul.istitle()
print(judul + "is title = " + str(cek_judul))

print("="*20)
# mengecek komponen startswith() dan endswith()
cek_abdul = "abdul ganteng".startswith("abdul") 
print("start = " + str(cek_abdul))
cek_abdul = "abdul ganteng".endswith("jelekkk")
print("end = " + str(cek_abdul))
# kalau mau lebih gampang, bisa codingan seperti ini

# penggabungan komponen join() dan split()
pisah = ['motorku','sangat','kencang']
gabungkan = ' '.join(pisah)
print(pisah)
print(gabungkan)

gabungkan = ' ekhmm '.join(pisah)
print(gabungkan)

gabung = "motorkuekhmmsangatekhmmkencang"
print(gabung.split('ekhmm'))

#alokasi karakter rjust(), ljust(), center()
# print(5*"=" + "data" + "="*5) kalo ini ribet
# ===== data =====
kanan = "supermannn".rjust(20)
print('='+kanan+"=")
kiri = "supermannn".ljust(20)
print('='+kiri+'=')
tengah = "supermannn".center(20,"-") # tambahkan argumen agar bagus
print('='+tengah+'=')

# kebalikkannya strip()
tengah = tengah.strip("-")
print('='+tengah+'=')

