# latian perhitungan sederhana 

celcius = float(input("masukkan suhu celcius: "))
print("suhu adalah: ", celcius,"celcius")

#kita akan konversikan suhu
# reamur
reamur = (4/5) * celcius
print("hasilnya adalah: ", reamur, "reamur")

# fahreinheit
fahreinheit = 9/5 * celcius + 32
print("hasilnya: ", fahreinheit, "fahreinheit")

# kelvin 
kelvin = celcius + 273
print("hasilnya: ", kelvin, "kelvin")

fahreinheit = float(input("masukkan suhu fahreinheit:"))
print("suhu adalah: ", fahreinheit, "fahreinheit")
celcius = 5/9 * (fahreinheit - 32)
kelvin = celcius + 273
print("hasil suhu kelvin: ", kelvin, "kelvin")

kelvin = float(input("masukkan suhu kelvin: "))
print("suhu adalah: ", kelvin, "kelvin")

