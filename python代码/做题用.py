# li = [88, 89, 90, 98, 00, 99]
# print("原列表为:",li)
# li2 = []
# for i in li:
#     if i > 0:
#         a = "19"
#         li2.append(a + str(i))
#     else:
#         b = "200"
#         li2.append(b + str(i))
# print(li2)

# li = []
# li2 = []
# for i in range(5):
#     Name = str(input("输入："))
#     li.append(Name)
# print(li)
# for j in li:
#     print(j)
# while True:
#     a = str(input("买啥:"))
#     if a == "q":
#         break
#     else:
#         if a in li:
#             print("已购买：", a)
#             li.remove(a)
#             li2.append(a)
#         else:
#             print("无商品")
# print("已购入的商品为：")
# [print(k) for k in li2]
# s = set()
# for i in range(5):
#     a = input(f"请输入第{i+1}位好友的姓名手机号")
#     s.add(a)
# for key in s:
#     print(key)

# word = input()
# s = 'HelloPyhton,HelloJava,hellophp'
# # print(s.upper().count(word))
# while True:
#     XU = {"name":"男神", "age" :18, "tel":110}
#     a = str(input("查询男神的第几项信息："))
#     print(XU[a])
#     print(type(a))
# a = int(input())
# for i in range(a):
# 	b, c = map(int, input().split())
# 	print(a+b)

# nums = list(map(int,input().split()))
# total = sum(nums)
# missing = 55 - total
# print("The missing integer is:", missing)

# def logger(fn):
#     def inner(a,b):
#         print("函数执行完毕")
#         return fn(a,b)          # fn(3,5)得到结果8，要将8这个值返回inner然后再被输出
#     return inner
# @logger     # 等价于add = logger(add)
# def add(a,b):
#     return a + b
# print("开始执行函数")
# print(add(3, 5 ))

# def prefix_decorator(prefix):
#     def decorator(fn):
#         def inner(a,b):
#             print(f"{prefix}函数即将运行")
#             res = fn(a,b)
#             print(f"{prefix}函数运行结束")
#             return res
#         return inner
#     return decorator
# @prefix_decorator("【INFO】")
# def multiply(a,b):
#     return a*b
# print(multiply(3,5))
# # 带参装饰器要三层，普通的只要两层
# a, b = map(int,input().split())
# print("a+b="+str(a+b))
# print("a-b="+str(a-b))
# print("a*b="+str(a*b))
# print("a/b="+str(int(a/b)))
# print("a%b="+str(a%b))
# import math
# a, b = map(int, input().split())
# c = math.sqrt(a*a + b*b)
# print("%.2f" % c)


# a = int(input())
# b = 0
# if a == 0:
#     b -= 1
# elif a > 0 and a < 60:
#     b += 0
# elif a >= 60:
#     b += 1
#     if a == 100:
#         b += 1
# print(b)

# lst = []
#
# for i in range(3):
#     nums = list(map(int, input().split()))
#     lst.append(nums)
#
# a = max(lst[0][0], lst[1][0], lst[2][0])
# b = max(lst[0][1], lst[1][1], lst[2][1])
# c = max(lst[0][2], lst[1][2], lst[2][2])
#
# conA = (lst[0][0] == a) or (lst[0][1] == b) or (lst[0][2] == c)
# conB = (lst[1][0] == a) or (lst[1][1] == b) or (lst[1][2] == c)
# conC = (lst[2][0] == a) or (lst[2][1] == b) or (lst[2][2] == c)
#
# if conA == conB == conC == True:
#     print("1")
# else:
#     print("0")
#
# x, y, z = map(int,input())
# if x == y:
#     print(z)
# elif x == z:
#     print(y)
# else:
#     print(x)

# x, k = map(int, input().split())
# s = f"{x:b}".zfill(15)      # 二进制补齐到15个字符
# s = s[::-1]
# a = list(str(s))
# if a[k-1] == '1':
#     print("1")
# else:
#     print("0")

# x, y = map(int, input().split())
# s = abs(x) * abs(y)
# # s是整数，分奇偶处理，格式化保留两位小数
# if s % 2 == 0:
#     print(f"{s//2}.00")
# else:
#     print(f"{s//2}.50")
# lst = []
# nums = str(input())
# for j in nums:
#     num = int(j)
#     lst.append(num)
# for i in lst:
#     if i == 0:
#         print("-----", end = "")
#     elif i > 0 and i <= 5:
#         print("." * i + "-" * (5 - i), end = "")
#     elif i > 5 and i <= 9:
#         print("-" * (i-5) + "." * (10 - i), end = "")

# y, m, d = map(int, input().split())
#
# # 先判断愚人节！优先判断
# if m == 4 and d == 1:
#     print("NO")
# elif m == 2 and d == 29:
#     # 修正闰年表达式
#     if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#         print("YES")
#     else:
#         print('NO')
# elif m >= 13 or m == 0 or d == 0 or d > 31:
#     print("NO")
# elif m == 4 or m == 6 or m == 9 or m == 11:
#     if d == 31:
#         print("NO")
#     else:
#         print("YES")
# else:
#     print("YES")

# nums = int(input())
# a = 0
# while nums > 0:
#     if nums % 5 != 0 and nums % 7 != 0 and nums % 6 == 0 and nums % 8 == 0 and nums % 9 == 0:
#         a += 1
#     nums -= 1
# print(a)

# a = str(input())
# b = a[::-1]
# c = int(b)
# print(c)

# C, w, k, t = map(int, input().split())
# now = 0
# threshold = C / k
#
# while True:
#     # 1. 计算当前这一口要吃多少
#     if now < threshold:
#         eat = w + 10
#     else:
#         eat = w
#     # 2. 吃这一口
#     now += eat
#     # 3. 呕吐，直到不超过容量C
#     while now > C:
#         now -= t
#     # 4. 预测【下一口】，看下一口能不能吃
#     if now < threshold:
#         next_eat = w + 10
#     else:
#         next_eat = w
#     # 如果吃下一口就超过C，就停止进食
#     if now + next_eat > C:
#         break
# print(now)

# import math
#
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     # 只检查奇数，从3到sqrt(n)，步长+2
#     max_i = int(math.sqrt(n)) + 1
#     for i in range(3, max_i, 2):
#         if n % i == 0:
#             return False
#     return True
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     if is_prime(n):
#         print("Yes")
#     else:
#         print("No")



# m = int(input())
# n = int(input())
# y = (6.0*n-8.0*m)/(n-m)
# x = 8.0*m-y*m
# z = x/(10.0-y)
# print(f"Original number of visitors: {"%.1f" % x}")
# print(f"New arriavlas per minute: {"%.1f" % y}")
# print(f"Check time when 10 gates are opened: {"%.1f" % z}")

# a = str(input())
# b = 'myxii'
# c = 0
# for i in range(5):
#     if a[i] != b[i]:
#         c += 1
# print(c)


# t1 = float(input())
# t2 = float(input())
#
# if t1 <= t2 * 0.2:
#     print("畅通")
#
# elif t1 <= t2 * 0.5 and t1 > t2 * 0.2:
#     print("基本畅通")
#
# elif t1<=t2*0.8 and t1>t2*0.5:
#     print("轻度拥堵")
#
# elif t1<=t2*1.1 and t1>t2*0.8:
#     print("中度拥堵")
# else:
#     print("严重拥堵")
