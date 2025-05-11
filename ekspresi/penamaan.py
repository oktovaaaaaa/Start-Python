# # prinsip overiding

# # dibuat sesuai fungsi namanya yang berguna 

# cariJalan() # ini fungsin nyah untuk mencari jalan
# #akan lebih mudah dipahami dibandng 
# jalan()

# #penamaan deskriptif 
# nama yang informatif, jelas, dan sesuai dengan tujuan dari elemen koce

# jangan menggunakan fungsi frasa seperti :
# # f_mean, r_name 
# prinsip python yang berlaku dalam penamaan sbg berikut :

# Atribut dan method name bersifat pre-fixed dengan objek.
# Function name selalu diawali dengan module name.

# # _diawali_sebuah_garis_bawah: penamaan ini dapat digunakan untuk penggunaan internal lemah yang merujuk pada penggunaannya dengan lingkup tertentu.
# # diakhiri_sebuah_garis bawah_: penamaan ini digunakan untuk mengatasi redundan dengan keyword/reserved words di Python.
# # __diawali_dua_garis bawah: menegaskan bahwa sebuah objek adalah bagian dari kelas tertentu.
# # __diawali_dan_diakhiri_dua_garis bawah__: Objek atau atribut tertentu yang diciptakan Python untuk digunakan dalam program. Contohnya adalah  __init__, __import__ or __file__.

# class contrsuctor adalah :
#     alam Python, constructor pada class adalah sebuah method khusus yang bernama __init__. Method ini otomatis dipanggil saat sebuah objek (instance) dari class tersebut dibuat. Fungsi utama dari constructor adalah untuk:

# Inisialisasi atribut objek: Constructor digunakan untuk menetapkan nilai awal ke atribut-atribut (variabel) yang dimiliki oleh objek.

# Melakukan konfigurasi awal: Constructor dapat melakukan tindakan lain yang diperlukan saat objek baru dibuat, seperti membuka file, membuat koneksi database, atau melakukan perhitungan awal.


# Nama paket juga sebaiknya singkat, menggunakan huruf kecil, dan hindari garis bawah(_). Contohnya, jika kita membuat paket bernama "math" yang di dalamnya ada modul 'math_operations.py"

# Penulisan Tipe Variabel
# Untuk penamaan variabel, umumnya menggunakan CamelCase atau CapWords, lebih pendek lebih baik.

# T, AnyStr, Num

# Jika terdapat covariant atau contravariant dari sebuah variabel, tambahkan di akhir variabel untuk mempermudah pembacaan. Covariant memungkinkan Anda menggunakan tipe turunan (lebih spesifik) dari yang telah ditentukan sebelumnya. Adapun, contravariant adalah istilah yang merujuk pada kemampuan untuk menggunakan tipe yang lebih umum dari sebelumnya.

# from typing import TypeVar
# VT_co = TypeVar('VT_co', covariant=True)
# KT_contra = TypeVar('KT_contra', contravariant=True)


# Nama Exception
# # Untuk pengecualian (exception), Anda juga menerapkan konvensi penamaan
# # kelas pada exception karena ia seharusnya bertipe kelas. Bedanya,
# # tambahkan "Error" atau nama deskriptif lain pada nama exception Anda. 
# # Contoh kodenya sebagai berikut.

""" class DivideByZeroError(Exception):
    def __init__(self, message ="Division by zero is not allowed"):
        super().__init__(message)
        
def devide_numbers(a, b):
    if b == 0:
        raise DivideByZeroError("Cannot divide by zero")
    return a / b

try:
    result = devide_numbers(10, 0)
except DivideByZeroError as e:
    print(f"Eror: {e}") """
    
#     Nama Variabel Global
# Dalam variabel global, penamaannya bisa mengikuti fungsi/modul 
# yang bersifat publik. Anda bisa menggunakan garis bawah untuk menghindari
# variabel tersebut diimpor jika ia termasuk modul non-publik.


# Nama Fungsi, Parameter, dan Variabel
# Nama fungsi, parameter, dan variabel sebaiknya menggunakan huruf kecil
# dengan pemisahan menggunakan garis bawah untuk meningkatkan keterbacaan
# . mixedCase dapat digunakan jika ada dependensi dengan pustaka
# menggunakan style tertentu.


# Argumen Fungsi dan Method
# Dalam pembuatan fungsi dan method pada suatu kelas, ada beberapa hal yang perlu dipertimbangkan.

# Gunakan self sebagai argumen pertama jika Anda membuat instance method.
# Gunakan cls sebagai argumen pertama ketika Anda membuat class method.
# Jika nama argumen fungsi adalah reserved keyword, tambahkan garis bawah di akhir nama argumen. 
# Jangan mengorbankan keterbacaan nama dengan menyingkatnya.
# Mengganti argumen bernama class dengan class_ atau kelas, lebih
# baik daripada clss.



# Nama Method dan Variabel Instance
# Saat membuat method dan variabel dalam suatu kelas, gunakan standar penamaan fungsi, yaitu gunakan huruf kecil 
# dengan pemisah kata garis bawah untuk meningkatkan keterbacaan. Tambahkan garis bawah sebagai awalan untuk method
# non-publik dan variabel internal pada fungsi.

# Untuk menghindari kesamaan dengan subkelas, gunakan __dimulai_dua_garis_nama_method 
# untuk memanggil proses yang tepat. Python menggabungkan nama modul dengan
# nama kelas. Misal ada suatu kelas bernama Foo, jika kelas Foo memiliki
# atribut __a, kita tidak dapat mengaksesnya melalui Foo.__a, tetapi Foo._Foo__a. Mulai
# dengan dua garis bawah hanya digunakan jika terjadi konflik dengan atribut di kelas atau subkelas lainnya.




# Selalu Persiapkan untuk Inheritance
# Saat membangun metode dan variabel dalam sebuah kelas, sebaiknya Anda
# dapat langsung mengetahui atribut pada metode dan variabel tersebut, 
# entah publik atau non-publik. Jika Anda ragu, jadikan atributnya
# non-publik. Sebab, lebih mudah menjadikan sebuah variabel/method
# bersifat non-publik menjadi publik, dibandingkan sebaliknya.

# Variabel atau method bersifat non-publik adalah suatu variabel
# atau method yang hanya digunakan untuk lingkup tertentu dan tidak 
# diakses secara langsung di luar. Contohnya berikut.


class MyClass:
    def __init__(self):
        self._private_var = 42 # variabel non publik dengan awalan satu garis bawah
        self._secret_list = [1,2,3] #variabel non punblik lainnya 
        
        
    def _private_method(self):
        print("Ini adlah method nonpublik")
        
    def public_method(self):
        print("Ini adalah method publik")
        self._private_method() #method pubik dapat memanggil method non publik
        
        # Pada contoh di atas, method '_private_method' merupakan jenis fungsi yang tidak
        
        # diakses secara langsung. Anda bisa melihat pada method '
        # public_method', tempat kita menggunakan method private di sana. Selain itu, variabel seperti '
        # _private_var' atau '_secret_list' merupakan variabel non_publik yang tidak digunakan secara langsung ketika kelas dipanggil.
        
        
# Method/Variabel publik dipersiapkan untuk pihak eksternal 
# menggunakan kelas Anda. Anda juga otomatis berkomitmen untuk 
# menghindari adanya incompatible backward changes atau suatu 
# kode yang tidak dapat berjalan kembali setelah adanya perubahan. 


# ebaliknya, method/variabel dengan atribut non-publik hanya digunakan oleh Anda sebagai developer. Itu juga tidak memberikan garansi kepada siapa pun bahwa Anda takkan mengubah atau menghapusnya. Di sini kita tidak menggunakan atribut private karena dalam Python tidak ada atribut yang benar-benar private.

# Kategori lain dari atribut adalah "subclass API", umumnya disebut protected pada bahasa lain. Sebuah kelas dapat didesain untuk diwariskan (inherited-from), misalnya untuk memodifikasi atau menjadi ekstensi dari perilaku (behavior) kelas. Dalam mendesain kelas-kelas sejenis, pastikan untuk membuat keputusan eksplisit, variabel/method yang memiliki atribut publik, bagian dari subclass API, dan yang hanya anda gunakan secara internal.

# Saat mendeklarasikan variabel/method tersebut, ikuti panduan Pythonic berikut.

# Atribut publik tidak menggunakan awalan garis bawah.
# Jika nama sebuah method/variabel publik sama dengan reserved keyword, tambahkan akhiran garis bawah. Hindari menyingkat atau mengurangi huruf.
# Pada data publik yang bersifat simpel, hindari nama yang terlalu panjang.
# Cukup dengan nama atribut sependek mungkin. Ingatlah bahwa pada masa depan Anda akan mungkin mengembangkan skema atau data ini sehingga nama sependek apa pun mungkin akan menguntungkan Anda.
# Jika Anda berniat untuk mewariskan atau membuat subclass dari kelas dan menginginkan sebuah variabel hanya digunakan di kelas utama saja, tambahkan awalan dua garis bawah. Ini akan memudahkan Anda karena Python mengenalinya sebagai konvensi kelas, untuk menghindari kemungkinan kesamaan nama atau implementasi.
# # Sekali lagi, semua materi style guide kali ini mengacu pada PEP8 yang dapat Anda baca lebih lanjut dalam link berikut.

# reserved keywords (kata kunci yang dicadangkan) adalah kata-kata yang 
# memiliki arti khusus dalam bahasa pemrograman dan tidak dapat digunakan
# sebagai nama variabel, fungsi, kelas, atau identifier lainnya. 
# Setiap bahasa pemrograman memiliki set reserved keywords sendiri
# . Menggunakan reserved keyword sebagai identifier akan menyebabkan 
# kesalahan sintaks (syntax error).

# Contoh Reserved Keywords dalam Python:

# Berikut adalah beberapa contoh reserved keywords dalam Python. Daftar 
# lengkapnya dapat berbeda sedikit tergantung pada versi Python yang Anda
# gunakan, tetapi ini adalah yang paling umum:

# and

# as

# assert

# async

# await

# break

# class

# continue