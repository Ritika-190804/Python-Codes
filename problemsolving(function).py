# 1.write a program to find maximum of three numbers in python:-

 def maximum_num(num1,num2,num3):
   if num1>num2 and num1>num3:
      print("number 1 is maximum number")
 elif num2>num1 and num2>num3:
    print("number 2 is maximum")
 else:
   print("number 3 is maximum")


 maximum_num(12,56,99)

# 2.write a python function to create and print a list where the values are square of numbers between 1 and 30:-


 def create_list():
 l= []
  for i in range(1,31):
       l.append(i**2)


        return l

 print (create_list())


# 3.write a python function that takes a number as a parameter
# and check if the number is prime or not:-

 def check_prime:
    if num == 1:
 print("it is not a prime number")
  if num == 2:
       print("it is a prime number")
 if num > 2:
 for i in range(2, num):
     if num % i == 0:
          print("it is not a prime number")
           break


        else:
             print("it is a prime number")
              break

 check_prime(37)


# 4. write a python function to sum all the numbers in a list:-

def add(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return (total)

print(add([2, 5, 8, 9, 7]))


# 5.write a python program to solve the fibonacci series using recursion:-
def fs(num):
    if num==1:
        return (0)
    elif num ==2:
        return (1)
    else:
        return(fs(num-1)+fs(num-2))

print(fs(7))

