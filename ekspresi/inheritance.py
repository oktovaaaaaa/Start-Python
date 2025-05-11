# inheritance, kita dapat membuat class baru dengan 
# menggunakan kelas innduk yang sudah ada 

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek 
        self.kecepatan = kecepatan
        
        def tambah_kecepatan(self):
            self.kecepatan += 10
            
            
class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

            
mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)


# kelas mobil sport 

mobil_sport_1 = MobilSport("Hitam", "OktoSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)


print(" Overridde ")

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 20

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)


print("===== super =====")

# menggunakan metode atau atribut tanpa menulisakan semua kode 
# dari kelas induk, menghindari kelas berulang 

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

# def = method 



class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

class Cat(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)

    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"  # Pastikan ini diindentasi

    def suara(self):
        return "meow!"  # Dan ini juga diindentasi

myCat = Cat("Neko", 3, "Persian")
print(myCat.deskripsi())


#code saya :

class Animal:
  def __init__(self, name, age, species):
    self.name = name
    self.age = age 
    self.species = species
class Cat(Animal):
  def __init__(self, name, age, species):
    super(). __init__(name, age, species)
  def deskripsi(self):
  return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
  
  def suara(self):
  return "meow!"
myCat = Cat("Neko", 3, "Persian")
print(myCat.deskripsi())
  