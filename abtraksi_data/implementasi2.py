""" inclusive menerima semua(bersamaan), batas akhir akan dianggap interval """

""" eksklusif adalah sebaliknya """

print("=================================")
x = ["Okto", "topa", "oktopa", "monica", "moncan", "popo", "lolo"]

print(x[0:5:2]) 
# outputnya adalah mengambil indeks ke 0 sampai ke 4 dan melompati 2 dan kelipatannya
print(x[1:])
print(x[:3])



print("============= TUPLE ()============")
# jenis dari list yang tidak dapat diubah elemennya,  biasanya sekali dekarasi

x= (1, "dicoding", 1+3j)
print(type(x))


print("============= TUPLE () indexing sceling ============")

x = (5, "program", 1+3j)
print(x[1])
print(x[0:3])
""" menampilkan dari index 0 hingga ke 2, bersifat eksklusif """

print("============= TUPLE ()  ============")

""" x = (5, 'program', 1+4j)
x[1] = 'dicoding' """
""" tuple bersifat immutable yang artinya tidak dapat diubah """

print("============= SET ==========")
""" kumpulan item bersifat unik tanpa urutan (unordered collection) dapat dinalisasikan dengan kurawal 
 """

""" x = {1,2,3,4,5,6,7,}
print(x[0]) """
# nilai dalam set tidak bisa dilakukan dalam indexing dan datanya uniq tidak bisa duplicate , dapat menghilangkan duplicat pada data
print("============= SET ==========")

x = {1,2,3,4,5,6,7,8,9}
print(x)
print(type(x))
# di apit kurawal akan dianggap set dan dapat menghilangkan nila duplikat


# set adalah himpunan matematika, dan disinin dapat menggunakan union dan interection atau irisan 

print("============= Method, object oriented programming OOP ==========")
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("intersecction:", intersection)


print("============= dictionary ==========")
# key value yang tidak berurrutan , untuk menyimpan data eg.

x ={'name': 'Oktova Samosir', 'age': 20, 'IsMarried' : False}
print(type(x))


""" print(x[0]) ini akan eror karena tidak bisa mengakses dist menggunnakan indexing
 """
print(x['name'])

print("============= dictionary ==========")
x ={'name': 'Oktova Samosir', 'age': 20, 'IsMarried' : False}
x ['job'] = "web developer"
print(x)

print("============= dictionary ==========")
x = {'name': 'Oktova Samosir', 'age': 20, 'IsMArried': False}
del x['IsMArried']
print(x)

print("============= dictionary ==========")
x = {'name': 'Oktova Samosir', 'age':20, 'IsMarried':'False' }
x ['name'] = "Dicoding"
print(x)