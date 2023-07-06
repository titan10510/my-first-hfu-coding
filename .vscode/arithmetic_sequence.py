a_0 = 1
n = 4 
d = 5
list_1 = []
a_1 = a_0 + d
a_2 = a_1 + d
a_3 = a_2 + d 
for i in  range(4):
    x= 0
    x = a_0 + i*d
    list_1.append(x)

print(list_1, sum(list_1),(n/2)*(list_1[0]+list_1[-1]))
