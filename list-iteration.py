#Iteration using for loop:-
a=["Hulk","Thor","Ironman","Captain America"]
for i in a:
    print(i)

#Iteration using for loop with range and length function:-
for i in range(len(a)):
    print(a[i])

#Iteration using while loop:-
i=0
while (i<len(a)):
    print(a[i])
    i+=1

#Using short hand for loop:-
[print (i) for i in a]