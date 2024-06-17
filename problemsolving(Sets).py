#write a program to find max and min in a set:-
a={9,7,78,56,34,21}
minimum=min(a)
maximum=max(a)
print("the minimum value is :",minimum)
print("the maximum value is :",maximum)


#write a program to find common elements in three lists using sets:-
a={56,90,43,71,89}
b={21,34,90,43}
c={43,90,71}

print("the common elements in three lists",set(a) & set(b) & set(c))


#write a program to find difference between two sets:-
a={2,3,4,5,6}
b={9,8,6,4,3}

print(b.difference(a))


#write a python program to remove an element from a set if it is present in a set:-
a={6,7,8,4,5}
a.discard(4)
print(a)


#write a python program to check if a set is a subset of another set:-
a={1,2,3,4,5,6}
b={2,3,4}

print(b.issubset(a))