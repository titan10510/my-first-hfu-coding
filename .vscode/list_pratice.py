list_x  = list()
list_y = [1,2,3,4]
list_z = ["This is a apple.".split()] #string to list
list_x.append('A')
list_x.append('B')
list_x.extend(['C','D','E','F'])
list_x.extend('G')
list_x = list_x + list_y
list_x.append(list_z)
print(list_x)

# find and get
# print(list_x[3:7]) #DEFG
# print(list_x[3:]) #不設定結尾
index_f  = list_x.index("F")
# print(list_x[index_f:])
# print(list_x[list_x.index("F"):])
reversed_f  = list(reversed(list_x))
print(reversed_f[0:4])

#sort 
temp = ['G','B','E','A','1','2','3']
list_w = sorted(temp)
print()
print()
