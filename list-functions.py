a=["Thor","Hulk","Ironman","Captain America","Hulk"]
print(a)
#to find the length of a list
print(len(a))

#to count an occurence of a particular element
print(a.count("Hulk"))

#to add to the list
a.append("spiderman")
print(a)

#to add to a specific location
a.insert(2,"vision")
print(a)

#to remove from a list
a.remove("Hulk")
print(a)
a.remove("spiderman")
print(a)

#to remove from a certain location
print(a.pop(2))
print(a)

#to create a copy of list:-
b=[]
print(b)
b=a.copy()
print(b)

#to access an element:-
print(a.index("Hulk"))

#to entend the list:-
c=["vision","superman"]
a.extend(c)
print(a)

#to reverse the list:-
a.reverse()
print(a)

#to sort the list:-
a.sort()
print(a)
d=[4,3,5,8,10,9]
d.sort()
print(d)

#to clear all the data from the list:-
a.clear()
print(a)
d.clear()
print(d)


