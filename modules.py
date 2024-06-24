#In-built functions
# 1. datetime module:-

import datetime
x=datetime.datetime.now()
print(x)

y=datetime.datetime(1997,10,14)
print(y)
print(y.strftime("%y"))
print(y.strftime("%A"))
print(y.strftime("%a"))
print(y.strftime("%B"))
print(y.strftime("%m"))
print(y.strftime("%Y"))

# 2.random module:-
import random
x=random.randint(1,10)
print(x)

l=["heads","tails"]
y=random.choice(l)
print(y)

# 3.math module:-
import math
x=max(13,67,45)
print(x)
y=min(13,67,45)
print(y)

a= pow(2,4)
print(a)
b=math.sqrt(49)
print(b)

c=abs(-12)
print(c)

k=math.ceil(2.4)
print(k)
m=math.floor(2.4)
print(m)