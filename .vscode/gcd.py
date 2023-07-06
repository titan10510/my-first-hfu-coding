import math
import numpy as np

def gcd(numbers):
    bigger_one= max(numbers)
    small_one = min(numbers)
    answer = 0
    while True:
        remainder = bigger_one % small_one
        if remainder == 0:
            answer = small_one
            break
        else:
            bigger_one, small_one = small_one, remainder
    print(numbers, answer)   
    return numbers,answer

numbers = np.random.choice(10000, 2)
# answer = math.gcd(*list(numbers))
# print(numbers, answer)
x = gcd(numbers)

print(x)


# 輾轉相除法 -> 歐西里德算法
bigger_one = max(numbers)
small_one = min(numbers)
answer = 0
while True:
    remainder = bigger_one % small_one
    if remainder == 0:
        answer = small_one
        break
    else:
        bigger_one, small_one = small_one, remainder

print(f"GCD of {numbers} is {answer}")
