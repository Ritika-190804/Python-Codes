#sort:-

import numpy as np
ar=np.array(([7,8,4,12,9],[2,8,5,1,3]))
print(np.sort(ar))

#search:-
ar=np.array([3,4,1,7,8])
#s=np.where(ar==4)
s=np.where(ar%2==0)
print(s)
ss=np.searchsorted(ar,2)
print(ss)

#filter:-
#ar=np.array([20,30,40,50])
#fa=[True,False,False,False]
#new=ar[fa]
#print(new)

#ar=np.array([20,30,40,50])
#fa=ar>35
#new=ar[fa]
#print(new)

ar=np.array([2,4,3,1])
fa=ar%2==1
new=ar[fa]
print(new)