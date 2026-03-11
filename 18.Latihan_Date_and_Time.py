# Date and Time (latihan)

# import datetime as dt
# hari_ini = dt.date.today()
# print(hari_ini)
# print(f"hari ini adalah hari : {hari_ini%A}")

#manual
import datetime as dt

tanggal = dt.date(2005,9,19)
print(tanggal)
# print(f"tanggalnya adalah = {tanggal:%A}")

print("silahkan masukkan tanggal, \nbulan, dan tahun data kamu")
tanggal = int(input("tanggal \t:")) # \t adalah jarak
bulan = int(input("bulan \t\t:"))
tahun = int(input("tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")
# print(f"hari nya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}")
umur = hari_ini - tanggal_lahir 
umur_tahun = umur.days // 365
umur_bulan_sisa = (umur.days % 365) // 30
print(f"umur anda adalah : {umur}")
print(f"umur tahun anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")



