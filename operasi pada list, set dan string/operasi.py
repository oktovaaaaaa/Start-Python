print("============= len() ============")
#list
contoh_list = [1,3,3,5,5,5,7,7,9]
print(contoh_list)
print(len(contoh_list))

# untuk menghitung panjang atau jumlah elemen


contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])

print(contoh_list)
print(len(contoh_list))
# perbedaannya ada dalam kurung dalam aray
#  nya danmenghitung angka dan menhindari duplikat 

contoh_list = "Belajar Python"

print(contoh_list)
print(len(contoh_list))
# menghitung jumlah dari variabelnya berapa karakter termasuk spasi


print("============= min dan max() ============")

angka = [ 13,7,24,5,96,84,71,11,38]
print(min(angka))
print (max(angka))

angka = [ -13,7,24,5,96,84,71,11,38]
print(min(angka))
print (max(angka))

print("============= count() ============")
genap = [2,4,4,6,6,6,8,10,10]
print(genap.count(6))
# menghitung banyaknya angka genap (6) = 

kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)
# menegecek boolean

print("============= nilai untuk mulltiple variable ============")
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

print("============= sort() ============")
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()

print(kendaraan)
# mengurrutkan dari abjad atau angka terkecil

print("=============  ============")

# untuk kebalikannya atau descending 
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

print(kendaraan)
print("=============  ============")

# tidak bisa jika seperti ini berbeda
""" urutan = ['Dicoding', 1, 2, 'Indonesia', 3]
urutan.sort()
print(urutan)
 """
print("=============  ============")

# urutan ascii yang dimana uppercase yang akan di prioritaskan
# ASCII (American Standard Code for Information Interchange) table merupakan sebuah kode karakter yang memetakan set karakter yang umum digunakan ke dalam angka. 
kendaraan = ['motor', 'Mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)
print("=============  ============")

""" x = (5,  'program', 1+3j)
x[1] = 'Dicoding' """


x = 'Dicoding'
x[0] = 'F'
print (x)