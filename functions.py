#functions:-
# 1.
def hello():
    print("hello world")

hello()

# 2.
def add():
    x=89
    y=90
    print(x+y)
add()


#parameters and arguments:-

def add(x,y):
    print(x+y)

add(2,3)

#RETURN STATEMENT AND RECURSION:-

#return:-
def add(a,b):
    return(a+b)

print(add(12,4))


#find factorial of any number:-
def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))

print(fact(5))


#lambda function:-

a=lambda b:b*5
print(a(4))

x=lambda a,b,c:(a+b)*c
print(x(3,7,2))