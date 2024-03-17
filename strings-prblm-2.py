#Take an input from a user as a string,then reverse it.
a=input("enter anything here:")
print(a[::-1])

#write a program to check if a string contains only digits.
c=input("enter anything here:")
d=(c.isdigit())
if d==True:
     print("it contain only digits")
else:
      print("it does not contain only digits")

#write a program to check if a string is a palindrome:-
r=input("enter anything here:")
rev=r[::-1]
if r==rev:
    print("it is palindrome")
else:
    print("it is not palindrome")

#write a program to find a number of vowels in a string:-
t=input("enter anything here:")
vowels=0
for i in t:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or  i=="U":
        vowels+=1

print("the no. of vowels in the following string are:",vowels)

#write a program to check if every word in a string
#begins with a capital letter:-
w=input("enter anything here:")
y=(w.istitle())
if y== True:
    print("begins with a capital letter")
else:
    print("not begins with a capital letter")

