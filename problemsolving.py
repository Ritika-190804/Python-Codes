#write a program to display a person's name ,age & address in three different lines
name="ritika"
age=23
address="657 lake street"
print("name is: ",name)
print("age is: ",age)
print("address is: ",address)

#write a program to swap two variables
#method 1
a=22
b=24
a,b=b,a
print(a)
print(b)
#method 2
a=26
b=56
temp=a
a=b
b=temp
print(a)
print(b)


#write a program to convert a float into integer
a=12.5
print(type(a))
a=int(a)
print("after convert the value:")
print(type(a))


#write a program to take details from a student for ID-card and then print it in differnetName=
Name=input("enter the name of student:")
Age= int(input("enter the age of the student:"))
Grade=input("enter the grade of the student:")
ph_no=input("enter the ph_no  of student:")
Email=input("enter the email of student:")
print("student identity card:-")
print("Name:",Name)
print("age:",Age)
print("grade:",Grade)
print("phone no:",ph_no)
print("email:",Email)


#write a program to take an user input as integer then convert to float
a=int(input("enter the number here:"))
print(a)
print(type(a))
a=float(a)
print("after conversion:",a)
print(type(a))


