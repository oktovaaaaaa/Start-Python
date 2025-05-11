# Library Pengolahan Data
# Library pengolahan data bertujuan untuk membantu dalam manipulasi, analisis, dan pemrosesan data. Library ini menyediakan berbagai fungsi dan metode yang memudahkan pengguna untuk melakukan operasi pengolahan data dengan lebih efisien dan cepat.

# tujuan library ini  untuk menyederhanakan tugas" kompleks 

# 1. Pandas

# library populer untuk mengelola data 
# menyesd==diakan struktur data dan alat untuk membantu 
# memanupulasi, membersihkan dan transformasi dan analisis dengan mudah dan efisienn

import pandas as pd

data = { #membuat dataframe dari dictionary 
    'Nama': ['Jhon', 'Jane', 'Bob', 'Alice'],
    'Usia': [25,30,22,28],
    'Pekerjaan': ['Enginer', 'Teacher', 'Designer','Doctor']
}

#menampilkan data frame 
df = pd.DataFrame(data)

print(df)


print("+++ Numpy +++++\n")
# 2. Numpy
# package fundamental yang sering digunnakan untuk 
# scientific computing pada python. menyediaan obbjek array 
# ,multiidimensi berbagai jenis objek lainnnya seperti masked matris dan sebagainya 

# termasuk library eksternal 

import numpy 

matriks = numpy.array([[1,2,3],[4,5,6],[7,8,9]]) #mengubah nested menjadi array menggunakan fungsi array()
print(matriks)

# 3.matplotlib

# library untuk visualisasi data. Matolotlib termasuk jenis library eksternal 

# print("======= matplotlib ========")

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,4,6,8,10]

#membuat plot garis 
# plt.plot(x,y)

# #menambahkan judul dan label sumbu 
# plt.title("Contoh plot Garis")
# plt.xlabel("Sumbu X")
# plt.ylabel("Sumbu Y")

# #meanmpilkan plot
# plt.show()

# 4. Seaborn 

# untuk visualisasi data sama seperti matploltib
# bahkan dii bangun berdasarkan library matplotlib

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips') # membuat data set dari seaborn ini adalah dattaset bawan sudah ada dtanpa menginput data  

#contoh plot histogram 
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram Total bill')
plt.xlabel('Total bill')
plt.ylabel('Frequncy')
plt.show()