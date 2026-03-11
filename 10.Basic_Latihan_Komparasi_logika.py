# Episode latihan Komparasi dan Logika

# membuat gabungan area rentang dari sebuah angka

#++++++3-------10+++++++

inputuser = float(input("masukkan angka yang bernilai\nkurang dari 3\natau\nlebih dari 10\n:"))

# kurang dari 3
iskurangdari = (inputuser < 3)
print("kurang dari 3 :", iskurangdari)

# lebih besar dari 10
islebihdari = (inputuser > 10)
print("lebih dari 10 :", islebihdari)

# gabungkan
iscorret = iskurangdari or islebihdari
print("anggka yang dimasukkan :", iscorret)

print("============")
#-----7++++++++15-----
inputuser = float(input("masukkan angka yang bernilai\nlebih dari 7\ndan\nkurang dari 15\n:"))

# lebih dari 7
islebihdari = inputuser > 7
print("lebih dari 7 :", islebihdari)

#kurang dari 15
iskurangdari = inputuser < 15
print("kurang dari 15 :", iskurangdari)

#gabungkan
iscorret = islebihdari and iskurangdari
print("angkka yang dimasukkan :", iscorret)