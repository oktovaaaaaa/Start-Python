""" Perbedaan yang menonjol adalah cara array menyimpan
 nilai sangat berbeda dengan list. Pada array, nilai 
di dalamnya harus memiliki tipe data yang sama. Namun,
 pada list, nilai di dalamnya tidak harus memiliki tipe data yang sama.  """

# dala python list mirip seperti array tapi 
# tidak harus memiliki tipe data yang sama 


# library  merupakan sekumpulan kode yang telah
#  dibuat oleh developer atau programmer dan disediakan
#  kepada pengguna lain agar dapat digunakan ulang dalam
#  pengembangan program atau perangkat lunak.
x = [1, 2, 3, 4, 5]
print(x)

print("=====================")

import array # menginport agar mempunyai banyak kode baru 
# seperti fungsi array() untuk membuat array

x = array.array("i",[1, 2, 3, 4, 5])
print(x)
print(type(x))

# maka nilainya harus sama atau tipe datanya harus sama 
# contoh  [1, 2, 3, 4, 5, 'Dicoding']" akan eror karna ada int dan string digbung 

print("=====================")
# list dibagi menjdi linear dan nonlinear 
# linear beraturan dan non sebaliknya 

# dimulai dari indeks ke 0 itu adalah elemen ke 1
# array length afalah panjang aray nya 

nama_siswa1 = 90
nama_siswa2 = 100
nama_siswa3 = 50
nama_siswa4 = 80
nama_siswa5 = 85
nama_siswa6 = 45
nama_siswa7 = 80
nama_siswa8 = 75
nama_siswa9 = 50
nama_siswa10 = 60

print(nama_siswa1)
print(nama_siswa2)
print(nama_siswa3)
print(nama_siswa4)
print(nama_siswa5)
print(nama_siswa6)
print(nama_siswa7)
print(nama_siswa8)
print(nama_siswa9)
print(nama_siswa10)

print("======== array ======")

siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]

print(siswa)
print(siswa[0])


# mendeklarasikan Array 
# dalam Python kita dapat mendeklarasikan array menggunakan dua cara.
#  Pertama dengan memanfaatkan list dan kedua menggunakan library Python.

print("======== array ======")


var_list = [1,2,3]
for elemen in var_list:
    print(id(elemen))

print("======== array ======")
    # Berikut adalah struktur mendeklarasikan variabel array dengan mendefinisikan isi array secara langsung.
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)

print("======== array ======")
print("untuk default")
var_arr = [0 for i in range(10)]
print(var_arr)


print("======== array ======")

var_arr = [0 for i in range(100)]
for i in range(50):
    var_arr[i] = i
print(var_arr)


print("Mengakses elemen array")
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr[0])


print("pemrosesan sekuensia pada array")

# merujuk pada operasi yang dilakukan pada elemen elemen
# suatu array.  Operasi ini melibatkan manipulasi hingga 
# pengolahan elemen yang ada pada array. 

# pemrosesan sekuensia adalah sebuah pemmrosesan setiap elemmen aray 
# yang dimulai dari elemen pada indeks terkecil hingga terbesar

var_arr = [1,2,3,4,9]

for i in range(len(var_arr)): #len adalah jumlah elemen 
    current_element = var_arr[i]
    next_index = i+1


    if next_index < len(var_arr):
        next_element = var_arr[next_index]
#outputnya memeprint element terakhir 
    else:
        next_element = None

    print(f"Currennt element: {current_element}, next element: {next_element}")
        #current element adalah element saat ini 
print("======== array ======")


var_arr = [1,7,2,89,3]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)

print("======== array ======")


var_array = [i for i in range(101)]

# TODO: Silakan buat kode Anda di bawah ini.

rata_rata = sum(var_array) // len(var_array)

print(rata_rata)


