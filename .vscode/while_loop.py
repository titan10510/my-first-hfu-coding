
# 1. 生成一段數列, 為小於1000的奇數
list_odd = list()
n = 0
while n < 1000:
    if n % 2 == 1:
        list_odd.append(n)
    n = n + 1  # n += 1
# print("End: ", list_odd)

# 2. Fibonacci numbers, which less than 1000000
print("=" * 20)
f_0 = 0
f_1 = 1
f_n_minus_1 = f_1   # f_1
f_n = f_0 + f_1  # f_2

list_fibo = [f_0, f_1]
while f_n < 10**6:
    list_fibo.append(f_n)
    temp = f_n_minus_1 # 先暫存 fn-1
    f_n_minus_1 = f_n # 更新f_n-1
    f_n = f_n + temp # 更新的f_n
    print(list_fibo)

print(list_fibo, len(list_fibo))

def fibo(n):
    if n == 0:
        return 0  
    if n == 1:
        return 1
    else:
        return(fibo(n-1)+fibo(n-2))
    
print(fibo(4))
