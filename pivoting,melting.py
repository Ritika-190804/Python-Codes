#pivoting

import pandas as pd
dict={"keys":["k1","k2","k1","k2"],
      "Names":["John","Ben","David","Peter"],
      "Houses":["red","blue","green","red"]}

df=pd.DataFrame(dict)
print(df)
print(df.pivot("keys","Names","Houses"))

#melting

dict={"keys":["k1","k2","k1","k2"],
      "Names":["John","Ben","David","Peter"],
      "Grade":["3rd","8th","9th","8th"]}

df=pd.DataFrame(dict)
print(df)
print(pd.melt(df,id_vars=["Names"],Value_vars=["Houses"]))