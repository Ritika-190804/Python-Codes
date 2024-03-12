#for loop 1.
for i in range(1,6):
    print(i)
# 2.
for i in range(1,6,2):
    print(i)
# 3.
n=7
for i in  range(1,11):
    print(n,"x",i,"=",n*i)

#while loop 1.
n=0
while n<=5:
    print(n)
    n+=1
# 2.
n=0
while n<=5:
    print(n)
    n+=2
# 3.
n=1
a=7
while n<=10:
    print(a,"x",n,"=",n*a)
    n+=1

#while True 1.
while True:
    print("hello")
    break
# 2.
while True:
    num1=int(input("enter a number here: "))
    num2=int(input("enter another number here: "))
    print(num1+num2)
    repeat=input("do you want to stop the program: ")
    if repeat=="yes":
        break

#nested loop 1.
for i in range(1,4):
    for j in range(1,11):
        print(j, end ="")
        print()
#for pattern problem 2.
for i in range(1,6):
    for j in range(1, i+1):
        print (j, end =" ")
        print ()

 #for loop with conditional statements 1.

for i in range(1,10):
     if i==3:
         print("add this song to the favs")
     else:
         print(i)

#break and continue statements
#continue:-
for i in range(1,11):
    if i==5:
        continue
    else:
        print(i)

 #break:-
for k in range(1,5):
     if k==3:
         break
else:
     print(k)