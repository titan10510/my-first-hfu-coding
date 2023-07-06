from collections import namedtuple
import numpy as np
np1 = np.random.randint(5)
print(np1)
pointxyz = namedtuple(typename="pointxyz",field_names=["x","y","z"])
name1 = pointxyz(3,4,5)
name2 = pointxyz(8,8,9)
print(name1,name2)
x=0
for i in range(0,3):
    if i==0:
       x = abs((name1[i] - name2[i])**2)
       print(x)
    if i ==1:
        x = x + abs((name1[i]  - name2[i])**2)
        print(x)
    if i ==2:
        x = x + abs((name1[i] - name2[i])**2)
        print(x)



