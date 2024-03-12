#ARITHMETIC OPERATORS
print(2+3)                          #addition
print(2**10)                        #exponent
print(6-2)                          #subtraction
print(2*6)                          #multiplication
print(8/4)                          #division
print(10//4)                        #floor division
print(10%4)                         #modulus

#COMPARISON OPERATOR
print(3>2)                         #greater than
print(3<6)                         #less than
print(3==3)                        #equal to
print(4!=5)                        #not equal to
print(3<=4)                        #less than or equal to
print(3>=3)                        #greater than or equal to

#LOGICAL OPERATOR
print(3>4 or 3<4)                  #or
print(3>4 and 3<4)                 #and
print(not(3<4 or 5>4))             #not

#ASSIGNMENT OPERATOR
a=6                                #=
print(a)
a+=3                               #+=
print(a)
a-=2                               #-=
print(a)
a*=6                               #*=
print(a)

#IDENTITY OPERATOR
a=11
b=11
print(a is b)                      #is
c=121
d=12
print(c is not d)                  #is not


#BITWISE OPERATOR
print(bin(2))
print(10&8)                       #and operator
print(10|8)                       #or operator
print(10^8)                       #xor operator
print(10<<2)                      #zero fill right shift
print(10>>2)                      #zero fill left shift


#MEMBERSHIP OPERATOR
a="hello"
print("p" in a)                  #in
print("p" not in a)              #not in