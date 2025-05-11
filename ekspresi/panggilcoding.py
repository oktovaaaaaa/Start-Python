# library parser

# untuk menguraikan code python menjadi struktur data yang dapat diproses
# dan analisis dan dapat menggukaan Getopt atau Argparse

# Argument parser bermanfaat jika kita ingin membuat program atau skrip kecil yang langsung menerima parameter pada saat pemanggilan program. Hal ini biasa digunakan dalam pemanggilan aplikasi atau skrip di CLI/terminal *nix-based, misalnya Linux dan MacOS. Contoh perintah dimaksud adalah berikut.

# python panggildicoding.py -o

# Contoh tindakan menambahkan Argument yang bersifat opsional/tidak wajib dengan
# menggunakan ArgParse adalah berikut.

""" import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
args = parser.parse_args()

if args.output:
    print("Halo, ini merupakan sebuah output dari panggilcoding.py")
"""

# menampilkan argument bersifat wajib 
#modifikasi berkas panggilcoding.py spt berikut 

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('-n', '--nama', required=True, help="Masukkan nama anda")
# args = parser.parse_args()


# print("Terimakasih telah menggunakan panggilcoding.py " +args.nama)


# Quiz =

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan nama anda")
parser.add_argument('-t', '--tanggallahir', required=True, help="Masukkan tanggal lahir anda (DD-MM-YYYY)")
args = parser.parse_args()


print("Terimakasih telah menggunakan panggilcoding.py pada tahun" +args.tanggallahir, ", kakak" +args.nama)

