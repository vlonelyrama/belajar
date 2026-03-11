# continue, pass, break

# pass, dia berfungsi sebagai dummy, tidak akan dieksikusi

# pass
angka = 0
while angka < 5:
    angka +=1
    if angka ==3:
        pass # tidak akan dieksekusi
    print(angka)

# continue
angka = 0
print(f"angka sekarang -> {angka}")
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
    if angka == 3:
        print("mas rusdi")
        continue # akan membuat loop ke step selanjutnya

    print("imut rizzman")

# break
angka = 0
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
    if angka == 3:
        print("imut rizzman")
        break
    print("mas rusdi")
print("okee")