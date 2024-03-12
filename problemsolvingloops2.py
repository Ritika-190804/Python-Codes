#pattern 1:-
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end = " ")
    print()

#pattern 2:-
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end = " ")

    print()

#pattern 3:-
for i in range(1,6):
    for j in range(6,i,-1):
        print (i, end = " ")

    print()

#pattern 4:-
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end = " ")
    for k in range(i):
            print("*",end = " ")
    print()

#pattern 5:-
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end = " ")
    print()

#pattern 6:-
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end = " ")
    print()
for i in range(5,0,-1):
    for k in range(0,i-1):
        print("*",end = " ")
    print()

#pattern 7:-
for i in range(1,11):
    for j in range(1,i+1):
        print(i*j,end =" ")
    print()















