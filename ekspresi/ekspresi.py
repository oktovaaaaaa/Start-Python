# 4x - 7=5  
# 4x - 7 adalah ekspresi dan 4,7,5 adalah suku bilangan 

# ekspresi adalah kombinasi seperti dalam matematika
# seperti simbol angka variabel operator dll


# operan seperti penjumlahan (+), pengurangan (-), perkalian (*), modulus (%), dan sebagainya.


print("======== operan =======")

x = 10 
y = 2
result = x - y
print(result)

print("======== operan =======")

angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf
# angka aakn di print pertama karena angka + huuruf begitu juga sebaliknya
print(gabung)

print("======== operan =======")

learn = ['P', 'Y', 'T', 'H', 'O', 'N']
replikasi = learn * 2

# akan memprint  ['P', 'Y', 'T', 'H', 'O', 'N'] sebanyak 2 x
print(replikasi)

# jenis jenis ekspresi 
# arity dan operator 

# Biner

# (x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), (x % y), (x == y), (x != y).

# Uner

# (x += 1), (x-=1), (not x).

# biner memiliki 2 operan tetapi uner memiliki 1 operan 

print("========= uner ==========")

a = True 
a = not a
print(a)


b = 6
b -= 1
print(b)

c = 6
c += 1
print(c)

d = 10
print(-d)


# Jenis	Contoh
# Ekspresi aritmetika: 

# <numerik> <operator> <numerik> = <numerik>

# 2 + 2 = 4, 2 - 2 = 0

# Ekspresi relasional: 

# <numerik> <operator> <numerik> = <boolean>

# 3 < 10 = True, 1 > 10 = False

# Ekspresi logika: 

# <boolean> <operator> <boolean> = <boolean>

# True or False = True

print("========= 0 ==========")


print(2+2)
print(3<10)
print(True or False)

print("========= operator aritmatika ==========")

x = 11
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x * y)

print("========= relasional ==========")
# Operator relasional merupakan operator perbandingan antara dua operan 
# yang berupa integer, float, string, ataupun boolean. Hasil akhir dari operator ini adalah nilai bertipe boolean

x = 5
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print("========= relasional ==========")


x = "Dicoding"
y = "andonesia"

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print("========= operator logika ==========")
# Operator logika merupakan jenis operator untuk melakukan operasi logika dengan kedua operannya bertipe boolean.

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("========= operator logika ==========")


print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("========= operator logika ==========")
print(not True)
print(not False)




print("========= Operator Assignment ==========")
""" +=

-=  selesai sama dengan adalah yang dikalikan atau ditambahkan dll 
contooh x += 16 = x + y = 16 dan -= sama x - y = """

# +=
x = 11
x += 5
print(x)

# -=
x = 11
x -= 5
print(x)

# *=
x = 11
x *= 5
print(x)

# /=
x = 11
x /= 5
print(x)

#%=
x = 11
x%= 5
print(x)

x = 11
x += 5
print(x)


x = 11
x = x + 5
print(x)
