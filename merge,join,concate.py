import pandas as pd

data1={"EmpId":["E01","E02","E03","E04","E05","E06"],
       "Names":["Ram","Shyam","Rahul","Vishal","Ravi"],
       "Age":[34,56,23,44,30]}


data2={"EmpID":["E01","E02","E03","E04","E05","E06"],
       "Salary":[45000,56000,34000,30000,50000],
       "Dept":["BCA","BBA","BTECH","LLB"]}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(df1)
print()
print(df2)


print(pd.merge([df1,df2]))
print(pd.merge(df1,df2,on="EmpId"))
print(pd.merge(df1,df2,on="EmpId",how="left"))
print(pd.merge(df1,df2,on="EmpId",how="right"))


