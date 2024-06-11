# tabel kebenaran (Logika Bolean)
# not and or  xor

print("\n*****Logika Not****")
x = False
y = not x
print("nilai dari x :", x)
print("nilai dari y :", y)



print("\n*****Logika And****")
x = False
y = False
z = x and y
print(x, "and", y, "=", z)

x = True
y = False
z = x and y
print(x, "and", y, "=", z)

x = False
y = True
z = x and y
print(x, "and", y, "=", z)

x = True
y = True
z = x and y
print(x, "and", y, "=", z)


print("\n*****Logika OR****")
x = False
y = False
z = x or y
print(x, "or", y, "=", z)

x = True
y = False
z = x or y
print(x, "or", y, "=", z)

x = False
y = True
z = x or y
print(x, "or", y, "=", z)

x = True
y = True
z = x or y
print(x, "or", y, "=", z)
