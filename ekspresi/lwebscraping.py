# Library web scraping adalah jenis library untuk membantu pengguna
# mengumpulkan data dari halaman web. Proses ini disebut sebagai
# “web scraping” atau “web crawling”. Anda bisa menggunakan 
# fungsi dan metode pada library ini untuk mengekstraksi 
# dari situs web dan menyimpannya dalam format yang 
# diakses dan digunakan dalam analisis atau aplikasi lainnya. 

# library untuk melakukan web scraping adalah sbg berikut 
# 1. Beautifulsoup
# untuk mengambil data dari halaman web dan mengekstrak informasi yang diperlukan 
# code :
from urllib.request import urlopen
from bs4 import BeautifulSoup


#pengambilan konten 
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")

#membuat objek BeutifulSoup
soup = BeautifulSoup(html, "html.parser")

#menjalankan judul halaman 
print(soup.title)

print(" 2. urlib")
# Urllib adalah library bawaan dari Python yang bertujuan untuk scraping
# konten dari sebuah website. Penggunaan urllib berbeda dengan 
# beautifulsoup. Bisa dikatakan bahwa cara penggunaan urllib sedikit 
# kompleks dibandingkan beautifulsoup. Kode di bawah adalah contoh 
# untuk memulai proses scraping pada situs dengan domain python.org dan
# menampilkan isi dari tag title dari situs tersebut.

from urllib.request import urlopen

#pengambilan konten 
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")

#mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")

#menegekstrak dan mencetak judul halaman 
title = html[start_index:end_index]
print(title)
