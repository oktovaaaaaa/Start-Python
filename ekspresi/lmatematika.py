import math

print(math.sqrt(25))
print(math.pi)


# 1. Fungsi Akar & Pangkat
# Fungsi	Deskripsi	Contoh
# math.sqrt(x)	Menghitung akar kuadrat dari x	math.sqrt(25) → 5.0
# math.pow(x, y)	Menghitung x pangkat y	math.pow(2, 3) → 8.0
# math.exp(x)	Menghitung e^x	math.exp(2) → 7.389
# 2. Fungsi Logaritma
# Fungsi	Deskripsi	Contoh
# math.log(x)	Logaritma natural (basis e)	math.log(10) → 2.30
# math.log10(x)	Logaritma basis 10	math.log10(100) → 2.0
# math.log2(x)	Logaritma basis 2	math.log2(8) → 3.0
# 3. Fungsi Trigonometri
# Fungsi	Deskripsi	Contoh
# math.sin(x)	Sinus dari x (radian)	math.sin(math.pi/2) → 1.0
# math.cos(x)	Cosinus dari x (radian)	math.cos(math.pi) → -1.0
# math.tan(x)	Tangen dari x (radian)	math.tan(math.pi/4) → 1.0
# math.degrees(x)	Konversi radian ke derajat	math.degrees(math.pi) → 180.0
# math.radians(x)	Konversi derajat ke radian	math.radians(180) → 3.14159
# 4. Fungsi Pembulatan
# Fungsi	Deskripsi	Contoh
# math.ceil(x)	Membulatkan ke atas	math.ceil(4.3) → 5
# math.floor(x)	Membulatkan ke bawah	math.floor(4.7) → 4
# math.trunc(x)	Menghapus desimal tanpa pembulatan	math.trunc(4.9) → 4
# 5. Fungsi Faktor & Kombinasi
# Fungsi	Deskripsi	Contoh
# math.factorial(x)	Menghitung faktorial dari x	math.factorial(5) → 120
# math.gcd(x, y)	Menghitung FPB dari x dan y	math.gcd(8, 12) → 4
# 6. Konstanta Penting
# Konstanta	Deskripsi	Nilai
# math.pi	Nilai π (pi)	3.141592653589793
# math.e	Bilangan Euler (e)	2.718281828459045
# math.tau	2π (lingkaran penuh)	6.283185307179586
# math.inf	Tak hingga	math.inf
# math.nan	Not-a-Number	math.nan
# Contoh Penggunaan
# python
# Copy
# Edit
# import math

# # Akar kuadrat
# print(math.sqrt(16))  # Output: 4.0

# # Pangkat
# print(math.pow(2, 3))  # Output: 8.0

# # Logaritma
# print(math.log10(100))  # Output: 2.0

# # Trigonometri
# print(math.sin(math.radians(30)))  # Output: 0.5

# # Pembulatan
# print(math.ceil(4.2))  # Output: 5
# print(math.floor(4.9))  # Output: 4

# # Faktorial
# print(math.factorial(5))  # Output: 120