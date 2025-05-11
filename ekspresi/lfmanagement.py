# Library file management adalah kumpulan library yang dirancang
# untuk membantu pengguna dalam mengelola dan berinteraksi dengan 
# berkas dan direktori pada sistem file. Beberapa library file
# management adalah berikut.


# 1. Os 
# modul os pada python berguna untuk fungsi fungsi yang berkaiitan dengan sistem operasi
# misal nya open(), path(), getcwd() dan lainnya 
# untuk memafaatkan fungsi yang sama dan mengeksekusi fungsi terkait os yang mungkin 
# berbeda dalam setiap sistem operasi.
# ada beberapa fitur yang hanya bekerja pada sistem operasi tertentu 

# conth os.getcwd(),akan mengembalikan string reseprentasi dari curent working directorry
# tempat direktori python kita berbeda, berlaku pada semua os 

import os 
print(os.getcwd())

# 2.JSON

# Untuk serialization dengan bahasa lain, umumnya kita menggunakan JSON(JavaScript Object Notation) yang memiliki beberapa perbedaan karakteristik dengan pickle, yakni berikut.
# JSON adalah format text-serialization dan umumnya menggunakan Unicode atau UTF-8. Sementara pickle bersifat binary serialization.
# JSON dapat dibaca dengan mudah oleh manusia, sementara pickle tidak.
# JSON dapat dioperasikan dan digunakan di luar ekosistem Python. Pickle adalah Python-specific.
# JSON secara default hanya dapat merepresentasikan subset dari built-in type pada Python.
# Pickle dapat merepresentasikan hampir (jika tidak seluruh) tipe Python dan secara default melakukan kompresi data.

# Sebagaimana yang telah disebutkan sebelumnya, JSON adalah format text yang ditujukan untuk serialization. Agar data dapat dengan mudah ditransmisikan antar berbagai sumber tanpa khawatir bentuknya kacau, menggunakan JSON adalah salah satu pilihan yang tepat.



# JSON memiliki format yang hampir mirip dengan dictionary, 
# yakni data disimpan dengan format key dan value pair. 
# Namun, tentunya JSON jauh lebih kompleks dari dictionary.
# Dapat dilihat dari contoh JSON untuk data pembelian di bawah.


# Dengan JSON kita dapat menyimpan data dengan lebih teratur. Sebuah key seperti children di bawah dapat memiliki sebuah dictionary baru yang berisi informasi terkait objek children tersebut.

import json 

#contoh JSON:
x = '{"nama":"Buchori", "umur":22, "Kota":"New York"}'

# parse x:
y = json.loads(x)

print(y["umur"])

# 3.Pickle

# Jika Anda memiliki sebuah list yang ingin disimpan atau ditransmisikan
# tanpa khawatir bentuknya akan rusak atau kacau, fungsi dari library 
# pickle dapat dimanfaatkan. Pickle termasuk fungsi Object Serialization
# pada Python. Pickling adalah istilah untuk mengubah objek menjadi byte
# stream, sedangkan unpickling adalah perlakuan sebaliknya.

# Kode berikut adalah contoh cara melakukan proses pickle pada sebuah
# object dictionary dan menyimpannya pada sebuah file.

import pickle  # Mengimpor modul pickle untuk serialisasi data

# Membuat dictionary
contoh_dictionary = {1: "6", 2: "2", 3: "f"}

# Membuka file 'dict.pickle' dalam mode 'wb' (write binary)
pickle_keluar = open("dict.pickle", "wb")

# Menyimpan (dump) dictionary ke dalam file 'dict.pickle'
pickle.dump(contoh_dictionary, pickle_keluar) #pickkle mengonversi dictionary ke format biner dan menyimpan file nyya 

# Menutup file setelah selesai menulis
pickle_keluar.close()
#kode berikut untuk mengekstraksi bekas pickle dan menaruhnya dalam sebuah variabel 




# 2.
import pickle  # Mengimpor modul pickle untuk deserialisasi data # untuk mmembaca data yang disimpan pada biner 

# Membuka file 'dict.pickle' dalam mode 'rb' (read binary)
pickle_masuk = open("dict.pickle", "rb")

# Membaca (load) data dari file pickle ke dalam variabel dictionary
contohDictionary = pickle.load(pickle_masuk)

# Menutup file setelah selesai membaca
pickle_masuk.close()
