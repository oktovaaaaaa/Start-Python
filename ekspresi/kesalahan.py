# Kesalahan sintaks (syntax errors) adalah jenis kesalahan yang terjadi ketika Python tidak mengerti perintah Anda.
z=0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai nol.")

print("===eror 2==========")

var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}") #dieksekusi saat terjadi penngecualian
except KeyError:
    print("Key tidak ditemukan.") # akan mengeksekusi jika terjadi pengecualian
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.") # akan mengeksekusi jika tidak terjadi pengecualian
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.") #mengeksekusi jika semua pernyataan sudah terjadi 

# Pengecualian (Exceptions)
# Pengecualian adalah kesalahan yang terjadi ketika Python mengerti 
# perintah Anda, tetapi mendapatkan masalah saat mengikutinya. Umumnya,
#  pengecualian bisa terjadi ketika aplikasi sudah mulai beroperasi.

#    dictionary merupakan tipe data yang melibatkan key-value.  

# atau tidak normal yang terjadi saat program sedang dieksekusi yang mengganggu alur normal program
#  tersebut. Dengan kata lain, exception adalah cara Python memberi tahu
#  Anda bahwa ada sesuatu yang salah.


print("==========================")

var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)
    