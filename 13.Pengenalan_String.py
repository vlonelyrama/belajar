data = "abdul"
print(data)
print(type(data))

# 1. Cara membuat string
# - dengan menggunakan single quote '.....'
data = 'abdul'
print(data)

# - dengan menggunakan double quote "....."
data = "ganteng bngtt"
print(data)

# - dengan menggabungkan quote '"....."' bisa dibalik
data = '"haii gantenkkk"'
print(data)

data = "kalian harus sholat jum'at"
print(data)

# 2. menggunakan tanda \ (backslash)
# - membuat tanda ' menjadi string
data = 'rajinlah untuk sholat jum\'at'
print(data)
data = 'don\'t, doesn\'t, didn\'t, isn\'t'
print(data)

# - membuat backslash terbaca (double)
data = ("C:\\user\\Abdul")
print(data)
 # - tab (semakin banyak tab, semakin jauh)
data = ("ucup\t\t\totong")
print(data)
# - backspace (semakin dekat)
data = ("abdul\brama")
print(data)
# - newline (baris baru)
data = ("satu\ndua\ntiga") # LF (Line Feed) used by unix, macos, linux
print(data)
data = ("satu\rdua\rtiga") # CR (Carrige Return) used by commodore, acorn, lisp
print(data)
data = ("satu\r\ndua\r\ntiga") # CRLF (Line Feed Carriage Return) used by windows
print(data)

# 3. String literal atau raw (r) agar lebih gampang
# data = ("C:\\User\\Abdul") dari ini menjadi...
data = (r"C:\User\Abdul") # menggunakan raw string (r)
print(data)
# multiline literal string
print("""
Nama : Abdul
Kelas : -5   
""")
# multiline literal string and RAW (r)
print(r"""
Nama : Abdul
Kelas : -5\anomali
web : www.abdul.com/newID    
""")