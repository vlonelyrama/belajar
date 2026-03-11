# looping dari list

# for loop
kumpulan_angka = [5,4,6,7,3,2,]
for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["amba","rusdi","imut","gatot"]
for member in peserta:
    print(f"member = {member}")

# for loop dan range untuk index(cara riber)
kumpulan_angka = [10,2,5,6,7]
panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

print("======while======")
# while
kumpulan_angka = [2,5,7,4,3,8]
panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(f"angka{kumpulan_angka[i]}")
    i += 1

