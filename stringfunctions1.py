#endswith():-

a="Harry Potter"
print(a.endswith("r"))
print(a.endswith("t",6,11))

#startswith():-
a="Harry Potter"
print(a.startswith("H"))
print(a.startswith("P",6,9))

#swapcase():-
a="ritika roy"
print(a.swapcase())


#strip():-
a="*******i am a good girl......."
print(a.strip("*"))


#split():-
a="OOFD#BRB#OMW#TB"
b="hello.my name is ritu.iam persuing BCA"
print(a.split("#"))
print(b.split("."))


#ljust():-
a="Devansh Roy"
x=a.ljust(20)
x=a.ljust(20,"*")
print(x,"is my brother name")


#rjust():-
a="Raunak Roy"
x=a.rjust(20)
print(x,"is my fighter name")


#replace():-
a="my name  is tina.tina is a good girl"
print(a.replace("tina","riti"))


#rindex():-
a="Harry Potter and the prisoner of azkaban"
print(a.rindex("prisoner"))


#rfind():-
a="Harry Potter and the Goblet of Fire"
print(a.rfind("Harry"))