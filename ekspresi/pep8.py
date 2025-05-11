print("LINT")
# proses pengecekan kode atas kemungkinan terjadinya kesalahan

# yang benar 

FILES = [
    'setup.cfg',
    'tox.ini',
    ]

# initialize(FILES,
#            error=True,
#            )

# yg salah :
#     FILES = ['setup.cfg', 'tox.ini',]
# initialize(FILES, error=True,)

# Yes:
# def munge(input: str):  # Menambahkan informasi parameter bertipe string
#     pass
# def munge() -> str:   # Menambahkan informasi return value bertipe string
#     pass
 
# No:
# def munge(input:str):  # Menambahkan informasi parameter bertipe string
#     pass
# def munge()->str:   # Menambahkan informasi return value bertipe string
#     pass

# Jika kita membuat fungsi yang menggabungkan anotasi dengan 
# nilai parameter, sebaiknya tetap menggunakan spasi sebelum 
# dan sesudah tanda sama dengan (=). Namun, ketika membuat fungsi
# biasa tanpa adanya anotasi, sebaiknya tidak menggunakan spasi
# sebelum dan sesudah tanda sama dengan (=).

# Yes:
# def LuasPersegiPanjang(panjang:int = 2, lebar=None):
#     pass

# Atribut publik tidak menggunakan awalan garis bawah.


# Jika nama sebuah method/variabel publik sama dengan reserved keyword,
# tambahkan akhiran garis bawah. Hindari menyingkat atau mengurangi huruf.
# eg:if, else, while, for, def, return, class, try, except, import, from, as, with, lambda, True, False, None
# 

# Jika Anda berniat untuk mewariskan atau membuat subclass dari kelas dan
# menginginkan sebuah variabel hanya digunakan di kelas utama saja,
# tambahkan awalan dua garis bawah. Ini akan memudahkan Anda karena 
# Python mengenalinya sebagai konvensi kelas, untuk menghindari 
# kemungkinan kesamaan nama atau implementasi.