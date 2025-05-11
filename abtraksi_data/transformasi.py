# upper() -> untuk mengubah semua lowercase besar menjadi uppercase 

kata = 'oktova'
kata = kata.upper()
print(kata)

print("===========lower()==================")
kata = 'MONCAN'
kata = kata.lower()
print(kata)

print("===========rstrip()===============")
print("Oktopaaaa   a         ".rstrip())
# yang di hapus spasi setelah a yang terakhir

print("==========lstrip()==========")
print("                           oktova".lstrip())

print("==========strip=========")
print("            okrova               ".strip())


print("==menghilangkan karakter====")
kata  = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

print("==mencari kata dan mengembalikan nilai true===")
print('dicoding indonesia'.startswith('dicoding'))
# mencari nilai awal apakah sama 

print("=endswith()========")
print('dicoding indonesia'.endswith('dicoding'))


print("===memisah dan menggabung string ==")
print(''.join(['okto dan ','moncan','!']))



print("===menambahkan whitespace===")
print('123'.join(['dicoding','indonesia']))

print("==========split()=============")

print('dicoding indonesia!'.split())

print(""" halo, namaku oktova, aku suka kak moncan karena rambut kak moncan lucyuuuuu kaya  mantan aku bwahahahaha """.split('\n'))

print("==========replace()=============")
string = "ayo belajar dari kak moncan"
print(string.replace("belajar","ayo"))
# menganti kata pertama menjadi kata kedua


# pengecekan string
print("==========isupper()==========")
# jika ada satu hurf saja lowercase maka akan False
kada = 'dicoding'
print(kata.isupper())

print("==========islower()==========")

kata = 'dicoding'
print(kata.islower())
# if evry text lowecrase  true maka mengembalikan true 

print("==========isalpha()==========")
# send true if every text huruf alphabet
kata ='dicoding'
print(kata.isalpha())

print("==========isalnum()==========")
# jika huruf atau angka saja atau keduanya maka mengembalikan nilai True
kata = 'dicoding123'
print(kata.isalnum())

print("==========isdecimal()==========")
print('123'.isdecimal())
# true jika hanya angka

print("==========isspace()==========")
print('                 '.isspace())
# mengirimkan true jika whitespace like spasi enter or tab


print("==========istitle()==========")
# mengirim true jika huruf kapotal pada setiap kata pertamanya

print('Dicoding Indonesia'.istitle())



# Formating pada string 

# zfill utk menambahkan o di depan sebuah string denganpanjang tertentu 
# membantu memastikan memiliki  panjang tetap

print("==========zfill()==========")

teks = 'Code'
tambah_number = teks.zfill(5)
print(tambah_number)

print("==========rjust()==========")
print('Dicoding' .rjust(20))

print('Dicoding'.rjust(20, 'i'))

print("==========ljust()==========")
print('Dicoding'.ljust(20,'o'))

print("==========center()==========")
print('Dicoding'.center(10,'_'))



print("========= Sring Literals ==========")
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")


print(r'Dicoding\tIndonesia')
""" code (\t) ikut tercetak karena didalam input teks """








