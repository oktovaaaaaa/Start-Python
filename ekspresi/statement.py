# if foo == 'blah':
#     do_blah_thing()
#     do_one()
#     do_two()
#     do_three() #disarankan seperti ini tidak bertingkat 
    
#     if foo == 'blah': do_blah_thing()
# do_one(); do_two(); do_three()

# if foo == 'blah': do_blah_thing()
# for x in lst: total += x
# while t < 10: t = delay()

# ini tidak bisa karena bertingkat, jika if else try etc tidaddk
# bertingkat itu masih bisa jalan 
# if foo == 'blah': do_blah_thing()
# else: do_non_blah_thing()
# try: something()
# finally: cleanup()
# do_one(); do_two(); do_three(long, argument,
#                              list, like, this)
# if foo == 'blah': one(); two(); three()

print("Penggunaan trailing commas")

# koma dibagian akhir 
# bersifat opsional dan kadang bersifat wajib saat kita 
# membua tvariabel menggunakan tipe tuple denfan satu elemen 
# untuk menghindari penghapusa atau pembersihan 

# coontoh benar
# FILES = ('setup.cfg',)

#contoh yang salah 
# FILES = 'setup.cfg',#pola yang disarankan  adalah meletakkan nilai atau string 
#pada sebuah baris baru 

# Tidak umum jika Anda menempatkan trailing
# comma pada baris letak Anda menutup kurung/kurawal
# /siku seperti di bawah ini, kecuali
# dalam tuple dengan satu elemen, seperti yang dijelaskan di atas.

#disarankan seperti ini:
# cara amenutup kurung kurawal

# FILES = [
#     'setup.cfg',
#     'tox.ini',
# ]
# initialize(FILES,
#            error=True,
#            )

#tidak disarankan seperti ini:
# FILES = ['setup.cfg', 'tox.ini',]
# initialize(FILES, error=True,)

# print("Anotasi Fungsi")
# fitur yang memungkinkan menambahkan informasi tambahan tentang parameter
# dan return velue dari sebuah fungsi 

# penggunaan anotasi fungsi menggunakan titik dua(:)
# dan menggunakan spasi untuk arah panah (->) type hints PEP 484

# Yes:
#     def munge(input: str):
#         pass
#     def munge() -> str:
#         pass
    
# No:
#     def munge(input:str):
#         pass
#     def munge()->str:
#         pass
#     def munge()->str:
#         pass
    
    #parameter dan return harus bertipe string kita bisa menentukan dgn itpe lain like int ddan float
    # saat membuat fungsi menggabungkan notasi dengan nilai parameter menggunakan spasisebelum dan sesudah (=)
    
def LuasPersegiPanjang(panjang: int = 2, lebar: int = None): # int = 2 akan memberikan nilai default yaitu  2
    pass

print("======= contoh =======")

def LuasPersegiPanjang(panjang: int = 2, lebar: int = None):
    luas = panjang*lebar
    return luas

luas_satu = LuasPersegiPanjang(lebar=2)
print(luas_satu)


print("Contoh baru")

#tanpa anotasi bahwa parameternya menandakan keyword argumen atau
# nilai defaulhindari penggunaan spasi di antara (=)

# Yes :
#     def LuasPersegiPanjang(panjang=2, lebar=None):
#         luas = panjang*lebar
#         return luas
    
# No :
#     def LuasPersegiPanjang(panjang = 2, lebar=None):
#         luas = panjang**lebar
#         return luas
    
    
#     #anotasi untuk menambahkan informasi tambahan tentang parameter dan return 
    