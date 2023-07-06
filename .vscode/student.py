list_name = ["Tony","Timmy","Steven"]
list_height = [184,154,140]
list_of_tuples = list()
for i in range(3):
    list_of_tuples.append((list_name[i],list_height[i]))
print(list_of_tuples)

print(max(list_of_tuples))

#method 2
generator_of_tuples = zip(list_name,list_height)
print(generator_of_tuples,list(generator_of_tuples))
