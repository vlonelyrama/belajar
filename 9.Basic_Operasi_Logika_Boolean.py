# Operasi Logika atau Boolean

# not, or, and, xor

# not
print("___NOT___")
abdul_ganteng = True
tidak_ganteng = not abdul_ganteng
print('abdul ganteng? ',abdul_ganteng)
print('_______________NOT')
print("tidak_ganteng? ", tidak_ganteng)

print('___OR___')
# or (jika salah satu true, maka hasilnya true)
x = False
y = False
z = x or y
print(x,'or',y,'=',z)

x = False
y = True
z = x or y
print(x,'or',y,'=',z)

x = True
y = False
z = x or y
print(x,'or',y,'=',z)

x = True
y = True
z = x or y
print(x,'or',y,'=',z)

# and (akan true jika kedua nilai adalah true)
print("___AND___")
x = False
y = False
z = x and y
print(x,'and',y,'=',z)

x = False
y = True
z = x and y
print(x,'and',y,'=',z)

x = True
y = False
z = x and y
print(x,'and',y,'=',z)

x = True
y = True
z = x and y
print(x,'and',y,'=',z)

# xor (akan true jika salah satu True, sisa nya False)
print("___XOR___")
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

