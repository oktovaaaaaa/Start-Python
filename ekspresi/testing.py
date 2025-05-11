# est fixture merepresentasikan persiapan yang dibutuhkan untuk melakukan satu pengujian atau lebih serta proses pembersihannya (cleanup). Beberapa contohnya adalah menyiapkan basis data pengujian, direktori pengujian, atau mengaktifkan sebuah proses server.
# Test case adalah sebuah unit dari pengujian ketika ia mengecek sejumlah respons dari sebagian kelompok masukan. Library unittest menyediakan basis class dan TestCase yang akan digunakan untuk membuat kasus pengujian baru.
# Test suite adalah sebuah koleksi dari kasus-kasus pengujian, koleksi dari test suite itu sendiri, atau gabungan keduanya. Hal ini berguna untuk mengumpulkan pengujian-pengujian yang akan dieksekusi bersama.


# Test runner adalah komponen yang akan mengatur (orchestrates) eksekusi dari pengujian-pengujian dan menyediakan keluaran untuk pengguna. Dalam hal ini, runner dapat menggunakan tampilan grafis, tampilan tekstual, atau mengembalikan nilai spesial yang menyatakan hasil dari pengujian.

import unittest


class TestStringMethods(unittest.TestCase): # turunan (subclass) dari class unittest 
    def test_strip(self):
        self.assertEqual("www.dicoding.com".strip("c.mow"), 'dicoding')

    def test_isalnum(self):
        self.assertTrue("c0ding".isalnum())
        self.assertFalse("c0d!ng".isalnum())
        
    # def test_isalnum(self):
    #    self.assertTrue('c0d1ng'.isalnum())  # ini akan berhasil
    #    self.assertTrue('c0d!ng'.isalnum())  # ini akan gagal

    def test_index(self):
        s = "dicoding"
        self.assertEqual(s.index("coding"), 2)
        # cek s.index galgal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index("decode")
            
            #awalan test inni  aturan wajib untuk menginformasikan ke test runner mempresentaisikan test yanng di operasikan 

#pada setiap metodde pengujian dilakukan dengan pemanggilan assert pada metode test_strip pengecekan kesamaan menggunakan assertequal untuk memasikan ww.dicoding sama dengan dicoding 
if __name__ == "__main__":
    # test runner
    unittest.main()

# Pada metode test_isalnum pengecekan bahwa fungsi bernilai benar (True) dilakukan dengan assertTrue untuk memastikan jika 'c0d1ng'.isalnum() bernilai benar, yakni ‘cOd1ng’ adalah betul bertipe alfanumerik. Kemudian juga ada pengecekan bahwa fungsi bernilai salah (False) dengan assertFalse untuk memastikan jika 'c0d!ng'.isalnum() betul bernilai salah karena ada karakter yang bukan alfanumerik yaitu ‘!’.
# Pada metode test_index pengecekan kesamaan dilakukan seperti sebelumnya dengan menggunakan assertEqual bahwa pencarian substring coding menempati index sama dengan 2. Kemudian juga ada pengecekan bahwa ValueError akan dibangkitkan dengan menggunakan assertRaises(ValueError), jika pencarian index tidak berhasil ditemukan pada string yang sudah ditentukan.
# Pada bagian terakhir kode, ada pemanggilan unittest.main() untuk mulai menjalankan test.

#outputnya ada (...) bahwa ketiga fungsi berhasil melewati test 
# berlangsung selama 0,001 detik 
# (ok)  menandakan sukses 

