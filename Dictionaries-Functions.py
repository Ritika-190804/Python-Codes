student = {"name": "John", "class": "6th", "roll_no": 23}
# get:-
x = student.get("name")
print(x)

# item:-
a = student.items()
print(a)

# keys:-
b = student.keys()
print(b)

# values:-
c = student.values()
print(c)

# copy:-
d = student.copy()
print(d)

# setdefault
x = student.setdefault("roll_no", 24)
print(x)

# update:-
student.update({'name': 'John', 'name': 'Ritika'})
print(student)

# pop:-
e = student.pop('name')
print(e)

# popitem:-
p = student.popitem()
print("removed", p)
print(student)

# clear:-
q = student.clear()
print(q)
