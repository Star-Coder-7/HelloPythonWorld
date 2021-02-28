parrot = "Norwegian Blue"
print(parrot)
print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[:6])
print(parrot[-14:-8])

print(parrot[0:6:2])   # Nre
print(parrot[0:6:3])   # Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])











