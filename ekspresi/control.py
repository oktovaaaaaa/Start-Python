print("======= control flow =====")

# perintah yang dimana ada perintah memulai dan mengakhiri /
# like loopinng

# Dalam pemrograman, sebuah kode program dapat berjalan 
# berdasarkan kondisi tertentu. Maknanya, Anda dapat
#  memberikan instruksi berdasarkan "Jika-maka" (if-else). 


ketersediaan = "Daging ayam"

if ketersediaan == "Daging ayam":
    print("Ibu akan memasak ayam")
else:
    print("Ibu membeli tempe dan memasak tempe")


print("======= control flow =====")

score = 100

if score == 100:
    print("Nilai Anda sempurna!")

print("======= control flow =====")

x = ""

if x:
    print("Ini True")
    
print("======= control flow =====")

score = 100

if score == 100: print("Nilai Anda sempurna!")
# tidak di anggap kesalahan setelah variabel baru print di line yang sama 


print("======= control flow =====")

tinggi_badan = 120

if tinggi_badan >=160:
    print("Anda boleh menaiki roller coaster")
else:
    print("Anda tidak diperbolehkan menaiki roller coaster")

print("======= control flow =====")


nilai = int(input("Masukkan nilai anda: "))

if nilai>=80:
    print("selamat anda mendapat nilai A")
elif nilai>=70:
    print("Selamat anda mendapatkan B")
elif nilai>=60:
    print("anda mendapatkan nilai c")
else:
    print("waduh masa itu aja gabisa")
    print("lu belajar lagi sono ")

print("======= control flow =====")

nilai = int(input("Masukkan nilai anda:"))
perilaku = 'tidak baik'

if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")

   print("======= Ternary OPERATOR =====")

lulus = True
print("selamat") if lulus else print("perbaiki")

print("======= Ternary OPERATOR =====")


lulus = True
if lulus:
    print("Selamat") 
else:
    print("Perbaiki")

print("======= Ternary OPERATOR =====")


lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan)

print("======= Ternary OPERATOR =====")

lulus = True
if lulus:
    print("Selamat, anda lulus")
else:
    print("Perbaii, anda belum lulus")

print("======= Ternary OPERATOR =====")

for i in range(1,10,2):
    print(i)
#end tidak termasuk
    # 1 sebagai start, 10 sebagai end dan 2 langkah"nya 

print("======= While =====")

counter = 1
while counter <= 5:
    print(counter)
    counter +=1

    print("======= While =====")
""" counter = 1
while counter <=5:
    print(counter)
    karena nggak di incrementkan jadi melakukan looping tanpa henti   """

print("======= for 2 =====")
# melakukan perulangan yang luar dulu baru perulangan yang dalam 
for i in range(1,3):
    for j in range(1, 3):
        print(i,j)
# start 1 dan end 3
        # tidak sampai 3 karena end (3) tidak ditampilkan 

print("======= BREAK =====")

for i in range(2):
    print("Perulangan luar:",i)
    for j in range(10):
        print("Perulangan dalam",j)
        if j == 1:
            break


print("======= BREAK =====")

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))


print("======= Continue =====")

for huruf in 'Dico ding':
    if huruf == ' ':
        continue #karena disaat huruf nya ' ' maka akan dilanjut
    print('Huruf saat ini: {}'.format(huruf))

print("======= Else setelah For =====")

numbers = [1,2,3,4,5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan ! program berhenti")
        break
else:
        print("Angka tidak ditemukan")

print("======= Else setelah while =====")

count = 0   

while count < 3:
    print("Dicoding Indonesia")
    count +=1
else:
    print("Blok else di eksekusi karena kodndisi pada while salah (3<3== False).")
# dicoding 3 x lalu  print blok


print("======= Else setelah while =====")


n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")
    # 9,8 aja ditampilkan karena 
    # di eksekusi dulu  bar di print dan saat 7 langsung di break 
    # tanpa di eksekusi 

print("======= PASS =====")

x = 10

if x > 5:
    pass 
else:
    print("Nilai x tidak memenuhi kondisi")
""" pass adalah jika tidak terpenuhi maka tidak melakukan apapun """

print("======= List Comprehension =====")
angka = [1,2,3,4]
pangkat = []
for n in angka:
    pangkat.append(n**2) #append untuk menambahkan nilai baru ke perangkat 
print(pangkat) #perkara spasi doang outputnya berubah kwkw

# expression merupakan ekspresi yang akan dijalankan seiring perulangan bernilai benar.

print("======== QUIZ ===========")
evenNumber = [i for i in range(0,501,2)]
print(evenNumber)



# Ternary Operators
# Ternary operators termasuk conditional expressions pada Python.
#  Conditional expressions adalah bentuk ekspresi yang bertujuan
#  untuk mengevaluasi kondisi dan mengembalikan nilai berdasarkan
#  hasil evaluasinya. Anda bisa asumsikan bahwa ternary operators ini
#  merupakan versi one-liner dari if dan else. 

""" 
Kondisi merupakan ekspresi yang akan dievaluasi dan
menghasilkan nilai true atau false. Selama hasil evaluasi bernilai
true, program akan terus berjalan hingga menghasilkan nilai false. """

