nums = [3, 1, 2, 4, 6, 5]

from collections import (
    deque, 
    Counter, 
    namedtuple, 
    defaultdict
)
left = 0  # pointer for even numbers
right = len(nums) - 1  # pointer for odd numbers


while left < right:
        # Find the first odd number from the left
        while nums[left] % 2 == 0 and left < right:
            left += 1
            

        # Find the first even number from the right
        while nums[right] % 2 != 0 and left < right:
            right -= 1
            

        # Swap the odd and even numbers
        nums[left], nums[right] = nums[right], nums[left]
        print(nums)

# print(nums)
# sorted_nums = []
   
#     # 將偶數元素添加到排序陣列
# for num in nums:
#         if num % 2 == 0:
#             sorted_nums.append(num)
    
#     # 將奇數元素添加到排序陣列
# for num in nums:
#         if num % 2 != 0:
#             sorted_nums.append(num)
# print(sorted_nums)

import matplotlib.pyplot as plt
data = [-1, -4.3, 15, 21, 31]


plt.figure(num=3 ,figsize=(8, 5),facecolor='pink')#可不寫預設會自動新一空畫布

plt.plot(data)#不同圖有不同的方法
plt.savefig('aa.jpg')
plt.show()
#plt.savefig('aa.jpg')#plt.show()他會把它消掉跟建立方法記憶體一樣
