#A= "OOTD.YOLD.ASAP.BRB.GTG.OTW"
#1.Write a program to separate the following string
#into comma(,) separated values.

a="OOTD.YOLD.ASAP.BRB.GTG.OTW"

b=a.split(".")
print(b)

#2.write a program to sort strings alphabetically in python.

a=input("enter anything here: ")

b=sorted(a)
print(b)

#3.write a program to remove a given character from a string.
a="hello"
b=a.replace("e","")
print(b)

#4.
#Z="F.R.I.E.N.D.S"
#write a program to remove dot(.) from the following string

z="F.R.I.E.N.D.S"
B=z.replace(".","")
print(B)

#5.write a program to check the number of occurence of a
#substring in a string.
a="she sells seashells on the sea shore"
b=a.count("sea")
print(b)
