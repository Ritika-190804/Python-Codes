a="hello"
b="Hello123"
c="123456"
d="HELLO everyone"
e=" "
f="Hello 123"
g="1.234"
h="Harry Potter and the Goblet of Fire"

print("function 1 isalnum:-")

#isalnum():-returns true if all characters in the strings are alphanumeric.
print(a,a.isalnum())
print(b,b.isalnum())
print(c,c.isalnum())
print(f,f.isalnum())
print(g,g.isalnum())


print("function 2 isalpha:-")

#isalpha():-returns true if all characters in the string are in the alphabet.
print(a,a.isalpha())
print(b,b.isalpha())
print(c,c.isalpha())
print(f,f.isalpha())
print(g,g.isalpha())



print("function 3 isdecimal:-")
#isdecimal():-returns true if all the characters in the strings are decimals.
print(a,a.isdecimal())
print(c,c.isdecimal())
print(g,g.isdecimal())



print("function 4 isdigit:- ")
#isdigit():-returns true if all the characters in the strings are digits.
print(g,g.isdigit())
print(c,c.isdigit())
print(b,b.isdigit())




print("function 5 isnumeric:- ")
#returns true if all the characters in the strings are numeric.
print(b,b.isnumeric())
print(c,c.isnumeric())
print(e,e.isnumeric())



print("function 6 islower:- ")
#returns true if all characters in the strings are lower case.
print(a,a.islower())
print(d,d.islower())
print(b,b.islower())



print("function 7 isupper:-")
#returns true if all the characters in the strings are upper case.
print(a,a.isupper())
print(b,b.isupper())
print(d,d.isupper())



print("function 8 isspace:-")
#returns true if all characters in the string are whitespaces.
print(e,e.isspace())
print(f,f.isspace())



print("function 9 istitle:-")
#returns true if the string follows the rules of a title.
print(d,d.istitle())
print(f,f.istitle())
print(h,h.istitle())
