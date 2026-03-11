# teknik menduplikat list

a = ["vario","aerox","stylo"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# kita akan merubah data a
# ini akan merubah kedua list
a[1] = "scoopy"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# addres dari kedua list a dan b, jika addres sama maka tidak bisa diubah salah satunya
print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")

# menduplikat list dengan copy
print("membuat list c")
c = a.copy()
print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")
print(f"addres c = {hex(id(c))}")

############
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

c[2] = "beat ngatta"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")




