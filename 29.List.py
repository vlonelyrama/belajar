# List adalah kumpulan data

# data angka
data_angka = [1,2,3,4,5]
print(data_angka)

# data nama
data_string = ["imut rizzman","mas rusdi","king nassir"]
print(data_string)

# data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# data campuran
data_campuran = [1,"imut rizzman",3,True,7,"mas rusdi",False]
print(data_campuran)

## cara alternative membuat list
data_range = range(0,10,2) # range (start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
data_list = [i**2 for i in range(0,10)]
print(data_list)

# membuat list pake for if
data_list = [i for i in range(0,10) if i != 5]
print(data_list)

# genap
data_list = [ i for i in range(0,10) if i %2 ==0]
print(data_list)

data_list = [ i for i in range(0,10) if i %2 !=0]
print(data_list)