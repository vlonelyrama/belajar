# casting adalah merubah satun tipe ke tipe lainnya
# tipe data = int, float, string/str, boolean/bool

#casting data int

## INTEGER
print("===INTEGER===")
data_int = 9
print("data = ", data_int, "type = ", type(data_int))

data_float = float(data_int)
print("data = ", data_float, "type = ", type(data_float))

data_string = str(data_int)
print("data = ", data_string, "type = ", type(data_string))

# cara lain keknya wkwk
data_string = str(data_int)
data_string = "abdul ganteng"
print("data = ", data_string, "type = ", type(data_string))

data_bool = bool(data_int)
print("data = ", data_bool, "type = ", data_bool)

# jika data int = 0 maka data bool = False. selain dari 0, maka tetap True
data_int = 0
data_bool = bool(data_int)
print("data = ", data_bool, "type = ", type(data_bool))

## FLOAT
print("===FLOAT===")
data_float = 9.5
print("data = ", data_float, "type = ", type(data_float))

data_int = int(data_float) # nilai dibulatkan ke bawah
print("data = ", data_int, "type = ", type(data_int))

data_string = str(data_float)
print("data = ", data_string, "type = ", type(data_string))
data_string = "madam ganteng"
print("data = ", data_string, "type = ", type(data_string))

data_bool = bool(data_float) # niali akan False jika float = 0, selain itu akan True
print(" data = ", data_bool, "type = ", type(data_bool) )

data_float = 0
data_bool = bool(data_float)
print("data = ", data_bool, "type = ", type(data_bool))

# BOOLEAN
print("===BOOLEAN===")

data_bool = True
print("data = ", data_bool, "type ", type(data_bool))

data_int = int(data_bool) # nilai dibulatkan ke bawah
print("data = ", data_int, "type = ", type(data_int))

data_float = float(data_bool) # nilai akan False jika float = 0, selain itu akan True
print("data = ", data_float, "type = ", type(data_float))

data_string = str(data_bool)
print("data = ", data_string, "type = ", type(data_string))

data_bool = False
print("data = ", data_bool, "type ", type(data_bool))

data_int = int(data_bool) # nilai dibulatkan ke bawah
print("data = ", data_int, "type = ", type(data_int))

data_float = float(data_bool) # nilai akan False jika float = 0, selain itu akan True
print("data = ", data_float, "type = ", type(data_float))

data_string = str(data_bool)
print("data = ", data_string, "type = ", type(data_string))

# STRING 
print("===STRING===")
data_string = "10"
print("data = ", data_string, "type = ", type(data_string))

data_int = int(data_string) # string harus angka. jika bukan, maka akan eror
print("data = ", data_int, "type = ", type(data_int)) # jika nilai string kosong, maka akan eror

data_float = float(data_string) # string harus angka. jika bukan, maka akan eror
print("data = ", data_float, "type = ", type(data_float))

data_bool = bool(data_string) # jika nilai string kosong, maka akan False
print("data = ", data_bool, "type = ", type(data_bool))