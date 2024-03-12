#write a program to check if a number is positive.

number=int(input("enter the number here: "))
if number>0:
    print("it is positive")
else:
    print("it is negative")

#write a program to check whether a number is odd or even.

number=int(input("enter the number here: "))
if number % 2==0:
    print("it is even number")
else:
    print("it is odd number")

#write a program to create area calculator.

print("*******AREA CALCULATOR*******")
print("""press 1 for area of square
         press 2 for area of circe
         press 3 for area of rectangle
         press 4 for area of triangle""")
choice=int(input("enter your choice: "))

if choice==1:
    side=float(input("enter the side of a square: "))
    area=side**2
    print("area of square is: ",area)

elif choice==2:
    radius=float(input("enter the radius of circle: "))
    area=(3.14*(radius**2))
    print("area of circle is: ",area)

elif choice==3:
    length=float(input("enter the length of rectangle: "))
    breadth=float(input("enter the breadth of rectangle: "))
    area=length*breadth
    print("area of rectangle is: ",area)

elif choice==4:
    base=float(input("enter the base of triangle: "))
    height=float(input("enter the height of triangle: "))
    area=(base*height)/2
    print("area of triangle is: ",area)

else:
    print("wrong choice")

#write a program to check whether the passed letter is a vowel or not.

letter=input("enter the letter: ")
if letter in "aeiou" or letter in "AEIOU":
     print("it is a vowel")
else:
    print("it is not a vowel ")

#write a program to check if a number is a singal digit number,2-digit number
#and so on.....,up to 5 digits

number=int(input("enter the number here: "))
if number>=0 and number<=9:
    print("it is a 1-digit number")

elif number>=10 and number<=99:
    print("it is a 2-digit number")

elif number>=100 and number<=999:
    print("it is a 3-digit number")

elif number>=1000 and number<=9999:
    print("it is a 4-digit number")

else:
    print("it is a 5-digit number")