# Width and multiline

data_nama = "abdul tomat"
data_umur = 50 
data_tinggi = 179.6
data_sepatu = 45

# string standar
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu {data_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

#string multiline (menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu {data_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

#string multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_sepatu}
"""
print(5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_string = f"""
nama   = {data_nama:>17}
umur   = {data_umur:>17}
tinggi = {data_tinggi:>17}
sepatu = {data_sepatu:>17}
"""
print(5*"="+"Data String"+5*"=")
print(data_string)



