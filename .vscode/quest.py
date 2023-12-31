# 把一串數列, 依據是否為
# 1. 偶數
# 2. 奇數
# 3. 3n
# 4. 3n or 5n
import numpy as np
numbers = np.random.randint(1, 100, 30)#產生30個1~100的數字
numbers.sort()#由小到大排列

# print(numbers)

list_even = list()
list_odd = list()
list_3n = list()
list_3n5n = list()

for number in numbers:
    if number % 2 == 0:
        list_even.append(number)
    else:
        list_odd.append(number)

    if number % 3 == 0:
        list_3n.append(number)
        list_3n5n.append(number)
    elif number % 5 == 0:
        list_3n5n.append(number)
