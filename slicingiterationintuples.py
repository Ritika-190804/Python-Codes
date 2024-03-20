#basics of tuples:-
a="apple","mango","banana",1,67,1.23
print(type(a))
print(a)
b=("ironman",)
print(type(b))

#slicing in tuples:-
a=("OnePlus","Vivo","Redmi","Samsung","Nokia")
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[1::2])
print(a[::-1])
print(a[2::-1])

#iteration in tuples:-
a=("one plus","vivo","redmi","samsung","nokia")
#for loop
for i in a:
    print(i)

#along with range & length in for loop:-
for i  in range(len(a)):
    print(a[i])

#along with while loop:-
i=0
while i<len(a):
    print(a[i])
    i+=1

