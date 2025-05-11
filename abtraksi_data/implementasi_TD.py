x = 6
print(type(x))

x= 6.0
print(type(x))


x = 1+2j
print(type(x))

print("===========================================")

var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))


print("===========================================")


x = True 
print(type(x))

x = False 
print(type(x))

print("===========================================")


x ='dicoding'
print(type(x))

print("===========================================")

multi_line = """ aku mau makan permen, tapi permenku habis di makan kak moncan.
kemarin kak moncan minta 1 tapi aku kasih 100 """

print(multi_line)

print("===========================================")

x = 'dicoding'  """ index pertama diminta di print """
print(x[0])


print("===========================================")

""" string pada python tidak dapat diuubah  """
""" 
x = 'dicoding'
x[0] = 'f'
 """

print("===========================================")

""" metode indexing dan sicling """
x = 'dicoding'
print(x[2:])

print("========= format string =====================")
name = 'Oktova Samosir'
print(f"Hello, nama saya {name}")


print("============ %-formating=====================")
name = "Oktova Samosir"
print("Nama saya %s" %(name))

print("============ str.format() =====================")

name = "Oktova Samosir"
print("Nama saya {}". format(name))



