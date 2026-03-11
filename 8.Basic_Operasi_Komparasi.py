# Operasi Komparasi
# setiap hasil dari Operasi Komparasi adalah boolean(True/False)

# lebih dari >
print("___LEBIH DARI >___")
a = 10
b = 20
hasil = 4 > b
print(4,'>',b,'=',hasil)
hasil = a < 17 
print(a,'<',17,'=',hasil) 

# kurang dari <
print("___KURANG DARI <___")
a = 12
b = 23
hasil = a < 7
print(a,'<',7,'=',hasil)
hasil = 12 < b
print(12,'<',b,'=',hasil)

# lebih dari sama dengan >=
print("___LEBIH DARI SAMA DENGAN >=___")
a = 29
b = 19
hasil = a >= 4
print(a,'>=',4,'=',hasil)
hasil = b >= b
print(b,'>=',b,'=',hasil)

# kurang dari sama dengan <=
print("___KURANG DARI SAMA DENGAN <=___")
a = 17
b = 12
hasil = 3 <= a
print(3,'<=',a,'=',hasil)
hasil = b <= 11
print(b,'<=',11,'=',hasil)
hasil = b <= 12
print(b,'<=',12,'=',hasil)

# sama dengan ==
print("___SAMA DENGAN ==___")
a = 10
b = 4
hasil = a == 10
print(a,'==',10,'=',hasil)
hasil = b == 10
print(b,'==',10,'=',hasil)

# tidak sama dengan
print("___TIDAK SAMA DENGAN !=___")
a = 2
b = 6
hasil = 3 != a
print(3,'!=',a,'=',hasil)
hasil = b != b
print(b,'!=',b,'=',hasil)

#  is
print("___is___")
# is tidak dapat bekerja pada syntax literal, misal: a == 4, a memiliki nilai yaitu 4 dan
# menyimpan atau memakan memori yang tersimpan di komputer. sedangkan 4 disebut sebagai literal 
# karena tidak memiliki variabel (nilai saja) dan tidak memakan memori. IS hanya membandingkan 
# memori atau objek. jadi jika "a is 4" akan eror, harus a = 4, b = 7, maka "a is b". begitupun
# dengan IS NOT

# is adalah komparasi object identity
a = 5 # ini adalah assigment membuat objek
y = 5
print('nilai x = ',a,',id = ', hex(id(a)))
print('nilai y = ',y,',id = ', hex(id(y)))
hasil = a is y
print('a is y =',hasil)

a = 7
b = 5
print('nilai x = ',a,',id = ', hex(id(a)))
print('nilai y = ',b,',id = ', hex(id(b)))
hasil = a is b
print('a is b =',hasil)

# is not
print("___IS NOT___")
a = 9
b = 18
print('nilai a = ',a,',id = ', hex(id(a)))
print('nilai b = ',b,',id = ', hex(id(b)))
hasil = a is not b
print('a is b =',hasil)
