# Basics of dictionaries:-

Employee_Data = {"name": "John", "age": "24", "gender": "male"}
print(Employee_Data)
print(Employee_Data["gender"])
print(Employee_Data["age"])

# Iteration in Dictionaries:-
Student = {"name": "John", "class": "6th", "roll_no": 23}

# printing all the key names one by one:-
for x in Student:
    print(x)

# printing all the value names one by one:-
for x in Student:
    print(Student[x])
student = {"name": "Ritika", "Dept": "BCA", "Roll_no": "22453"}
# using value function:-
for x in student.values():
    print(x)

# using items function:-
for x, y in student.items():
    print(x)
