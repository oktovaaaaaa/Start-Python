print("Fundamental Matriks")

# array adalah struktur data 1 dimensi dalam 1 linear dan 1 tipe data

#  lebih dari 1 itu adlaah matriks

# vertikal ke atas yaitu klom
# sebaliknya kanan yaitu bariz horizontal
# dimulai dari kiri ke kanan

""" Matriks Pengukuran
Matriks pengukuran adalah jenis matriks dengan indeks (i, j) 
yang merepresentasikan suatu titik koordinat. Setiap elemen dari matriks
ini merepresentasikan hasil pengukuran pada suatu titik koordinat
tertentu dan termasuk bilangan real atau tipe data float. """


# Matriks Satuan
# Selanjutnya adalah matriks satuan dengan elemen bernilai hanya 0 atau 1.
#  Setiap elemen matriks ini bertipe data integer.


matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriks)

print("=====================")
import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriks)

print("=====================")

import numpy
import sys


var_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# harus dipanggil dengan numpy.


print("Ukuran keseluruhan elemen list dalam bytes = ", sys.getsizeof(var_list))
print(
    "Ukuran keseluruhan elemen numpy dalam bytes = ",
    var_array.size * var_array.itemsize,
)

print("=====================")

# implementasi matriks pada python

# deklasrasi matriks
# deklaeeasi sekaliigus inisialisasi nilai matriks
# Cara pertama adalah mendeklarasikan matriks sekaligus menginisialisasikan
# nilainya dengan ukuran N baris dan M Kolom (NxM).
# Cara ini dilakukan jika kita telah mengetahui nilai yang perlu diberikan.

matriks = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]

print(matriks)
print("=====================")

# Deklarasi dengan nilai default.
# Cara kedua adalah mendeklarasikan matriks dengan nilai default.
# Sebagaimana materi array, nilai default ditentukan oleh kesepakatan
#  bersama sesuai kebutuhan dengan nilainya di luar rentang yang
# ditentukan. Misalnya, tim Anda menentukan nilai dalam list harus
# berkisar dari 1 hingga 10. Kita bisa menyepakati nilai "0" sebagai
# nilai default karena di luar jangkauan yang disepakati (1-10).
#  Cara kedua ini melibatkan list comprehension yang sama seperti
# pada materi array.

matriks = [[0 for j in range(4)] for i in range(3)]

print(matriks)
# dikerjain yang fdalam dulu (4) lalu perulangan yang luar 3

print("=====================")

# mengakses elemen matriks

var_mat = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

print(var_mat[2][1])

# menambil dari kolom inddex kedua dan baris ke satu


# perasi 1 matriks.
# Menghitung total semua elemen matriks.
# Mengalikan elemen matriks dengan konstanta.
# Transpose matriks.
# Inverse matriks.
# Menentukan determinan, dan sebagainya.
# Operasi 2 matriks:
# Menambahkan dua matriks.
# Mengalikan dua matriks.
# Pembagian dua matriks, dan sebagainya.

print("=============================")

var_mat = [[5, 0], [1, 2]]

def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j] * 2

print(def_mat)

# i untuk baris dan j untuk kolom

print("=============================")


import numpy as np

var_mat = np.array([[5, 0], [1, -2]])

result = var_mat * 2

print(result)

# tipe homogen atau tipe yang sama
# memanggilnya harus dari baris dullu baru ke kolomm
