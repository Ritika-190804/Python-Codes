#if the statement
marks=95
if marks >=90:
    print("you will get a phone")
    print("thank you")


#if else statement
marks=87
if marks>=90:
    print("you will get a phone")
else:
    print("no phone for one week")
    print("thank you")


#if-elif-else statement
marks=95
if marks>=90:
    print("you can go to a trip")
elif marks >=80 and  marks<90:
    print("you will get a new phone")
elif marks >=70 and marks<80:
    print("you will get a new book")
else:
    print("you will get your phone back")


#nested if statement
marks=96
if marks >=80:
    print("you will get a new phone")
if marks >=95:
    print("you can go to a trip")
else:
    print("no phone for a month")


#short hand if statement
marks=97
if marks>=90:print("you will get a new phone")


#short hnad if else statement
marks=83
print("you will go to a trip") if marks>=90 else print("no phone for a month")

