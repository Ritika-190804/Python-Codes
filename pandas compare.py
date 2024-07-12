import pandas as pd

dict={"Fruits":["mango","apples","banana","papaya"],
      "Price":[100,150,50,35],
      "Quantity":[15,10,10,3]}


df1=pd.DataFrame(dict)
print(df1)

df2=df1.copy()
df2.loc[0,"Price"]=120
df2.loc[1,"Price"]=175
df2.loc[3,"Price"]=30
df2.loc[0,"Quantity"]=12
df2.loc[1,"Price"]=175
df2.loc[3,"Quantity"]=4
print(df2)
df1.compare(df2)
print(df1)
print(df1.compare(df2,align_axis=0))
print(df1.compare(df2,keep_equal=True))
print(df1.compare(df2,keep_shape=True))