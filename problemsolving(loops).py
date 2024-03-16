# Fibonacci Series
a = 0
b = 1
n = int(input("enter a number here:"))
if (n == 1):
    print(1)
else:
    print(a)
    print(b)
    for i in range(2, 13):
        c = a + b
        a = b
        b = c
        print(c)

# if number is prime or not:-

num = int(input("enter a number here:"))
if num <= 1:
    print("it is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("number is not a prime number")
            break

    else:
        print("number is a  prime number")

# check for palindrome
num = int(input("enter a number here:"))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if rev == temp:
    print("it is a palindrome number")
else:
    print("it is not a palindrome number")

# Area Calculator:-
print("*******AREA CALCULATOR*******")
while True:
    print("""press 1 for area of square
         press 2 for area of circe
         press 3 for area of rectangle
         press 4 for area of triangle""")

    choice = int(input("enter your choice: "))

    if choice == 1:
        while True:
            side = float(input("enter the side of a square: "))
            area = side ** 2
            print("area of square is: ", area)
            repeat = input("do you want to try again with square?")
            if repeat == "no":
                break

    elif choice == 2:
        while True:
            radius = float(input("enter the radius of circle: "))
            area = (3.14 * (radius ** 2))
            print("area of circle is: ", area)
            repeat = input("do you want to try again with circle?")
            if repeat == "no":
                break

    elif choice == 3:
        while True:
            length = float(input("enter the length of rectangle: "))
            breadth = float(input("enter the breadth of rectangle: "))
            area = length * breadth
            print("area of rectangle is: ", area)
            repeat = input("do you want to try again with rect?")
            if repeat == "no":
                break

    elif choice == 4:
        while True:
            base = float(input("enter the base of triangle: "))
            height = float(input("enter the height of triangle: "))
            area = (base * height) / 2
            print("area of triangle is: ", area)
            repeat = input("do you want to try again with triangle?")
            if repeat == "no":
                break

    repeat1 = input("do you want to repeat again?")
    if repeat1 == "no":
        break
