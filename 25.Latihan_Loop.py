# Latihan buat segitiga

sisi = 20

# Menggunakan for
# dummy variabel
count = 1
for i in range(10):
    print("*"*count)
    count += 1

print("=====for====")

# Menggunakan while
count = 1
while True:
    # print jika ganjil
    if (count % 2):
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue
    
    # akan break jika count melebihi sisi
    if count > sisi:
        break


print("====while====")

# segitiga sempurna

count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        # print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    #akan break jika melebihi sisi
    if count > sisi:
        break

count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        # print jika ganjil
        print(" "*spasi,"+"*count)
        spasi += 1
        count -= 1
    else:
        # akan kembali ke atas jika ganjil
        count -= 1
        continue

    #akan break jika melebihi sisi
    if count > 0:
        break









