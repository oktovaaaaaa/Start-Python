# oop object oriented programming 

# tipe atau class tidak lebih penting dari  method

# i = "makanan" akalu diganti jadi anglka sepert =203
# print(len(i)) tidak bisa karena hanya untuk string tidak untuk int 

print("Class, Object, dan Method")

#class adalah bluprint objek yg memiliki karaktersitik like, manusia , mobil 

#objek merupakan perwujudan class dengan anggapan bahwa kelas 
# adalah cetakan yang memungkinkan kita dapat membuat 
# banyak objek berdasarkan cetakan 

# Mtethod adalah perilaku atau tindakan yanng apat dilakukan 
# oleh object atau kelas 

#perilaku tindakan yang dilakukan kelas 

# class Mobil:
#     pass # dibuat pass agar tidak eror karena hanya mendef class tidak  atribut dan method 

class Mobil: #clas adalah bentuk abstrak dari objek 
    warna = "Merah" #atribut
    
mobil_1 = Mobil() # untuk menyimpan dalam variabel mobil_1
print(mobil_1.warna) #memanggil atribut objek dari kelas mobil
# mobil_1 adalah objek dan warna adalah atribut
print("=================")


class Mobil:
    # Atribut
    warna = 'Merah'

mobil_1 = Mobil()
mobil_1.warna = "Biru" # mengubah warna menjadi biru 
print(mobil_1.warna)

print("=================")


# atribut terbagi 2 yaitu atribut kelas dan atribut objek 
# onjek jika berdasarkan kelas maka semua atribut dan nilaunya sama 

class Mobil:
    # Atribut kelas
    warna = "Merah"

mobil1 = Mobil()
print(mobil1.warna)

mobil2 = Mobil()
print(mobil2.warna)

# Mengubah atribut kelas
Mobil.warna = "Hitam"

print(mobil1.warna)
print(mobil2.warna)



print("== class constuctor =====")
# fungsi khusus untuk menentukan kondisi awal 
# ass Mobil:
#     def __init__(self):
#         self.warna = 'Merah'

print("== objek constuctor =====")

class mobil:
    def __init__(self): # __inti__ fungsi untuk menjadi construcctor 
        self.warna = "merah"         #def untuk mendefenisikan dan parameter self

mobil_1 = mobil()
mobil_2 = mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# mengubah atribbut instance 
mobil_1.warna = "Hitam"

#menampilkan kembali atribut 
print(mobil_1.warna)
print(mobil_2.warna)


print("== objek constuctor =====")
#menambahkan parameter lain 

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek 
        self.kecepatan = kecepatan
        
mobil_1 = Mobil('Merah', 'Dicodingcar', 160)
        
print(mobil_1.warna)
print(mobil_1.merek)


print("== method ===")

# mwthod untuk membuat fungsi di dalam kelas itu sedniri 
# obhject method 

# dekorator diawali sintaks @

def my_decorator(func): #my_decorator menerima fungsi func sebagai parameter
    def wrapper(): #mendef fungsi wrapper
        print("Sebelum fungsi di eksekusi.")
        func()
        print("Setelah fungsi di eksekusi")
    return wrapper
#dekorasi fungsi dengan decorator 
@my_decorator # harus menambahkan @ sebelummendef fungsi lain
def say_hello():
    print("Hello, World")
    
    #memanggil fungsi yang sudah di dekorasi
say_hello()

print("Metode dari Objek (Object Method)")
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Merah", "DicodingCar", 160)
print("Sebelum ditambahkan: ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()        # Memanggil metode tambah_kecepatan.

print("Setelah ditambahkan: ")
print(mobil_1.kecepatan)


# print("Metode dari Objek (Object Method ERORRR)")

# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan
    
#     def tambah_kecepatan(self):
#         self.kecepatan += 10
        
# Mobil.tambah_kecepatan()
# #  variabel mobil belum di defenisikan 
#  metode ini perlu parameter self dan merujuk pada objek yang dibuat 


print(" Metode secara Statis (Static Method) ")
#fungsinya bersifat independen dan tidak terkait instance kelas 
# Anda bisa menambahkan dekorator @staticmethod 
# tepat sebelum mendefinisikan fungsi atau metode.

class Mobil:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()


print(" Metode dari Kelas (Class Method) ")
# Metode terakhir adalah class method yang termasuk jenis
# metode cukup spesial dalam Python. Jika object method identik 
# dengan parameter self yang merujuk pada objek, class method juga
# memerlukan sebuah parameter yang merujuk pada kelas. Mari buat
# contoh yang sama dengan sebelumnya, tetapi kali ini menggunakan 
# class method.

class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls): # cls parameter wajib dalam clasmethod 
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

print("=================")

class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(*args):
        print(args)
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

