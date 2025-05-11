class Kalkulator:
    def __init__(self, _i):
        self.i = _i

    def tambah(self, _i):
        return self.i + _i

    def kurang(self, _i):
        return self.i - _i
    
    
    # Membuat objek Kalkulator dengan nilai awal 10
kalkulator = Kalkulator(10)

# Memanggil metode tambah dengan nilai 5
hasil_tambah = kalkulator.tambah(5)
print(f"Hasil penjumlahan: {hasil_tambah}")  # Output: Hasil penjumlahan: 15

# Memanggil metode kurang dengan nilai 3
hasil_kurang = kalkulator.kurang(3)
print(f"Hasil pengurangan: {hasil_kurang}")  # Output: Hasil pengurangan: 7