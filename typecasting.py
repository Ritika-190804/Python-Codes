#typecasting
name="john"
print(type(name))
age=23
print(type(age))


#implicit typecasting
a=123
b=1.23
print(type(a))
print(type(b))
c=a+b
print(c)
print(type(c))


#explicit typecasting
a="123"
b=1.23
print(type(a))
print(type(b))
a=float(a)
print("after conversion",type(a))
c=a+b
print(c)
print(type(c))