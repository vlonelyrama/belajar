# operasi aritmatika

# operasi pertambahan +
a = 10
b = 5
c = 2
hasil = a + b + c
print(a,'+',b,'+',c,'=',hasil)

# operasi pengurangan -
a = 30
b = 7 
c = 8
hasil = a - b - c
print(a,'-',b,'-',c,'=',hasil)

# operasi perkalian *
a = 2
b = 4 
c = 8
hasil = a * b * c
print(a,'*',b,'*',c,'=',hasil)

# operasi pembagian /
a = 12
b = 8
c = 2
hasil = a / b / c
print(a,'/',b,'/',c,'=',hasil)

# operasi eksponen (pangkat) **
a = 2
b = 3
c = 2
hasil = a ** b ** c 
print(a,'**',b,'**',c,"**",hasil)

# operasi modulus (sisa pembagian) %
a = 10
b = 4 
hasil = a % b 
print(a,'%',b,'=',hasil)

# operasi floor division (pembulatan pembagian) //
a = 12
b = 8 
c = 2
hasil = a // b // c
print(a,'//',b,'//',c,'=',hasil)

# prioritas operasi
# 1. ()  2. eksponen **  3. perkalian * dan pembagian /  4. pertambahan + dan pengurangan -

x = 5
y = 12 
z = 4 
hasil = x + y * z - x ** z
print(x,'+',y,'*',z,'-',x,'**',z,'=',hasil)
# kurung yang paling diprioritaskan
hasil = x + y * (z - x) ** z
print(x,'+',y,'*',z,'-',x,'**',z,'=',hasil)

