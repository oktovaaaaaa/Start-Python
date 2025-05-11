import unittest


def koneksi_ke_db():
    print("[terhubung ke db]")


def putus_koneksi_db(db):
    print("[Tidak terhubung ke db{}]".format(db))


class User:
    username = ""
    aktif = False

    def __init__(self, db, username):
        self.username = username

    def set_aktif(self):
        self.aktif = True


class TestUser(unittest.TestCase):
    # # test case 1

    # def test_user_default_not_active(self):
    #     db = koneksi_ke_db()
    #     dicoding = User(db, "dicoding")
    #     self.assertFalse(dicoding.aktif)  # tidak aktif secara default
    #     putus_koneksi_db(db)
        

    # # test case 2

    # def test_user_is_active(self):
    #     db = koneksi_ke_db()
    #     dicoding = User(db, "dicoding")
    #     dicoding.set_aktif()  # aktifkan user baru
    #     self.assertTrue(dicoding.aktif)
    #     putus_koneksi_db(db)
        
        #test fixture 
    def setUp(self):
        self.db = koneksi_ke_db()
        self.dicoding = User(self.db, "dicoding")
    def tearDown(self):
        putus_koneksi_db(self.db)
 
    # Test Case 1
    def test_user_default_not_active(self):
        self.assertFalse(self.dicoding.aktif)  # tidak aktif secara default
    # Test Case 2
    def test_user_is_active(self):
        self.dicoding.set_aktif()  # aktifkan user baru
        self.assertTrue(self.dicoding.aktif)


if __name__ == "__main__":
    unittest.main()


# Lantas, kita bisa memperbaikinya dengan menerapkan konsep test fixture. Konsep ini merepresentasikan persiapan yang dibutuhkan untuk melakukan satu pengujian atau lebih serta proses pembersihannya (cleanup). 

# Kita akan menggunakan metode bawaan dari class TestCase, yakni metode setUp() dan tearDown().


# Metode setUp(), sesuai namanya, bertujuan untuk mempersiapkan pengujian. Metode ini akan dipanggil untuk menyiapkan tes sehingga pemanggilannya akan dilakukan tiap sebelum metode tes dilaksanakan.
# Metode tearDown() akan dipanggil setiap metode tes selesai dilaksanakan dan bertindak untuk membersihkan, meskipun terjadi kesalahan (exception) pada proses tes.
