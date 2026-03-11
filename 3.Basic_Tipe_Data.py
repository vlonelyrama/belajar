# a = 10, a adalah variabel dengan nilai 10

# tipe data: Angka satuan int(integer)
data_integer = 1
print("data : ", data_integer, ", bertipe : ", type(data_integer))

data_integer = 10
print("data : ", data_integer)
print("bertipe : ", type(data_integer))

# tipe data : Angka dengan coma (float)
data_float = 2.5
print ("data : ", data_float, "bertipe : ", type(data_float))

data_float = 20.3
print("data : ", data_float)
print("bertipe : ", type(data_float))

# tipe data : kumpulan kata kata atau karakter str(string)
data_string = "abdul"
print("data : ", data_string, "bertipe : ", type(data_string))

data_string= "ganteng"
print("data : ", data_string)
print("bertipe : ", type(data_string))

# tipe data : antara True/False boolean(bool)
data_bool = True
print("data : ", data_bool, "bertipe : ", type(data_bool))

data_bool = False
print("data : ", data_bool)
print("bertipe : ", type(data_bool))

# tipe data khusus : bilangan complex seperti 5i, i adalah imaginer
data_complex = complex(5.9)
print("data : ", data_complex, "bertipe : ", type(data_complex))
print("bertipe : ", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.5)
print("data : ", data_c_double, "bertipe : ", type(c_double))

data_c_double = c_double(20.5)
print("data : ", data_c_double)
print("bertipe : ", type(c_double))