# write a python program to sort a dictionary by value:-
a = {"a": 91, "b": 13, "c": 45, "d": 12, "e": 90}
a = sorted(a.values())
print(a)

# write a python script to print a dictionary
# where the keys are numbers between 1 and 15 and the
# values are square of keys:-

b = {"a": 91, "b": 13, "c": 45, "d": 12, "e": 90}
b = {}
for i in range(1, 16):
    b[i] = i ** 2

print(b)

# write a program to multiply all the items in a dictionary:-
c = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

product = 1
for i in c:
    product *= c[i]

print(product)
# write a python program to sort a dictionary by key:-

d={91:"a",13:"b", 45: "c",12: "d",90: "e"}
d=sorted(d.keys())
print(d)