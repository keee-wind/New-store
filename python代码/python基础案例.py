# -*- coding: utf-8 -*-
"""
================================================================================
            Python 基础知识案例集  ——  题目在前 · 答案在后
================================================================================

【使用说明】
1. 在 PyCharm 中右键本文件 -> Run 'python_basics_cases'，会依次运行所有题目的
   参考答案并打印结果。
2. 建议先自己动手做一遍，做完再往下翻答案（答案在文件的后半部分）。
3. 每道答案都是一个独立函数，函数名与题号一一对应，可以单独运行。
   把文件最底部 main 里的 RUN_ALL 改成 False，再在 SELECTED 里写题号，
   就只运行你指定的几道题。
4. 环境要求：Python 3.8+，只用标准库，无需安装任何第三方包。

【题目导航】
    第一部分  基础语法 ......................  第  1 ~  5 题
    第二部分  列表 / 元组 / 字典 / 集合 ......  第  6 ~ 12 题
    第三部分  流程控制 ......................  第 13 ~ 18 题
    第四部分  函数与函数式编程 ..............  第 19 ~ 23 题
    第五部分  进阶与实战 ....................  第 24 ~ 30 题
================================================================================
"""


# ==============================================================================
# ==============================================================================
# #                                                                          #
# #                     第 一 部 分  ·  题  目  区                            #
# #                                                                          #
# #              （先别往下滑，自己动手写一遍再看答案）                        #
# #                                                                          #
# ==============================================================================
# ==============================================================================

# ------------------------------------------------------------------------------
# 【第一部分】基础语法
# ------------------------------------------------------------------------------
#
# 第 1 题  变量交换
#   已知 a = 1, b = 2，请交换两个变量的值。要求用两种方法：
#   (1) 借助临时变量  (2) Python 特有的写法（一行搞定）


#
# 第 2 题  数据类型与类型转换
#   现有字符串 age_str = "18"、price_str = "3.14"：
#   (1) 把它们分别转成 int 和 float，并打印各自的类型
#   (2) 把数字 123 转成字符串，把 0 和 1 转成布尔值
#   (3) 思考题：bool("False") 的结果是什么？为什么？
#
# 第 3 题  字符串反转与回文判断
#   (1) 把字符串 "上海自来水来自海上" 反转输出
#   (2) 写一个函数 is_palindrome(s)，判断字符串是否为回文（正读反读都一样）
#
# 第 4 题  f-string 格式化
#   已知 name = "小明"，score = 95.5：
#   (1) 输出 "姓名: 小明, 成绩: 95.5"
#   (2) 成绩保留 1 位小数；如果成绩 >= 90 显示等级 A，否则显示 B
#   (3) 用 f-string 输出左对齐、居中、右对齐各 10 个字符宽度的表格行
#   (4) 把 0.256 格式化成百分比（保留 1 位小数）
#
# 第 5 题  字符串常用方法
#   给出 s = "  Hello, Python World!  "，请完成：
#   (1) 去掉首尾空格   (2) 全部转小写   (3) 按逗号分割
#   (4) 把 Python 替换成 Python3   (5) 判断是否以 "he" 开头、以 "lo" 结尾
#   (6) "abc123".isalpha() / "abc123".isalnum() / "123".isdigit() 分别是什么


# ------------------------------------------------------------------------------
# 【第二部分】列表 / 元组 / 字典 / 集合
# ------------------------------------------------------------------------------
#
# 第 6 题  列表去重（并保持原来的顺序）
#   已知 nums = [1, 3, 2, 3, 1, 4]，去重后应该是 [1, 3, 2, 4]。
#   请用至少两种方法实现，并说明为什么直接 set() 不满足要求。
#
# 第 7 题  统计最大值 / 最小值 / 总和 / 平均值
#   已知 nums = [12, 45, 7, 23, 56, 8]，求最大值、最小值、总和、平均值（保留 2 位小数）
#
# 第 8 题  排序
#   (1) 把 [5, 2, 9, 1] 升序、降序输出（分别用 sorted 和 list.sort）
#   (2) 学生列表 [("小明",88),("小红",95),("小刚",76)]，按成绩从高到低排序
#   (3) 单词列表 ["banana","apple","cherry"]，按单词长度排序
#
# 第 9 题  切片
#   已知 lst = list(range(10))，请输出：
#   (1) 第 3~5 个元素  (2) 前 3 个  (3) 后 3 个
#   (4) 所有偶数下标元素  (5) 整个列表反转  (6) 从下标 1 开始每隔 3 个取一个
#
# 第 10 题  字典的遍历与合并
#   d = {"name":"小明","age":18,"city":"北京"}
#   (1) 遍历打印所有键值对   (2) 只取所有键和所有值
#   (3) 把 {"age":19,"score":90} 合并进 d，age 被覆盖
#   (4) 取不存在的键时，怎样不报错并返回默认值？
#
# 第 11 题  统计字符出现次数
#   统计 "hello world" 中每个字符出现的次数（忽略空格），并按次数从高到低排序。
#   提示：可以用字典的 get 方法，也可以试试标准库 collections.Counter
#
# 第 12 题  集合运算
#   a = {1,2,3,4}，b = {3,4,5,6}，求：交集、并集、差集（a 有 b 没有）、对称差集


# ------------------------------------------------------------------------------
# 【第三部分】流程控制
# ------------------------------------------------------------------------------
#
# 第 13 题  判断闰年
#   写函数 is_leap(year)：能被 4 整除但不能被 100 整除，或者能被 400 整除。
#   分别测试 1900、2000、2023、2024 年。
#
# 第 14 题  打印九九乘法表
#   用两层循环打印成三角形，第一行 1x1，最后一行 1x9 到 9x9。
#
# 第 15 题  斐波那契数列
#   输出前 10 项（0, 1, 1, 2, 3, 5, 8, ...）。要求：循环版 + 递归版各写一个。
#
# 第 16 题  素数（质数）
#   写 is_prime(n) 判断素数，并输出 2~50 之间所有的素数。
#   提示：只需判断到 int(n ** 0.5) 即可，不用循环到 n-1。
#
# 第 17 题  水仙花数
#   找出 100~999 之间所有"水仙花数"：各位数字的立方和等于该数本身（如 153 = 1³+5³+3³）
#
# 第 18 题  猜数字游戏
#   程序随机生成 1~100 的数字，玩家输入猜测，程序提示"太大/太小"，直到猜中。
#   要求：真人在键盘上玩不方便自动化测试，请写一个用二分法"模拟玩家"的版本，
#        再把真正的交互版（用 input()）以注释形式写在旁边。


# ------------------------------------------------------------------------------
# 【第四部分】函数与函数式编程
# ------------------------------------------------------------------------------
#
# 第 19 题  函数参数：默认值 / *args / **kwargs
#   (1) 定义 func(a, b=2, *args, **kwargs)，分别用 func(1) 和
#       func(1, 3, 5, 7, name="小明", age=18) 调用，观察参数去到了哪里
#   (2) 写一个 add(*nums)，可以传入任意个数并求和
#
# 第 20 题  递归求阶乘
#   用递归实现 fact(n)，计算 5! ，并与 math.factorial(5) 对比。
#
# 第 21 题  lambda 与 map / filter / reduce
#   已知 nums = [1,2,3,4,5,6]：
#   (1) 用 map 求每个数的平方  (2) 用 filter 取出所有偶数
#   (3) 用 reduce 求和  (4) 用 lambda 做排序 key，实现降序
#
# 第 22 题  装饰器
#   (1) 写一个装饰器，在函数执行前后打印日志
#   (2) 写一个带参数的装饰器 repeat(n)，让被装饰的函数重复执行 n 次
#
# 第 23 题  生成器
#   (1) 写生成器 count_up(n)，依次产出 1~n
#   (2) 把 (x**2 for x in range(5)) 转换成列表
#   (3) 写一个无限斐波那契生成器，用 next() 取前 8 个


# ------------------------------------------------------------------------------
# 【第五部分】进阶与实战
# ------------------------------------------------------------------------------
#
# 第 24 题  推导式（列表 / 字典 / 集合 / 嵌套）
#   (1) 1~10 的平方  (2) 1~20 中能被 3 整除的数  (3) {1:1, 2:4, ...} 的平方字典
#   (4) 用集合推导式去重取余数  (5) 二维列表展平  (6) 二维列表推导式（九九乘法表的数字版）
#
# 第 25 题  异常处理
#   (1) 写 divide(a, b)，处理除零错误，并保证 finally 一定执行
#   (2) 自定义异常 ScoreError，当成绩不在 0~100 之间时抛出并捕获
#
# 第 26 题  文件读写
#   用 with open(...) 以 UTF-8 编码：写入 3 行文字 -> 整体读回 -> 按行读成列表 -> 追加一行
#   注意：写文件一定要指定 encoding="utf-8"，否则 Windows 中文会乱码。
#
# 第 27 题  面向对象
#   (1) 定义父类 Animal（类属性 + __init__ + speak + __str__）
#   (2) Dog、Cat 继承并重写 speak，用同一个循环调用实现多态
#   (3) 用 @property / @setter 实现属性封装
#
# 第 28 题  模块与常用标准库
#   演示 import math / random / datetime，以及 from collections import Counter, defaultdict
#
# 第 29 题  常用内置函数：zip / enumerate / any / all
#   把 names = ["小明","小红","小刚"] 与 scores = [88,95,76] 配对输出带编号的成绩单
#
# 第 30 题  综合实战：学生成绩管理
#   给一份学生名单（姓名+成绩），输出：按成绩排名的榜单、平均分、最高分、
#   优秀名单（>=90）、不及格名单（<60，没有则显示"无"）


# ==============================================================================
# ==============================================================================
# #                                                                          #
# #                     第 二 部 分  ·  答  案  区                            #
# #                                                                          #
# ==============================================================================
# ==============================================================================


# ------------------------------------------------------------------------------
# 第一部分 · 基础语法
# ------------------------------------------------------------------------------

# %% 第 1 题 · 变量交换
# 题目：已知 a = 1, b = 2，请交换两个变量的值。要求两种写法：(1) 借助临时变量  (2) Python 特有的元组解包


# def q01_swap():
#     """变量交换"""
#     a, b = 1, 2
#     print(f"交换前: a={a}, b={b}")
#
#     # 方法一：借助临时变量（几乎所有语言都通用）
#     temp = a
#     a = b
#     b = temp
#     print(f"方法一(临时变量)后: a={a}, b={b}")
#
#     # 方法二：Python 特有的元组解包，一行搞定（推荐）
#     a, b = b, a
#     print(f"方法二(元组解包)后: a={a}, b={b}")
#
#     # 补充：Python 中 a, b = b, a 右边会先算出一个元组 (2, 1)，再依次赋值
#
#
# # %% 第 2 题 · 数据类型与类型转换
# # 题目：age_str = "18"、price_str = "3.14"：(1) 分别转成 int / float 并打印类型  (2) 数字转字符串、0 和 1 转布尔  (3) 思考 bool("False") 是什么
#
#
# def q02_data_types():
#     """数据类型与类型转换"""
#     age_str = "18"
#     price_str = "3.14"
#
#     age = int(age_str)          # 字符串 -> 整数
#     price = float(price_str)    # 字符串 -> 浮点数
#     text = str(123)             # 数字 -> 字符串
#     flag = bool(0)              # 0 -> False，非 0 -> True
#
#     print(f"age = {age}, type = {type(age)}")
#     print(f"price = {price}, type = {type(price)}")
#     print(f"text = '{text}', type = {type(text)}")
#     print(f"flag = {flag}, type = {type(flag)}")
#
#     # 反例：不是"看起来像数字"就能转，下面这行会报 ValueError
#     # int("18.5")
#
#     # 思考题答案：bool("False") 结果是 True！
#     # 因为非空字符串本身是"真值"，和字符串内容无关。只有 ""、0、0.0、[]、{}、None 才是 False。
#     print('bool("False") =', bool("False"), '  <-- 非空字符串一律为 True')
#
#
# # %% 第 3 题 · 字符串反转与回文判断
# # 题目：(1) 把 "上海自来水来自海上" 反转输出  (2) 写 is_palindrome(s) 判断回文
#
#
# def q03_reverse_palindrome():
#     """字符串反转与回文判断"""
#     s = "上海自来水来自海上"
#
#     # 切片反转：[开始:结束:步长]，步长为 -1 表示倒着取
#     print("原字符串 :", s)
#     print("反转后   :", s[::-1])
#
#     def is_palindrome(text):
#         """判断是否为回文"""
#         return text == text[::-1]
#
#     print("是否回文 :", is_palindrome(s))
#     print("是否回文 :", is_palindrome("hello"))
#
#
# # %% 第 4 题 · f-string 格式化
# # 题目：name = "小明"，score = 95.5：(1) 输出姓名和成绩  (2) 成绩保留 1 位小数 + 等级 A/B  (3) 左对齐/居中/右对齐各 10 宽  (4) 0.256 转百分比
#
#
# def q04_format():
#     """f-string 格式化"""
#     name, score = "小明", 95.5
#
#     # (1) 最基本的 f-string
#     print(f"姓名: {name}, 成绩: {score}")
#
#     # (2) 保留 1 位小数 + 条件表达式
#     print(f"姓名: {name}, 成绩: {score:.1f}, 等级: {'A' if score >= 90 else 'B'}")
#
#     # (3) 对齐：< 左对齐  ^ 居中  > 右对齐，数字是总宽度
#     print(f"|{'左对齐':<10}|{'居中':^10}|{'右对齐':>10}|")
#     print(f"|{'abc':<10}|{'abc':^10}|{'abc':>10}|")
#
#     # (4) 百分比格式
#     print(f"0.256 转百分比: {0.256:.1%}")
#
#     # 加分项：千分位、补零
#     print(f"{12345678:,}  {42:05d}")
#
#
# # %% 第 5 题 · 字符串常用方法
# # 题目：s = "  Hello, Python World!  "：(1) 去首尾空格 (2) 转小写 (3) 按逗号分割 (4) 替换 Python (5) startswith/endswith (6) isalpha/isalnum/isdigit
#
#
# def q05_str_methods():
#     """字符串常用方法"""
#     s = "  Hello, Python World!  "
#
#     print("strip   :", repr(s.strip()))                 # 去首尾空格
#     print("lower   :", s.strip().lower())               # 转小写
#     print("split   :", s.strip().split(","))            # 按逗号分割 -> 列表
#     print("replace :", s.strip().replace("Python", "Python3"))
#     print("startswith / endswith:",
#           s.strip().lower().startswith("he"), s.strip().endswith("lo"))
#     print("join    :", "-".join(["a", "b", "c"]))
#     print("find    :", s.find("Python"))                # 找不到返回 -1
#
#     print('"abc123".isalpha() =', "abc123".isalpha(), "(有数字，False)")
#     print('"abc123".isalnum() =', "abc123".isalnum(), "(字母+数字，True)")
#     print('"123".isdigit()    =', "123".isdigit())
#
#
# # ------------------------------------------------------------------------------
# # 第二部分 · 列表 / 元组 / 字典 / 集合
# # ------------------------------------------------------------------------------
#
# # %% 第 6 题 · 列表去重并保持原顺序
# # 题目：nums = [1, 3, 2, 3, 1, 4] 去重后为 [1, 3, 2, 4]，至少两种方法，并说明为什么 set() 不满足要求
#
#
# def q06_dedup():
#     """列表去重并保持原顺序"""
#     nums = [1, 3, 2, 3, 1, 4]
#     print("原列表:", nums)
#
#     # 方法一：dict.fromkeys —— 利用了 Python 3.7+ 字典有序的特性，既快又保序（推荐）
#     print("方法一 dict.fromkeys :", list(dict.fromkeys(nums)))
#
#     # 方法二：循环判断，逻辑最好懂，但数据量大时较慢（in 是 O(n)）
#     result = []
#     for n in nums:
#         if n not in result:
#             result.append(n)
#     print("方法二 循环判断       :", result)
#
#     # 方法三：set 去重，但不保证顺序，所以不满足本题要求
#     print("方法三 set(不保序)    :", list(set(nums)))
#
#
# # %% 第 7 题 · 最大值/最小值/总和/平均值
# # 题目：nums = [12, 45, 7, 23, 56, 8]，求最大值、最小值、总和、平均值（保留 2 位小数）
#
#
# def q07_stats():
#     """最大值 / 最小值 / 总和 / 平均值"""
#     nums = [12, 45, 7, 23, 56, 8]
#
#     print("最大值:", max(nums))
#     print("最小值:", min(nums))
#     print("总和  :", sum(nums))
#     print("平均值:", round(sum(nums) / len(nums), 2))   # round 四舍五入到 2 位
#     print(f"平均值(f-string): {sum(nums) / len(nums):.2f}")
#
#     # 也可以用内置的统计模块
#     import statistics
#     print("平均值(statistics):", statistics.mean(nums))
#
#
# # %% 第 8 题 · 排序
# # 题目：(1) [5,2,9,1] 升序降序（sorted 与 list.sort 各写一遍） (2) 学生列表按成绩降序  (3) 单词按长度排序
#
#
# def q08_sort():
#     """排序"""
#     nums = [5, 2, 9, 1]
#
#     # sorted() 返回新列表，原列表不变
#     print("sorted 升序 :", sorted(nums))
#     print("sorted 降序 :", sorted(nums, reverse=True))
#     print("原列表未变  :", nums)
#
#     # list.sort() 原地排序，返回 None
#     nums.sort(reverse=True)
#     print("原地降序后  :", nums)
#
#     # 按 key 排序：key 是一个函数，表示"按什么排序"
#     students = [("小明", 88), ("小红", 95), ("小刚", 76)]
#     print("按成绩降序 :", sorted(students, key=lambda x: x[1], reverse=True))
#     print("按姓名排序 :", sorted(students, key=lambda x: x[0]))
#
#     words = ["banana", "apple", "cherry"]
#     print("按长度排序 :", sorted(words, key=len))
#
#     # 多级排序：先按成绩降序，成绩相同再按姓名
#     print("多级排序   :", sorted(students, key=lambda x: (-x[1], x[0])))
#
#
# # %% 第 9 题 · 切片
# # 题目：(1) 第 3~5 个 (2) 前 3 个 (3) 后 3 个 (4) 偶数下标 (5) 整体反转 (6) 从下标 1 开始每隔 3 个取一个
#
#
# def q09_slice():
#     """切片"""
#     lst = list(range(10))          # [0,1,2,...,9]
#     print("原列表   :", lst)
#     print("第3~5个 :", lst[2:5])     # 下标从 0 开始，左闭右开
#     print("前3个   :", lst[:3])
#     print("后3个   :", lst[-3:])
#     print("偶数下标:", lst[::2])
#     print("反转    :", lst[::-1])
#     print("每3取1  :", lst[1:8:3])
#     print("复制一份:", lst[:])
#
#
# # %% 第 10 题 · 字典遍历与合并
# # 题目：(1) 遍历打印键值对 (2) 取出所有键和值 (3) 合并 {"age":19,"score":90} 且覆盖 age (4) 取不存在的键时不报错的方法
#
#
# def q10_dict_ops():
#     """字典的遍历与合并"""
#     d = {"name": "小明", "age": 18, "city": "北京"}
#
#     # 遍历
#     for key, value in d.items():
#         print(f"  {key} = {value}")
#     print("所有键:", list(d.keys()))
#     print("所有值:", list(d.values()))
#
#     # 合并：update 会覆盖同名键
#     d2 = {"age": 19, "score": 90}
#     d.update(d2)
#     print("update 后:", d)
#
#     # 也可以这样合并（生成新字典）
#     print("解包合并 :", {**{"a": 1}, **{"b": 2}})
#
#     # 安全取值：get(key, 默认值)，键不存在也不报错
#     print("get 安全取值:", d.get("gender", "未知"))
#     # 对比：d["gender"] 会直接抛 KeyError
#     print("setdefault   :", d.setdefault("gender", "男"), "->", d["gender"])
#
#
# # %% 第 11 题 · 统计字符出现次数
# # 题目：统计 "hello world" 每个字符出现次数（忽略空格），并按次数从高到低排序；再试试 collections.Counter
#
#
# def q11_count_chars():
#     """统计字符出现次数"""
#     s = "hello world"
#     print("原字符串:", s)
#
#     # 方法一：字典 + get(key, 0) + 1
#     counter = {}
#     for ch in s:
#         if ch == " ":
#             continue
#         counter[ch] = counter.get(ch, 0) + 1
#     print("方法一:", counter)
#
#     # 按次数从高到低排序：把 dict 转成 (键, 值) 列表再按 value 排序
#     ranked = sorted(counter.items(), key=lambda x: x[1], reverse=True)
#     print("按次数排序:", ranked)
#
#     # 方法二：标准库 Counter，一行搞定
#     from collections import Counter
#     print("方法二 Counter:", Counter(s))
#     print("出现最多的 3 个:", Counter(s).most_common(3))
#
#
# # %% 第 12 题 · 集合运算
# # 题目：a = {1,2,3,4}，b = {3,4,5,6}：求交集、并集、差集、对称差集
#
#
# def q12_set_ops():
#     """集合运算"""
#     a = {1, 2, 3, 4}
#     b = {3, 4, 5, 6}
#
#     print("a 交集 b   (&):", a & b)
#     print("a 并集 b   (|):", a | b)
#     print("a 差集 b   (-):", a - b)     # 在 a 中但不在 b 中
#     print("对称差集   (^):", a ^ b)     # 只在其中一个里出现
#
#     # 等价的函数写法
#     print("union        :", a.union(b))
#     print("intersection :", a.intersection(b))
#     print("difference   :", a.difference(b))
#
#     # 集合最常见的用途：去重 + 快速判断成员
#     print("判断 3 是否在 a 中:", 3 in a)
#     print("列表去重:", list(set([1, 1, 2, 3, 3])))
#
#
# # ------------------------------------------------------------------------------
# # 第三部分 · 流程控制
# # ------------------------------------------------------------------------------
#
# # %% 第 13 题 · 判断闰年
# # 题目：is_leap(year)：能被 4 整除不能被 100 整除，或能被 400 整除。测试 1900 / 2000 / 2023 / 2024
#
#
# def q13_leap_year():
#     """判断闰年"""
#     def is_leap(year):
#         # 能被 4 整除且不能被 100 整除，或者能被 400 整除
#         return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#
#     for year in [1900, 2000, 2023, 2024]:
#         print(f"{year} 年 {'是' if is_leap(year) else '不是'}闰年")
#
#
# # %% 第 14 题 · 打印九九乘法表
# # 题目：两层循环打印成三角形，第 i 行打印 1x1 到 ixi
#
#
# def q14_multiplication_table():
#     """打印九九乘法表"""
#     for i in range(1, 10):          # i 是行号（被乘数）
#         for j in range(1, i + 1):   # 第 i 行只打印 i 个式子
#             print(f"{j}x{i}={i * j:<4}", end="")
#         print()                     # 每行结束后换行
#
#
# # %% 第 15 题 · 斐波那契数列
# # 题目：输出前 10 项，要求循环版 + 递归版各写一个
#
#
# def q15_fibonacci():
#     """斐波那契数列"""
#     n = 10
#
#     # 循环版：滚动变量，效率 O(n)
#     a, b = 0, 1
#     result = []
#     for _ in range(n):
#         result.append(a)
#         a, b = b, a + b          # 同时更新，等价于 a,b = 1,0+1
#     print("循环版:", result)
#
#     # 递归版：写法简洁但重复计算多，n 大了会非常慢
#     def fib(k):
#         return k if k < 2 else fib(k - 1) + fib(k - 2)
#
#     print("递归版:", [fib(i) for i in range(n)])
#
#
# # %% 第 16 题 · 素数
# # 题目：写 is_prime(n) 并输出 2~50 之间的所有素数。提示：只需判断到 int(n ** 0.5)
#
#
# def q16_prime():
#     """素数"""
#     def is_prime(n):
#         if n < 2:
#             return False
#         # 只需判断到平方根：如果 n 有大于 sqrt(n) 的因子，必然有对应的小因子
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     print("2~50 的素数:", [x for x in range(2, 51) if is_prime(x)])
#     print("is_prime(97) =", is_prime(97), " is_prime(1) =", is_prime(1))
#
#
# # %% 第 17 题 · 水仙花数
# # 题目：找出 100~999 中各位数字立方和等于自身的数，如 153 = 1³+5³+3³
#
#
# def q17_narcissistic():
#     """水仙花数"""
#     result = []
#     for i in range(100, 1000):
#         hundreds = i // 100          # 百位
#         tens = i // 10 % 10          # 十位
#         units = i % 10               # 个位
#         if hundreds ** 3 + tens ** 3 + units ** 3 == i:
#             result.append(i)
#
#     print("100~999 的水仙花数:", result)
#
#     # 更通用的写法：用字符串处理，适用于任意位数（如四叶玫瑰数）
#     def is_narcissistic(num):
#         digits = str(num)
#         power = len(digits)
#         return sum(int(d) ** power for d in digits) == num
#
#     print("四叶玫瑰数(1000~9999):", [x for x in range(1000, 10000) if is_narcissistic(x)])
#
#
# # %% 第 18 题 · 猜数字游戏
# # 题目：随机 1~100，提示太大/太小直到猜中。用二分法模拟玩家 + 注释形式给出真人交互版
#
#
# def q18_guess_number():
#     """猜数字游戏"""
#     import random
#
#     target = random.randint(1, 100)
#
#     # 用二分法"模拟玩家"来自动演示（真正的玩家每次手输一个数）
#     low, high, times = 1, 100, 0
#     while True:
#         guess = (low + high) // 2
#         times += 1
#         if guess == target:
#             break
#         elif guess < target:
#             low = guess + 1
#         else:
#             high = guess - 1
#
#     print(f"随机目标数 = {target}，二分法用了 {times} 次猜中")
#     print(f"（理论上 7 次以内一定能猜中 1~100 的任意数字，因为 2^7 = 128 > 100）")
#
#     print("""
# # ===== 真人交互版（把下面的注释去掉就能玩）=====
# # import random
# # target = random.randint(1, 100)
# # count = 0
# # while True:
# #     guess = int(input("请输入 1~100 的数字: "))
# #     count += 1
# #     if guess == target:
# #         print(f"恭喜你，{count} 次猜对了！")
# #         break
# #     print("太大了" if guess > target else "太小了")
# """)
#
#
# # ------------------------------------------------------------------------------
# # 第四部分 · 函数与函数式编程
# # ------------------------------------------------------------------------------
#
# # %% 第 19 题 · 函数参数
# # 题目：(1) func(a, b=2, *args, **kwargs) 分别用 func(1) 和 func(1,3,5,7,name="小明",age=18) 调用  (2) add(*nums) 任意个数求和
#
#
# def q19_func_params():
#     """函数参数：默认值 / *args / **kwargs"""
#     def func(a, b=2, *args, **kwargs):
#         print(f"  a={a}  b={b}  args={args}  kwargs={kwargs}")
#
#     print("func(1):")
#     func(1)
#
#     print('func(1, 3, 5, 7, name="小明", age=18):')
#     func(1, 3, 5, 7, name="小明", age=18)
#
#     # 顺序：位置参数 -> 默认参数 -> *args（多出来的位置参数） -> **kwargs（关键字参数）
#     def add(*nums):
#         """任意个数求和"""
#         return sum(nums)
#
#     print("add(1,2,3,4) =", add(1, 2, 3, 4))
#     print("add() =", add())
#
#     # 解包传参：* 解包列表，** 解包字典
#     params = [1, 3]
#     print("解包列表 func(*[1,3]):")
#     func(*params)
#
#
# # %% 第 20 题 · 递归求阶乘
# # 题目：递归实现 fact(n) 计算 5!，并与 math.factorial(5) 对比
#
#
# def q20_factorial():
#     """递归求阶乘"""
#     def fact(n):
#         """5! = 5 * 4 * 3 * 2 * 1 = 120"""
#         if n <= 1:                 # 递归的出口（基线条件），必须有，否则无限递归
#             return 1
#         return n * fact(n - 1)     # 递归调用
#
#     for n in [0, 1, 5, 10]:
#         print(f"{n}! = {fact(n)}")
#
#     import math
#     print("对比 math.factorial(5) =", math.factorial(5))
#
#
# # %% 第 21 题 · lambda 与 map/filter/reduce
# # 题目：(1) 求平方 (2) 取偶数 (3) 求和 (4) 用 lambda 做排序 key 实现降序
#
#
# def q21_lambda_map_filter():
#     """lambda 与 map / filter / reduce"""
#     nums = [1, 2, 3, 4, 5, 6]
#
#     # lambda 就是匿名函数，等价于 def square(x): return x ** 2
#     print("map 求平方   :", list(map(lambda x: x ** 2, nums)))
#     print("filter 取偶数:", list(filter(lambda x: x % 2 == 0, nums)))
#
#     from functools import reduce
#     print("reduce 求和  :", reduce(lambda a, b: a + b, nums))
#
#     print("lambda 排序  :", sorted(nums, key=lambda x: -x))
#
#     # 推导式写法通常更 Pythonic，可读性也更好
#     print("推导式等价   :", [x ** 2 for x in nums], [x for x in nums if x % 2 == 0])
#
#
# # %% 第 22 题 · 装饰器
# # 题目：(1) 函数执行前后打印日志的装饰器  (2) 带参数的装饰器 repeat(n) 重复执行 n 次
#
#
# def q22_decorator():
#     """装饰器"""
#     # ---- (1) 基础装饰器：在不改动原函数的前提下增加功能 ----
#     def logger(func):
#         """接收一个函数，返回一个新的函数"""
#         def wrapper(*args, **kwargs):
#             print(f"  [日志] 开始执行 {func.__name__}()")
#             result = func(*args, **kwargs)      # 调用原函数
#             print(f"  [日志] {func.__name__}() 执行结束")
#             return result
#         return wrapper
#
#     @logger                                     # 等价于 say_hello = logger(say_hello)
#     def say_hello(name):
#         print(f"  你好, {name}!")
#
#     say_hello("小明")
#
#     # ---- (2) 带参数的装饰器：外面再套一层 ----
#     def repeat(times):
#         def decorator(func):
#             def wrapper(*args, **kwargs):
#                 for _ in range(times):
#                     func(*args, **kwargs)
#             return wrapper
#         return decorator
#
#     @repeat(3)
#     def hi():
#         print("  Hi!")
#
#     hi()
#
#
# # %% 第 23 题 · 生成器
# # 题目：(1) count_up(n) 产出 1~n  (2) 把生成器表达式转成列表  (3) 无限斐波那契生成器取前 8 个
#
#
# def q23_generator():
#     """生成器"""
#     # 生成器：用 yield 逐个返回值，不会一次性把所有数据放到内存里（适合大数据量）
#     def count_up(n):
#         i = 1
#         while i <= n:
#             yield i          # 每次 next() 执行到 yield 就暂停
#             i += 1
#
#     print("count_up(5) ->", list(count_up(5)))
#
#     # 手动 next 观察暂停特性
#     g = count_up(3)
#     print("next:", next(g), next(g), next(g))
#     # print(next(g))   # 再取会抛 StopIteration
#
#     # 生成器表达式（把列表推导式的 [] 换成 ()）
#     gen = (x ** 2 for x in range(5))
#     print("生成器表达式:", list(gen))
#
#     # 无限斐波那契（因为是惰性的，所以永远不会内存爆炸）
#     def fib_gen():
#         a, b = 0, 1
#         while True:
#             yield a
#             a, b = b, a + b
#
#     f = fib_gen()
#     print("前 8 个斐波那契:", [next(f) for _ in range(8)])
#
#
# # ------------------------------------------------------------------------------
# # 第五部分 · 进阶与实战
# # ------------------------------------------------------------------------------
#
# # %% 第 24 题 · 推导式
# # 题目：(1) 1~10 平方 (2) 1~20 中能被 3 整除的数 (3) 平方字典 (4) 集合推导式 (5) 二维列表展平 (6) 二维列表推导
#
#
# def q24_comprehension():
#     """推导式"""
#     # 列表推导式：[表达式 for 变量 in 可迭代对象 if 条件]
#     print("1~10 平方    :", [x * x for x in range(1, 11)])
#     print("能被 3 整除  :", [x for x in range(1, 21) if x % 3 == 0])
#     print("条件表达式   :", [x if x % 2 == 0 else -x for x in range(1, 7)])
#
#     # 字典推导式
#     print("平方字典     :", {x: x ** 2 for x in range(1, 6)})
#
#     # 集合推导式（自动去重）
#     print("余数集合     :", {x % 3 for x in range(10)})
#
#     # 嵌套 / 展平二维列表
#     matrix = [[1, 2, 3], [4, 5, 6]]
#     print("展平二维列表 :", [n for row in matrix for n in row])
#
#     # 生成二维结构
#     print("乘法表二维数组:")
#     table = [[i * j for j in range(1, 5)] for i in range(1, 5)]
#     for row in table:
#         print("   ", row)
#
#
# # %% 第 25 题 · 异常处理
# # 题目：(1) divide(a, b) 处理除零并保证 finally 执行  (2) 自定义异常 ScoreError，成绩不在 0~100 时抛出并捕获
#
#
# def q25_exception():
#     """异常处理"""
#     def divide(a, b):
#         try:
#             result = a / b
#         except ZeroDivisionError as e:
#             print("  捕获到 ZeroDivisionError:", e)
#             return None
#         except (TypeError, ValueError) as e:        # 可以用元组一次捕获多种异常
#             print("  捕获到类型/值错误:", e)
#             return None
#         else:
#             print("  没有异常时执行 else")
#             return result
#         finally:
#             print("  finally：无论是否出错都会执行（常用于释放资源）")
#
#     print("divide(10, 2) ->", divide(10, 2))
#     print("divide(10, 0) ->", divide(10, 0))
#     print('divide(10, "a") ->', divide(10, "a"))
#
#     # ---- 自定义异常 ----
#     class ScoreError(Exception):
#         """自定义异常：继承 Exception 即可"""
#         pass
#
#     def check_score(score):
#         if not 0 <= score <= 100:
#             raise ScoreError(f"成绩 {score} 不合法，应在 0~100 之间")
#         return score
#
#     for s in [95, 120]:
#         try:
#             print(f"  录入成绩 {s} -> {check_score(s)}")
#         except ScoreError as e:
#             print("  捕获自定义异常:", e)
#
#
# # %% 第 26 题 · 文件读写
# # 题目：用 with open 以 UTF-8：写入 3 行 -> 整体读回 -> 按行读成列表 -> 追加一行
#
#
# def q26_file_io():
#     """文件读写"""
#     import os
#
#     # 把文件写到当前脚本所在目录，方便查看
#     dir_path = os.path.dirname(os.path.abspath(__file__))
#     path = os.path.join(dir_path, "demo_text.txt")
#     print("文件路径:", path)
#
#     # 写：mode="w" 覆盖写入。encoding="utf-8" 在 Windows 上必写，否则中文会乱码
#     with open(path, "w", encoding="utf-8") as f:
#         f.write("第一行：Python 文件读写\n")
#         f.write("第二行：with 会自动关闭文件\n")
#         f.write("第三行：不用手动 close()\n")
#
#     # 读：整个读回来
#     with open(path, "r", encoding="utf-8") as f:
#         content = f.read()
#     print("----- 整体读取 -----")
#     print(content, end="")
#
#     # 读：按行读成列表
#     with open(path, "r", encoding="utf-8") as f:
#         lines = [line.strip() for line in f]
#     print("按行读取的列表:", lines)
#
#     # 追加：mode="a"
#     with open(path, "a", encoding="utf-8") as f:
#         f.write("第四行：追加写入的内容\n")
#
#     print("追加后行数:", len(open(path, encoding="utf-8").readlines()))
#     print("文件是否存在:", os.path.exists(path))
#     print("(演示结束后文件保留在脚本同目录，可自行删除)")
#
#
# # %% 第 27 题 · 面向对象
# # 题目：(1) 父类 Animal（类属性 + __init__ + speak + __str__） (2) Dog/Cat 继承重写实现多态  (3) @property 实现封装
#
#
# def q27_oop():
#     """面向对象：类 / 继承 / 多态 / 封装"""
#     # ---------- (1) 父类 ----------
#     class Animal:
#         species = "动物"                       # 类属性，所有实例共享
#
#         def __init__(self, name, age):
#             self.name = name                   # 实例属性
#             self.age = age
#
#         def speak(self):
#             return "……"
#
#         def __str__(self):
#             """print(对象) 时调用，方便调试"""
#             return f"{self.__class__.__name__}({self.name}, {self.age}岁)"
#
#     # ---------- (2) 继承 + 重写 + 多态 ----------
#     class Dog(Animal):
#         def speak(self):
#             return "汪汪汪"
#
#     class Cat(Animal):
#         def __init__(self, name, age):
#             super().__init__(name, age)        # 调用父类构造方法
#             self.lives = 9
#
#         def speak(self):
#             return "喵喵喵"
#
#     animals = [Dog("旺财", 3), Cat("咪咪", 2)]
#     for a in animals:
#         # 同一个 speak() 调用，不同子类表现出不同行为 —— 这就是多态
#         print(f"  {a} -> {a.speak()}")
#     print("  类属性 species =", Animal.species)
#
#     # ---------- (3) 封装：@property ----------
#     class Student:
#         def __init__(self, name, score):
#             self.name = name
#             self._score = None
#             self.score = score                 # 走下面的 setter，做数据校验
#
#         @property
#         def score(self):
#             """读的时候像访问属性一样：stu.score"""
#             return self._score
#
#         @score.setter
#         def score(self, value):
#             """写的时候自动校验：stu.score = 120 会报错"""
#             if not 0 <= value <= 100:
#                 raise ValueError(f"成绩 {value} 不合法")
#             self._score = value
#
#     stu = Student("小红", 95)
#     print(f"  {stu.name} 的成绩: {stu.score}")   # 不用写 stu.score()
#     stu.score = 98
#     print(f"  修改后: {stu.score}")
#     try:
#         stu.score = 120
#     except ValueError as e:
#         print("  捕获到校验失败:", e)
#
#
# # %% 第 28 题 · 模块与标准库
# # 题目：演示 math / random / datetime，以及 from collections import Counter, defaultdict
#
#
# def q28_modules():
#     """模块与常用标准库"""
#     import math
#     import random
#     import datetime
#
#     print("math  :", math.pi, math.sqrt(16), math.floor(3.7), math.ceil(3.2))
#     print("math  :", round(math.sqrt(2), 4), math.pow(2, 10))
#
#     random.seed(42)                            # 固定随机种子，保证每次运行结果一样
#     print("random:", random.randint(1, 10), random.choice(["石头", "剪刀", "布"]))
#     print("random:", [random.randint(1, 6) for _ in range(5)], "（5 个骰子）")
#
#     today = datetime.date.today()
#     now = datetime.datetime.now()
#     print("日期  :", today)
#     print("时间  :", now.strftime("%Y-%m-%d %H:%M:%S"))
#     print("格式化:", today.strftime("%Y年%m月%d日"))
#     tomorrow = today + datetime.timedelta(days=1)
#     print("明天  :", tomorrow)
#
#     from collections import Counter, defaultdict
#     print("Counter     :", Counter("aabbc").most_common())
#     # defaultdict：访问不存在的键时自动创建默认值，省掉一堆 if
#     groups = defaultdict(list)
#     for name, cls in [("小明", "一班"), ("小红", "二班"), ("小刚", "一班")]:
#         groups[cls].append(name)
#     print("defaultdict :", dict(groups))
#
#
# # %% 第 29 题 · 常用内置函数
# # 题目：names = ["小明","小红","小刚"] 与 scores = [88,95,76] 配对输出编号成绩单，并演示 any/all
#
#
# def q29_builtins():
#     """常用内置函数：zip / enumerate / any / all"""
#     names = ["小明", "小红", "小刚"]
#     scores = [88, 95, 76]
#
#     # zip：把多个列表"拉链"式配对，长度取最短的那个
#     print("成绩单:")
#     for i, (name, score) in enumerate(zip(names, scores), start=1):
#         print(f"  {i}. {name}  {score} 分")
#
#     print("直接转字典:", dict(zip(names, scores)))
#
#     # any：只要有一个为 True 就返回 True；all：全部为 True 才返回 True
#     print("有人 >= 90 吗:", any(s >= 90 for s in scores))
#     print("全部 >= 60 吗:", all(s >= 60 for s in scores))
#     print("全部 >= 80 吗:", all(s >= 80 for s in scores))
#
#     # 其他常用内置函数
#     print("max/min/sum/len:", max(scores), min(scores), sum(scores), len(scores))
#     print("reversed:", list(reversed(names)))
#     print("sorted  :", sorted(names, key=len, reverse=True))
#
#
# # %% 第 30 题 · 综合实战：学生成绩管理
# # 题目：输出排名榜、平均分、最高分、优秀名单（>=90）、不及格名单（<60），并用字典实现快速查分
#
#
# def q30_student_manager():
#     """综合实战：学生成绩管理"""
#     students = [
#         {"name": "小明", "score": 88},
#         {"name": "小红", "score": 95},
#         {"name": "小刚", "score": 76},
#         {"name": "小美", "score": 92},
#         {"name": "小强", "score": 55},
#     ]
#
#     # 1. 排名榜（按成绩降序）
#     ranked = sorted(students, key=lambda s: s["score"], reverse=True)
#     print("----- 成绩排名榜 -----")
#     for i, s in enumerate(ranked, start=1):
#         print(f"  第 {i} 名  {s['name']:<4} {s['score']} 分")
#
#     # 2. 统计信息
#     scores = [s["score"] for s in students]       # 列表推导式
#     avg = sum(scores) / len(scores)
#     top = max(students, key=lambda s: s["score"])
#     low = min(students, key=lambda s: s["score"])
#
#     print("----- 统计信息 -----")
#     print(f"  平均分: {avg:.2f}")
#     print(f"  最高分: {top['name']} {top['score']} 分")
#     print(f"  最低分: {low['name']} {low['score']} 分")
#
#     # 3. 分类名单
#     excellent = [s["name"] for s in students if s["score"] >= 90]
#     fail = [s["name"] for s in students if s["score"] < 60]
#
#     print("----- 分类名单 -----")
#     print(f"  优秀(>=90): {', '.join(excellent) if excellent else '无'}")
#     print(f"  不及格(<60): {', '.join(fail) if fail else '无'}")
#
#     # 4. 加分项：用字典快速查分
#     score_map = {s["name"]: s["score"] for s in students}
#     print("----- 快速查分 -----")
#     print("  小美:", score_map.get("小美", "查无此人"))
#     print("  小李:", score_map.get("小李", "查无此人"))
#
#
# # ==============================================================================
# #                          程 序 入 口
# # ==============================================================================
#
# ANSWERS = [
#     q01_swap, q02_data_types, q03_reverse_palindrome, q04_format, q05_str_methods,
#     q06_dedup, q07_stats, q08_sort, q09_slice, q10_dict_ops, q11_count_chars, q12_set_ops,
#     q13_leap_year, q14_multiplication_table, q15_fibonacci, q16_prime,
#     q17_narcissistic, q18_guess_number,
#     q19_func_params, q20_factorial, q21_lambda_map_filter, q22_decorator, q23_generator,
#     q24_comprehension, q25_exception, q26_file_io, q27_oop, q28_modules, q29_builtins,
#     q30_student_manager,
# ]
#
#
# if __name__ == "__main__":
#     # ------------------------------------------------------------------
#     # 想单独练习某几道题时：
#     #   1. 把 RUN_ALL 改成 False
#     #   2. 在 SELECTED 里写上题号，例如 {1, 6, 24}
#     # ------------------------------------------------------------------
#     RUN_ALL = True
#     SELECTED = {1, 6, 24}
#
#     passed, failed = 0, []
#
#     for func in ANSWERS:
#         no = int(func.__name__[1:3])
#         if not RUN_ALL and no not in SELECTED:
#             continue
#
#         print("\n" + "=" * 72)
#         print(f"  答案 {no:02d}  ·  {func.__doc__}")
#         print("=" * 72)
#         try:
#             func()
#             passed += 1
#         except Exception as exc:                       # 防止某一题出错导致后面全跑不了
#             failed.append((no, repr(exc)))
#             print(f"  [ERROR] 运行出错: {exc!r}")
#
#     print("\n" + "-" * 72)
#     print(f"运行结束：成功 {passed} 题，失败 {len(failed)} 题 {failed if failed else ''}")
#     print("-" * 72)
