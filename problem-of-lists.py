A=["ROSS","RACHEL","MONICA","JOE"]
#write a program to swap first and forth element:-
A[0],A[3]=A[3],A[0]
print(A)


#write a program to add  a new value at second position:-
A.insert(1,"Phoebe")
print(A)


#write a program to delete a value from 3rd position:-
A.pop(2)
print(A)


B=[13,7,12,10]
#write a program to multiply all the numbers in the list:-
mul = 1
for i in (B):
    mul = mul*i

print(mul)

#write a program to find a largest number from the list:-
B.sort()
print(B)

print("the largest number is",B[-1])
#write a program to find a smallest number from the list:-
B.sort()
print(B)

print("the smallest number is",B[0])

