a = ("OnePlus", "Nokia", "Redmi")

print(a.count("Redmi"))

print("the index of redmi is",a.index("Redmi"))

print("before conversion", type(a))

a = list(a)
print("after conversion", type(a))
a = a.append("Samsung")
print(a)
a = tuple(a)
print(type(a))
print(a)
