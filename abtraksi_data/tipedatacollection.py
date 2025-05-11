""" list python tidak mengharuskan tipe data yang sama, sedangkan array sebaliknya  """

""" array didalam python bisa memilii tipe yang berbeda dalam 1 index atau array  """
""" index selalu dimulai dari 0
 """

""" contoh kode dalam python: var = [1, "dicoding, True, 7.9"] """

""" contoh kode dalam java: int[] myArray = {1,2,3,4,5}; """


print("=============type list==================")
x = [1, 3.6, "Oktova samosir"]
print(type(x))

print("=============mempriint index=================")

x = [1,"okto", True, 1.00]
print(x[2])

print("=============mempriint index=================")
x = [1, 3.3, "Okto"]
x[0] = "indonesia"
print(x)

print("=============mempriint index=================")
x = ["Laptop", "mouse", "kabel", "microphone", "moncan"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])
