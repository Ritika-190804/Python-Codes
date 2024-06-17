#SET FUNCTIONS:-

a={"Ironman","Hulk","Captain America","Thor"}

# 1.add:-
a.add("spiderman")
print(a)

# 2.pop:-
#a.pop()
#print(a)

# 3.remove:-
a.remove("Thor")
print(a)

# 4.discard:-
a.discard("Hulk")
print(a)

# 5.copy:-
b=a.copy()
print(b)

a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","wonder-woman"}
c={"Hulk","Thor"}

# 6.isdisjoint:-
print(a.isdisjoint(c))

# 7.issubset:-
print(c.issubset(a))

# 8.issuperset:-
print(a.issuperset(c))

# 9.update:-
a.update(c)
print(a)

# 10.clear:-
a.clear()
print(a)

a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-woman"}
c={"Hulk","Thor","Spiderman"}

# 11.union:-
print(a.union(c))

# 12.difference:-
#print(a.difference(c))

# 13.difference update:-
#a.difference_update(c)
#print(a)

# 14.intersection:-
print(a.intersection(c))

# 15.intersection update:-
a.intersection_update(c)
print(a)

# 16.symmetric difference:-
x=a.symmetric_difference(c)
print(x)

# 17.symmetric difference update:-
a.symmetric_difference_update(c)
print(a)
