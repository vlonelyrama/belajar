# format string

# contoh generic
nama = "abdul"
str = "woyy " + nama
print(str)

#lebih rapi
nama = "abdul"
format_str = f"woyyy {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 1390.77
format_str = f"ini adalah angka = {angka}"
print(format_str)

# bilangan bulat
angka = 17
format_str = f"angka bilangan bulat = {angka:d}" # d hanya berfungsi untuk menampilkan bil bulat
print(format_str)

# bilangan ada koma seperti 2,000 3,000,000
angka = 3140
format_str = f"angka ribuan = {angka:,}"
print(format_str)
angka = 3134570
format_str = f"angka jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2007.78910
format_str = f"desimal = {angka:.3f}" # . (batas angka) 3 (batas huruf yang terikut)
print(format_str)

# menampilkan leading zero
angka = 2007.78910
format_str = f"desimal = {angka:010.3f}" 
print(format_str)

# menampilkan tanda + atau -
angka_minus = -20
angka_plus = 20
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+d}" # tambahkan +d agar tanda + - muncul
print(format_minus)
print(format_plus)

angka_minus = -20.6079
angka_plus = 20.44590
format_minus = f"minus = {angka_minus:+.3f}"
format_plus = f"plus = {angka_plus:+.2f}" # jika angka besar, maka seperti ini
print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:%}"
print(format_persen)
persentase = 0.045
format_persen = f"persen = {persentase:.2%}" # .2 mau berapa banyak angka dibelakang koma
print(format_persen)

# melakukan operasi aritmatika didalam placeholder {}
harga_ban = 367000
jumlah = 2
format_string = f"harga total Rp = {harga_ban*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadesimal)
angka = 1000
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexadesimal = f"hexadesimal = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hexadesimal)