# membuat kalkulator sederhana

angka_pertama = float(input("masukkan angka pertama: "))
operator = input("masukkan operator: +, -, *, %: ")
angka_kedua = float(input("masukkan angka kedua: "))

if operator== "+":
    hasil = angka_pertama + angka_kedua
    print(hasil)
elif operator== "-":
    hasil = angka_pertama - angka_kedua
    print(hasil)
elif operator== "*":
    hasil = angka_pertama * angka_kedua
    print(hasil)
elif operator== "%":
    hasil = angka_pertama - angka_kedua
    print(hasil)

# diskon belanja

total = float(input("masukkan harga total: "))

if total >= 100.000:
    diskon = total * 0.10
else:
    diskon = 0
bayar = total - diskon
print(diskon)
print(bayar)

# nilai ujian

nilai = input("masukkan nilai ujian: ")

if nilai >= "65":
    print("kamu lulus")
elif nilai <= "65":
    print("kamu remedial, tolol")


