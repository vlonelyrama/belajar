# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assigment

a = 5 # ini adalah assigment
print("nilai a =",a)

#a = a + 1
print("nilai a =",a)

a += 1 # artinya adalah a = a + 1
print("nilai a += 1, nilai a menjadi",a)

a -= 2 # artinya adalah a = a - 2
print("nilai a -= 2, nilai a menjadi",a)

a *= 5 # artinya adalah a = a * 2
print("nilai a *= 5, nilai a menjadi",a)

a /= 2
 # artinya adalah a = a / 2
print("nilai a /= 2, nilai a menjadi",a)

b = 10
print("nilai b =",b)

b %= 3
print("nilai b %= 3, nilai b menjadi",b)

b = 10
print("nilai b =",b)

b //= 3
print("nilai b //= 3, nilai b menjadi",b)

a = 5 
print("nilai a =",a)

a **= 3
print("nilai a **= 3, nilai menjadi ", a)

#operasi bitwise
print("=====OR====")# OR
c = True
print("nilai c =", c)

c |= False
print("nilai c |= False, nilai menjadi ", c)

print ("=====AND=====")# AND 
c = True
print("nilai c =", c)
c &= False
print("nilai c &= False, nilai menjadi ", c)
c = True
print("nilai c =", c)
c &= True
print("nilai c &= False, nilai menjadi ", c)

print ("======XOR=====")
c = True
print("nilai c =", c)
c ^= False
print("nilai c &= False, nilai menjadi ", c)
c = True
print("nilai c =", c)
c ^= True
print("nilai c &= False, nilai menjadi ", c)

print("====SHIFTING=====")
d = 0b0100
print('nilai d =',format(d,'04b'))
d >>= 2
print("nilai d >>= 2, nilai menjadi ",format(d,'04b'))
d <<= 2
print("nilai d <<= 2, nilai menjadi ",format(d,'04b'))