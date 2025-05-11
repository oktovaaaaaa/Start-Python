# Fungsi dalam pemrograman sebenarnya didasari oleh konsep pemetaan
#  (asosiasi) dan fungsi dalam matematika. Fungsi pada matematika
#  merupakan pemetaan antara dua himpunan nilai, yaitu domain dan range.
#


#  input (domain) dan output (range)

# f(x) = 2x
# f adalah nama fungsi 
# (x) adalah input 
# 2x adalah apa yang harus diekluarkan (output)

# f dari x sama dengan 2 kali x

# fungsi adalah blok kode yang dapat dinakan untuk mengeksekusi



# Built-in Functions
# Built-in functions atau dalam bahasa Indonesia berarti fungsi
#  bawaan adalah kumpulan fungsi yang sudah terintegrasi dengan bahasa 
# pemrograman Python contoh print, leen, type

# User-defined Functions
# User-defined functions atau dalam bahasa Indonesia berarti fungsi
#  yang didefinisikan pengguna adalah jenis fungsi yang kita definisikan
#  sendiri untuk melakukan tugas spesifik tertentu. Contoh dari
#  user-defined functions adalah fungsi yang telah kita buat
#  di awal materi ini tentang mencari luas persegi panjang.


def mencari_luas_persegi_panjang(panjang,lebar): #header panjang dan lebar 
    # adalah parameter fungsinya (:) adalah awal blok kode fungsi , mencari luas
    #adalah nama fungsi
    luas_persegi_panjang = panjang*lebar # body untuk mendef apa yang akan dikerjakan
    #panjang * lebar adalah function 
    return luas_persegi_panjang # untuk mengembalikan nilai dari fungsi 

# def dan return adalah  keyword yang duguhakan 

# untuk menyimoan nilai fungsi yang di kembalikan 
persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10) #mencari luas untuk memanggil fungsi dan angka nya adalah argumen fungsi 
print(persegi_panjang_pertama)

print("+=== Docstring ===+")
# documentation string untuk membuat dokumentasi terhadap funsgi yg dibuat 
# berupa argumen, return, deskripsi fungsi 
#  docstring nya adalah ("""  """)



print("+=== Argumen dan parameter ===+")

# parameter untuk menampung nilai 
# dan nilai tersebut adalah argumen 
# intinya pparameter menampung argumen 

def mencari_luas_persegi_panjnag(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(lebar=10, panjang=5)
print(persegi_panjang_pertama)

# #positional argument
# kebalikan dari keyword argumen adalah postional 
# tidak menyebutkan nama parameter(identifir) persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)

print("=== jenis pparameter ====")

print("positional-or-keyword")
# parameter default python 
def greeting(nama, pesan):
    return "Halo, " + nama + "!" + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore !", nama="Dicoding"))

print("positional only ")
# dimamfaatkan dengan menggunakan
# jenis argumen posisi saat pemanggilan fungsi menggunakan sintaks "/"

def penjumlahan(a,b,/):
    return a + b
print(penjumlahan(8,50))

def penjumlahan(a,b):
    return a + b
print(penjumlahan(a=3, b=5))

print("Keyword only")
def greeting (*,nama, pesan): # * untuk mendefenisikan parameter fungsi untuk keyword argument 
    return "Halo, " + nama + "!" + pesan

print(greeting(pesan="Selamat sore!", nama="Dicoding"))
    

print("Var-positional")
#menampng jumlah argumen posisi yang bervariasi 
#saat pemanggilan fungsi 

def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total 

print(hitung_total(1,2,3))
# print(hitung_total(1, 2, 3, 4, 5, 6, 7, 8))


print("Var - keyword")

def cetak_info(**kwargs): #kwargs akaan mengumpulkan semua pasangan key value 
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info
    # sepertinya harus dalam 1 line vertikal seperti var info return viewnya di info juga 

# print(cetak_info(nama="Dicoding", usia = "17", pekerjaan= "Python programer"))
print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer", tempat_lahir="Bandung", lulusan="ITB"))

#setelah key akan ditambahkan titik 2 dan dipisahkan komma setiap value 


# fungsi anonim (lambarada expression)
# membuat fungsi tanpa mendeklarasikan def

# def func(agrs):
#     return ret_val
# menjadi
# lambda args: ret_val  ret_val adalah nilai yang di return 

# contoh mencari luas persegi panjang menggunakan lambda
#args itu untuk menyimpan nilai 

mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,10))

# argumen nya adalah panjang dan lebar 


print("===== variabel global ====")

a = 10

def add(b):
    result = a+b
    return result

bilanganPertama = add(20)
print(bilanganPertama)

print("===== variabel lokal ====")


def add(a, b):
    lokal_var = 5
    result = a+b-lokal_var
    return result, lokal_var # gabisa di print tadi karena tidak di defenisikan

bilanganPertama, lokal_var = add(10,20)
print(bilanganPertama)
print(lokal_var)


print("===== Quiz fungsi  ====")


"""
TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""

# TODO: Silakan buat kode Anda di bawah ini.

def minimal(a,b):
	if a > b:
		return b
	else:
		return a

angka1 = 10
angka2 = 5
nilai_terkecil = minimal(angka1,angka2)
print(nilai_terkecil)

# fungsi adalah blok kdoe yang menerima input melakukan pemrosesan
# prosedur adalah deretan intruksi yang jelas keadaan awall dan keadan akhirnya 
# parameter adalah variabel yang menyimpan nillai 

# value nya adalah argumen fungsi 













