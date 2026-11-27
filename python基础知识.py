#调试功能：开始键右边的那个小虫子
#设置断点：在要设置断点的地方用鼠标点击左侧数字和代码中间的空白处，再点一下取消断点
#以下是在debug状态下，点击小虫子
#调试功能下各个按键功能：
#1.运行到光标处：跳到下一个断点位置
#2.代码为蓝色表示即将要运行的代码、
#3.显示执行点：python代码是一行行执行，直到遇到报错，此键可以帮助查询代码此时运行到了哪里
#4.对表达式求值：求值，不用加等于号

#Ctrl+/可以添加注释，也可以取消，使用的是单行（井号）注释
# ctrl+f 查找代码
# ctrl+d 复制到下一行
# ctrl+z：撤回到上一步，用于不小心把代码删了
# print("哈哈哈","hiahiahia")
# 同时输出多个值，用逗号隔开
# sep写在括号里，前面用都好隔开：表示输出内容用什么隔开（放在后面）↓
# print("123","234","345",sep = ",")
#end用来设定以什么结尾，设置默认值是换行符 ’\n'，可以切换成其他字符串
# print("hello world",end = ',')
# print("hello world")
#变量只能由数字，字母和_（下划线）
#不能由数字开头

#int：任意大小整数  float 浮点数：小数    bool布尔型：有固定写法，True 和 False  complex复数型： z = a + bj（固定写法 a，b可以变，j是虚数单位
#字符串类型str：单引号、双引号
#布尔值可以当整型  True当作整数1 ， False当作整数0  print(True + True) → = 2

# type:# 检测变量的类型  print(type(变量名))

#格式化输出
#占位符：生成一定格式的字符串，只是占据位置，不会被输出
# %s:字符串  %d：整数
# age = 18
# name = 'wa'
# print("我的名字是：%s， 年龄是：%d" %(name,age))
# a = 123
# print("%d" % a)
# print("%06d" % a)
# print("%02d" % a) #表示输出的整数显示位数，不足的话在前面用0补全，超过当前位数则原样输出

# # %f 浮点数（常用）
# b = 1.2345678
# print("%f" % a)
# print("%f" % b)#默认写出后六位小数，遵循四舍五入原则

# # %.Xf 浮点数 (X表示保留几位小数）X的值超出这个小数有的位数则补0
# #数字设置小数位数，遵循四舍五入
# c = 2.34567
# print("%.3f" % c)
# print("%.4f" % c)

# # %%  占位符
# print("我是%%的1%%" % ())
# # f格式化   格式为：f"(表达式)"
# name = "keee"
# age = "19"
# print(f"My name is {name}, and I am {age} years old" )

#运算符 //：取整除（向下取整，直接忽略小数，无四舍五入原则） ！ 若有浮点数，则结果以浮点数表示
#/： 结果为浮点数
# %：取余除（取余数）   “5 % 2 = 1”
# **：取幂
#优先级：幂＞乘除＞加

#简便运算
# a = 10
# a += 10 # 相当于a = a + 10 ，此时a = 20， “+-*%/  ** ”同理

# 输入函数input()
# a = input("请输入文本：")
# print("你输入的文本为：",a)

# 转义字符
# \t  制表符，表示空四个字符（缩进）
# print("nihao\ta")
# print("nihaoa")
# \n  换行符：后面的内容换行
# print("你好世界")
# print("你好\n世界")
# \r 回车： 表示将当前位置移到开头，将\r后面的内容移到前面，前面的内容没有了
# print("FiveStar ")
# print("Five\rStar ")
# \\ 反斜杠符号：看示例↓  “\"一般为转义字符，不会打印出来，但如果想要打印\，就可以用\\反斜杠
# print("你好\t啊")
# print("你好\\t啊")
# print("你好\\\t啊")
# print("你好\\啊") # 两个\\打印出来一个\， \\\t：可以理解为\\(打印出一个\) + \t(缩进)
# 字符串前面加一个r（原生字符串），默认后面代码的字符串不转义
# print(r"没有转义你会看到:Fi\rve\tSta\nrs")
# print("转义之后你会看到:↓")
# print("Fi\rve\tSta\nrs")

# if判断 格式： if (条件):
# age = 18
# if age >= 18:
#     print("你已成年")

# 比较判断符： !=，==，<, >, <=, >=   返回值为True和False
# a = 10
# b = 20
# print(a > b)
# print(a <= b)

# 逻辑运算符： and（与）, or（或）, not（非）
# and:两边都符合才为真    or:左右两边有一个符合为真，两个都为假则为假    not:表示相反的结果
# print(3 > 9)
# print(not 3 > 9)

# 三目运算（三元表达式）： 如果条件为真，则执行if下的代码， 如果条件为假， 则执行else下的代码，elif为if之下第二次判断
# a = int(input("请输入第一个数："))
# b = int(input("请输入第二个数："))
# if a > b :
#     print("第一个数大于第二个数")
# elif a == b:
#     print("这俩数一样大")
# else:
#     print("第一个数小于第二个数")

# if, else的诡异写法（一般别用，会搞混）：格式：（条件为真时执行的代码）if 判断 else （条件为假时执行的代码）
# a = input("请输入第一个数：")
# b = input("请输入第二个数：")
# print("第一个数大于等于第二个数") if a >= b else print("第一个数小于第二个数")


#报错提示：
# SyntaxError：语法有问题
# invalid syntax：无效语法  （例如if没有加冒号）
# IndexError: 索引有问题
# string index out of range：字符串超出索引范围
# ValueError: 值错误，不存在这个值

# 循环 for, while
# while 循环
# 死循环 while True:  另：   while 任意不是0的数字：无限循环while下面的内容
# while False: = while 0:
# while 条件:
#     循环内容
# i = 1
# while i <= 10:
#     i += 1
#     print(i)

# for循环
# for 临时变量 in 可迭代对象:
#       循环体
# 可迭代对象：字符串、元组、集合、列表等（序列类型）
# str = "这是一个可迭代对象"
# for i in str:
#     print(i)
# range() 记录循环次数，相当于计数器
# range(start, stop, step) # i的起点， i的终点， i每一次增加多少（包前不包后原则）
# for j in range(1, 11, 2):  # 从1开始，从11-1=10结束，因此结果不会有11（包前不包后原则）
#     print(j)
# for i in range(5):         # 只写一个数，默认从0开始，步长为1
#     print(i)

# break与continue (只能放在循环里面)
# break退出循环：    疯狂干饭人案例：
# rice = 1
# while rice <= 5:
#     print(f"我在吃第{rice}碗米饭")
#     if rice == 3:
#         print("毁了，吃不下了")
#         break
#     rice += 1

# continue ：退出本次循环，下一次循环继续执行
# 要在continue之前修改计数器，否则必定陷入死循环
# rice = 1
# while rice <= 5:
#     print(f"我在吃第{rice}碗米饭")
#     if rice == 3:
#         print("孩子们，这碗没煮熟")
#         rice += 1   # 要在这里先修改计数器,相当于在rice = 3时单独加了一个rice += 1
#         continue    # 这个continue会在i == 3 时把下面那个rice += 1也给跳过
#     rice += 1

# 字符串编码：本质上是二进制数据与与语言文字的一一对应关系
# Unicode: 所有字符都是2个字节
# UTF-8: 对不同字符用不同的长度表示

# 字符串编码转换
# 编码encode()        解码decode()
# a = 'hello'
# print(a, type(a))
# b = a.encode()         # 用一个变量来储存编码后的结果
# print(b, type(b))      # bytes以字节为单位进行处理的
# c = b.decode()
# print(c, type(c))      # 解码后回到原来的字符串
# py = '严肃学习中'
# py1 = py.encode('utf-8') # 一般python设定默认为UTF-8，因此加不加效果都一样，但个别配置环境不一样，加了可以适配更多不确定环境
# print(py1, type(py1))

# 字符串常见操作
# 加号，字符串拼接
# print("10" + "10")
# 乘号，字符串重复输出
# print("无敌了" * 4)

# 成员运算符：检测某个字符串内是否包含某个字符或某个字符串
# in :包含则返回True,不包含则返回False
# not in :相反
# a = "apple"
# print("p" in a)     # 返回True
# print("c" not in a) # 返回True
# print("ape" in a)   # 返回False，把ape作为整体去检测

# 下标：Python的下标从0开始 （通过下标快速找到对应的数据）
# 格式： 字符串名[下标值]
# a = "python"
# print(a[2])      # 返回从左到右数第三个字符
# print(a[-1])     # -1的下标表示从右往左数第1个,会输出n
# print(a[6])      # 会报错。超出索引范围了,正负同理

# 切片：对操作的对象截取其中一部分的操作   （包前不包后原则）
# 格式：变量名[开始位置:结束位置:步长]     # 是冒号
# a = 'abcdefg'
# print(a[2:5])       # 不填步长默认为1，步长>0，则从左往右取
# print(a[::2])       # 不填起始默认为收尾
# print(a[3:])        # 加个冒号后面不填默认到结尾
# print(a[:5])        # 加个冒号前面不填默认从头开始，且不包含结尾
# 起始位置要和切取方向一致，否则就是空的


# 字符串常见操作
# 查找元素 find: 检测某一个子字符串是否包含在字符串中，如果在就返回子字符串的下标，否则就返回-1
# fing(要找的字符串,开始位置下标,结束位置下标)         （包前不包后原则）
# 起始位置可以省略，则默认为全部字符串
# name = "Fivestars"
# print(name.find('s'))     # 检测第一个s
# print(name.find('Five'))  # 检测到第一个字符串的第一个字母的下标为该字符串的下标
# print(name.find('s',5))   # 从第六个字符开始查找
# print(name.find('s',5,6)) # 没找到就返回-1

# index：检测某一个子字符串是否包含在字符串中，如果在就返回子字符串的下标，否则就会报错
# index(要找的字符串,开始位置下标,结束位置下标)       （包前不包后原则）
# 起始位置可以省略，则默认为全部字符串
# name = "Fivestars"
# print(name.index('s'))          # 返回4
# print(name.index('s',5,6))      # 会报错

# count: 返回某个子字符串在整个字符串中出现的次数，没有就返回0
# count(要数的字符串,开始位置下标,结束位置下标)       （包前不包后原则）
# name = "Fivestars"
# print(name.count('s'))      # 返回2
# print(name.count('a'))      # 未出现过，返回0
# print(name.count('s',5, 6)) # 返回0

# startswith:  是否以某个字符开头，是则返回True，不是则返回False
# startswith(子字符串,开始位置下标,结束位置下标)      （包前不包后原则）
# name = "Fivestars"
# print(name.startswith("Fiv"))           # 是否以Fiv开头，返回True
# 其他同上

# isupper： 检测字符串中所有的字母是否都为大写，是的话就返回True
# st = "Four people"
# print(st.isupper())

# replace: 替换
# 格式： replace(旧内容,新内容,替换次数)
# 替换次数：替换多少个，不填默认全部替换
# name = 'Blowing wind'
# print(name.replace("wind","cloud"))
# py1 = "angry angry apple"
# print(py1.replace("a","b",1))           # 只替换第一个

# split: 指定分隔符来切字符串，并以列表的形式返回
# 格式： split("指定的字符串",指的是第几个字符)
# st = "hello,world"
# print(st.split(","))        # 以逗号为划分
# print(st.split("a"))        # 没有则整体为一个列表
# print(st.split("o",2))      # 以第二个2划分

# capitalize： 使第一个字符大写
# st = "binbin"
# print(st.capitalize())      # 只大写第一个字符

# 其他常见操作
# lower：全部大写字母转为小写
# upper: 全部小写字母转为大写
# endswith：检测是否以某个字符结尾

# 将字符中的所有字符倒过来再拼在一起
# a = 'kskbl'
# b = a[::-1]    # 把a倒过来就是'lbksk'
# print(c)


# 列表
# 格式：列表名 = [元素1,元素2,元素3... ]
# 元素之间的数据类型可以各不相同

# 列表的常见操作
# 添加元素
# lis = ["one","two","three"]
# # append():整体添加
# lis.append("four")          # 先单独进行添加，把“four”整体添加到列表
# print(lis)                  # 再打印
# # extend(): 分散添加
# lis.extend("four")          # 同样先单独写一行，把f,o,u,r分开添加
# print(lis)
# # insert(): 在指定位置整体插入元素，原来位置已经有元素，则该位置的元素往后移
# lis.insert(2,"five")        # 整体插入，不会分开
# print(lis)
# lis.append(4)                 # 会报错，添加内容必须为可迭代对象
# lis.extend(4)                 # 会报错，添加内容必须为可迭代对象
# lis.insert(2,4)                 # 不会报错，可以添加整型
# print(lis)

# join 插到中间
# ls = ["1","3","4"]
# a = "2"
# b = a.join(ls)
# print(b)                # 把2插入到13和34里面

# 修改元素：直接通过下标就可以进行修改
# 格式: 列表名[下标] = 要修改的内容
# li = [1,2,3]
# li[2] = "a"         # 直接修改第三项
# print(li)

# 查找元素
# in,   not in： 与在字符串中的用法一样
# li = [1,2,3]
# print(1 in li)          # 返回True

# 案列：用户输入昵称，昵称重复则不能使用（用于游戏账户注册时id的重复性检测）
# Name_List = []
# while True:
#     name = str(input("Enter your name: "))
#     if name in Name_List:
#         print("Your name already exists")
#         continue
#     else:
#         Name_List.append(name)
#         break

# ***
# 输入一串数字，并将这一串数字以列表形式保存
# nums = list(map(int,input().split()))     # split()以空格隔开

# index, count：用法与在字符串中相同
# li = [1,2,3]
# print(li.index(2))      # 返回下标1

# 删除元素
# del
# li = [1,2,3,4]
# del li           # 该操作就是删除列表,此时若打印就会报错
# del li[2]        # 根据下标来删除
# print(li)

# pop: 删除指定下标的数据，默认删除最后一个元素
# li = [1,2,3,4]
# li.pop()          # 默认删除最后一个元素
# li.pop(2)         # 只能根据下标来删除，不能指定元素
# li.pop(3)         # 超出范围会报错
# print(li)

# remove: 根据元素的值进行删除
# li = [1,2,3,4]
# li.remove(1)        # 默认删除第一个指定元素
# li.remove(5)        # 会报错，列表中不存在这个值
# print(li)

# 排序
# sort：将列表按特定顺序重新排列，默认从小到大
# li = [1,4,3,8,2]
# li.sort()
# print(li)

# reverse： 倒叙，将列表倒置过来
# li = [1,4,3,8,2]
# li.reverse()    # 直接把整个列表反过来
# print(li)

# 列表推导式
# 格式一： [表达式 for 变量 in 列表]    *in后面可以放range()，可迭代对象等
# li = [1,2,3,4,5,6]
# [print(i) for i in li]
# li = []
# for i in range(1,6):
#     li.append(i)
# print(li)
# # 用列表推导式编写
# li = []
# [li.append(i) for i in range(1,6)]
# print(li)

# 格式二： [表达式 for 变量 in 列表 if 条件]
# 把奇数放进列表
# li = []
# [li.append(i) for i in range(1,6) if i % 2 == 1]
# print(li)

# # enumerate()   同时取出列表的元素和下标
# lst =[83,84,85,86,87,88]
# for index, value in enumerate(lst):
#     print(index)            # 打印出元素的下标
#     print(value)            # 打印出元素值

# 列表嵌套：一个列表里面又有一个列表
# li = [1,2,3,4,[1,2,3,4]]
# print(li[4][2])             # [4]表示取出列表，[2]表示取出内列表里的元素，超出就会报错

# 元组
# 基本格式： YZ = (1,2,3)
# 如果只有一个元素，末尾要加逗号，多个元素用逗号隔开，不同元素可以为不同类型
# tua = (1)
# tub = (1,)
# tuc = ("str")
# print(type(tua))        # 返回的是整数类型
# print(type(tub))        # 返回的是元组类型
# print(type(tuc))        # 返回的是字符串类型

# 元组只可以查询，不可以增删改操作
# 查询: 元组名[下标]
# count(), index(), len()用法与列表一致
# len()的用法： len(列表、元组名)
# tu = (1,2,3)
# print(len(tu))

# 元组也可以进行切片操作
# tu = [1,4,2,7,3,1]
# print(tu[2:])       # 从第三项开始往后切

# 元组的应用场景：
# 函数的参数与返回值
# 格式化输出后面的()本质就是一个元组
# name = "waaaa"
# age = 19
# print("我的名字是：%s， 年龄是：%d" % (name, age))
# info = ("waaaa", 19)
# print("我的名字是：%s， 年龄是：%d" % info)
# 数据不能被修改时，可以保护数据安全

# 字典
#格式: 字典名 = {键1：值1，键2：值2...}         键不能重复，值可以，键重复会用后面的值覆盖前面的值
# dic = {"name":"wa", "age":19}
# print(dic)

# 字典的增删改查
# 查看元素
# 格式一：变量名[键名]        字典中不可以根据下标查找
# dic = {"name":"wa", "age":19}
# print(dic["name"])          # 根据键名查看对应的值， 键名不存在时会报错
# # 格式二：变量名.get(键名)
# print(dic.get("name"))      # 键名不存在时返回none
# # get(键名,返回值)            # 返回的内容时当键名不存在时返回的内容
# print(dic.get("sex", "没找到"))    # 不存在，返回自己设置的默认值

# 修改元素
# 字典名[键名] = 修改的内容
# dic = {"name":"wa", "age":19}
# dic['age'] = 20         # 字典通过键名修改
# print(dic)

# 添加元素
# dic = {"name":"wa", "age":19}
# dic["tel"] = 110     # 注意：键名存在就是修改元素，不存在就是新增元素
# print(dic)
# dic["tel"] = 120     # 此时已经有了"tel"，那就是修改操作
# print(dic)

# 删除元素
# del
# 删除整个字典：    del 字典名
# dic = {"name":"wa", "age":19}
# del dic                     # 此时已经完成删除字典了，此时再打印字典就会报错
# 删除指定的键值对，键名不存在就会报错    del 字典名[键名]
# dic = {"name":"wa", "age":19}
# del dic["name"]             # 删掉了name的键值对
# print(dic)

# clear:清空整个字典里面的东西，但是保留了这个字典
# 格式：字典名.clear()
# dic = {"name":"wa", "age":19}
# dic.clear()                 # 把name和age对应的键值对删掉，但是dic字典本身保留，此时dic字典为空字典
# print(dic)                  # 打印不会报错

# pop:删除指定键值对，键不存在就会报错
# 格式：字典名.pop(键名)
# dic = {"name":"wa", "age":19}
# dic.pop("name")             # 不存在的键名或没有写键名，会报错
# dic.popitem()               # 什么都不用写，默认删除最后一个，其他方法与pop同理
# print(dic)


# 字典常见操作
# len()求字典长度
# dic = {"name":"wa", "age":19}
# print(len(dic))         # 返回键值对的数量

# keys(): 返回字典里面包含的所有键名
# dic = {"name":"wa", "age":19, "tel": 110}
# print(dic.keys())           # 返回的不是列表，可以通过for循环取出来
# for i in dic.keys():        # 代表只取出键名，没有.keys()，也会取出键名，不会取出值
#     print(i)

# values()：返回字典里面包含的所有值
# dic = {"name":"wa", "age":19, "tel": 110}
# print(dic.values())
# for i in dic.values():          # 同样可以用for循环取出值
#     print(i)

# items() ： 返回字典里面包含的所有键值对，以元组的形式
# dic = {"name":"wa", "age":19, "tel": 110}
# print(dic.items())
# for i in dic.items():
#     print(i)                # i是元组类型

# 字典的应用场景
# 使用键值对，存储描述一个物体的相关信息


# 集合 set
# 基本格式： 集合名 = {元素1, 元素2, 元素3...}
# s1 = {1, 2, 3, 4}           # 定义一个集合
# s2 = {}                     # 定义一个空字典
# s3 = set()                  # 定义一个空集合

# 集合具有无序性：不能修改其中的值
# s1 = {"a","b","c","d","e"}
# print(s1)                     # 字符串组成每一次运行结果都不一样
# s2 = {1,2,3,4,5}
# print(s2)                     # 数字组成每次运行结果一样
# s3 = {"c",1,"a",2,3,"b","d","e"}
# print(s3)                     # 数字部分不会变，但字符串部分会变，字符串会穿插在数字左右

# 集合无序的实现方式设计hash表（了解）
# print(hash("a"))
# print(hash("b"))
# print(hash("c"))              # 会发现每一次打印的数字不同，在hash表中对应的位置也不同，因此是无序的
# print(hash(1))
# print(hash(2))
# print(hash(3))                # 整型的hash值就是其本身，不会发生改变

# # 集合具有唯一性，可以自动去重
# s1 = {1,5,8,2,4,6,4}
# print(s1)                       # 自动去重

# 集合的常见操作
# 添加元素:
# add 添加整体
# s1 = {1, 5, 8, 2, 4, 6}
# s1.add(7)                       # 一次只能添加一个元素
# s1.add(1)                       # 添加的数原集合已经存在，则不会添加
# print(s1)
# update:把传入的元素拆分一个个放入集合
# s1 = {1, 5, 8, 2, 4, 6}
# s1.update([1,2,3])                # 里面要放一个可迭代对象
# # 里面放元组，集合，列表，效果一样，放字典则会把键值放进去
# print(s1)

# 删除元素
# remove: 选择删除的元素，如果集合中有就会删除，没有就会报错
# s1 = {1, 5, 8, 2, 4, 6}
# s1.remove(2)
# print(s1)

# pop：直接删除
# s1 = {1, 5, 8, 2, 4, 6}
# s1.pop()                # 默认删除第一个数字
# print(s1)
# s2 = {"c",1,"a",2,3,"b","d","e"}
# s2.pop()                # 根据排序后的hash表删除第一个数据，及随机删除
# print(s2)

# discard： 选择要删除的元素，有就删除，没有不会报错，不会进行任何操作
# s1 = {"c",1,"a",2,3,"b","d","e"}
# s1.discard(3)
# print(s1)

# 交集与并集
# 交集：&
# a = {1, 2, 3, 4}
# b = {2, 3, 4, 5, 6}
# c = {7,8,9,10}
# print(a&b)
# print(a & c)             # 如果两个集合没有交集，则返回set(), 表示空集合
# 并集：|
# a = {1, 2, 3, 4}
# b = {2, 3, 4, 5, 6}
# c = {7,8,9,10}
# print(a | b)             # 重复的部分不会再算
# print(a | c)

# 类型转换
# int() 把纯数字组成的字符串转换为整数，将浮点型转为整型向下取整
# str() 可以把任何类型转换为字符串类型，列表也可以
# float() 将整型转换为浮点型，在后面添加一位小数
# eval() 把传入的字符串当作表达式来执行，并返回表达式的结果,两个字符串相加没办法使用
# +/-写在前面表示正负号，否则表示加减
# a = str(10+10)
# print(type(a))
# b = eval(a)         # 把"10+10"转换成10+10
# print(b)
# eval可以实现列表，字典，元组和str之间的转换： eval(str)
# eval() 非常强大，但是不够安全，容易被恶意修改数据

# list()：将可迭代对象转换为列表
# 支持转换为list的类型： str, tuple, dict, set
# print(list("abcdefg"))                    # 字符串-列表：每个元素拆分成列表的每一项
# print(list((1,2,3,4)))                    # 元组-列表：把元组转换成列表
# print(list({"name":"wa", "age":19}))      # 字典-列表：把字典转换为列表，只会将键值转换
# print(list({1, 2, 3, 4, "a", "d"}))    # 集合-列表：先去重，再转换，并且会有无序


# 赋值：等于完全共享资源，一个值的改变会被另一个值共享
# li = [1,2,3,4]
# li2 = li            # 将li的值赋值给li2
# print(li)
# print(li2)
# li.append(5)
# print(li)
# print(li2)          # 将li改变之后，li2也会随之改变

# 浅拷贝：会创建新的对象，拷贝第一层数据，嵌套层会指向原来的内存地址，就是第一层列表内存地址不一样，第二层列表内存地址一样
# 一般用浅拷贝，速度快，空间校，效率高  （数据半共享）
# import copy         # 导入copy模块
# li = [1,2,3,[4,5,6]]
# li2 = copy.copy(li)
# print(li)
# print(li2)
# print(id(li))
# print(id(li2))                  # 查看内存地址
# 内存地址不一样，说明不是同一个对象， 赋值的内存地址是一样的
# li.append(8)
# print(li)
# print(li2)          # 浅拷贝第二个列表不会添加8
# li[3].append(7)       # 在嵌套列表里添加元素
# print(li)
# print(li2)            # 会发现两个列表都添加了元素：因为这两个列表的嵌套列表的地址是一样的，说明是一个对象

# 深拷贝：外层对象和内部的元素都拷贝了一边
# 只影响自己本身，跟原来的对象meiyou关联  （数据不共享）
# import copy
# li = [1,2,3,[4,5,6]]
# li2 = copy.deepcopy(li)             # deepcopy深拷贝
# print(li)
# print(li2)
# print(id(li))
# print(id(li2))                      # 不同说明两个是独立的对象
# li.append(8)
# print(li)
# print(li2)
# li2.append(7)
# print(li)
# print(li2)                          # 不论改哪个都只有自己本身发生变化

# 可变对象：存储空间保存的数据允许被修改（列表，字典，集合）
# 变量对应的值可以修改，但是内存地址不会发生改变
# li = [1,2,3,4]
# print(li)
# print(id(li))
# li.append(5)
# print(li)
# print(id(li))               # 变量的值会发生改变，但对应的地址不会

# 不可变对象 存储空间保存的数据不允许被修改 ，修改的话就会生成新的值，从而分配新的生存空间
# 不可变对象：（数值类型，字符串，元组）
# 数值类型
# n = 10
# print(id(n))
# n = 15
# print(id(n))            # 修改之后内存地址就会改变

# 元组
# tua = (1,2,3)
# print(tua,id(tua))
# # 不支持增删改
# tua = ("a","b","c")
# print(tua,id(tua))          # 相当于生成了另一个对象

# 深浅拷贝只针对可变对象



# 函数：将独立的代码块组织成一个整体，使其具有特殊功能的代码集，增加代码的复用性，提高程序编写效率
# 定义函数   结构： def 函数名():
# 调用函数   结构： 函数名()
# def login():
#     print("这是一个函数")         # 设置一个函数
# login()                         # 调用这个函数，调用几次就运行几次，每次调用函数都会从头开始执行

# 案例：编写一个打招呼的函数并使用它
# def greeting():
#     print("你好!")
# a = input("请问好：")
# if a == "你好":
#     greeting()                # 调用函数前必须保证函数存在

# 返回值return：函数执行结束后，最后给调用者的一个结果
# ①return会给函数的执行者一个返回值
# def buy():
#     return "一个苹果"
# print(buy())            # 函数名()单独使用视为调用，也可以看作是一个返回值,打印返回值不需要调用
# ②函数中遇到return表示此函数结束了，不继续执行
# def buy():
#     return "一个苹果"
#     return 20
# print(buy())                        # 只打印了"一个苹果"，此时函数已经结束，20不会打印
# def buy():
#     return "一个苹果",20, "可口的"     # 若想要返回两个值，在return后面用逗号隔开，并且以元组形式返回
# print(buy())
# def buy():
#     return                          # 若一个返回值都没有就返回None
# print(buy())

# 参数
# 定义函数： def 函数名(形参a, 形参b):           形参只在这个函数内有效，是个变量
# 调用函数   函数名(实参a, 实参b)               具体的值
# def add(a, b):
#     return a+b
# print(add(1, 2))                       返回1+2的值

# 函数参数
# 必备参数(位置参数):传递和定义参数的顺序和个数必须一致
# 格式 def func(a,b):         写几个，传几个
# def info(name, age, tel):
#     print(f"My name is {name}. I am {age} years old, and my phone number is {tel}")
# info("zk", 19, 147)

# 默认参数：为参数提供默认值，调用函数时可不传该默认函数的值
# 注意：所有的位置参数必须出现在默认参数前，包括函数的定义和调用
# 格式： def 函数名(a = 12):
# def funb(b, a = 8):           # 位置参数b必须在默认参数a = 8前面，否则会报错
#     print(a)
# funb()                  # 没有报错：因为一开始已经默认传值了，a = 8就是默认参数
# funb(200)               # 如果传值，就会根据传入值执行代码

# 可变参数：传入的值的数量可以改变，可以传入多个，也可以不传
# 格式： def func(*args):        # 可以把args改成其他参数名a,b等，但args更符合代码规范性
# def func (*args):               # 星号必须有，具有特殊含义,否则就是必备参数
#     print(args)                 # 以元组形式接受
# func(1)
# func(1,3)
# func()                          # 传几个值都可以

# 关键字参数
# 格式： def func(**kwargs):           # kwargs只是一个形参
# def funb(**kwargs):
#     print(kwargs)
# funb()                                # 返回一个字典，以字典接受
# funb(name = "zk", age = 19)           # 要以字典形式传值
# 可以扩展函数的功能

# 函数嵌套
# 嵌套调用：在一个函数里面调用另外一个函数
# def study():
#     print("学习ing")
# def course():
#     study()
#     print("python")
# # 调用
# course()

# 嵌套定义： 在一个函数里面定义另一个函数
# def study():
#     print("学习ing")
#     def course():
#         print("学习python")
#         # study()               # 不要在内函数调用外函数，否则超过最大递归深度就会报错（报错原因：超过最大递归深度
#     course()
# study()

# 作用域： 变量生效的范围
# 全局变量&局部变量： 命名相同时也不会被覆盖
# 全局变量：函数外部定义的变量，在整个文件中都是有效的
# a = 100     # 全局变量
# def tes():
#     a = 120         # 局部变量
#     print(a)
# print(a)                    # a不会被覆盖，因为函数内部要使用变量，先从函数内部找，有的话直接使用，没有的话就从函数外面找
# tes()

# 局部变量：函数内部定义的变量，从定义位置开始到函数定义结束位置有效
# 在函数体内部临时保存数据，函数结束后会销毁这个变量
# def func():
#     a = 10
#     print(a)
# func()
# print(a)        # 函数内部定义的变量在函数外部不能使用，会报错

# global: 在函数内修改全局变量的值，将局部变量声明为全局变量
# 格式： global 变量名                # 写在前面
# a = 20
# b = 30
# def func():
#     global a                    # 声明这个函数下的a为全局变量，修改a就是修改全局变量a
#     a = 120
#     b = 130
#     print(a)
#     print(b)
# func()
# print(a)                        # 此时全局a已经被改为120
# print(b)                        # 全局b并不是130，仍然为30
# 案例
# def study():
#     global name                   # 声明部分要在定义前面
#     name = '学习Pyhton基础'
#     print(f'我们在{name}')
# study()
# print(name)

# nonlocal： 将变量声明为外层变量（外层函数的局部变量，且不能是全局变量）
# 只能在嵌套函数中使用，在外部函数先进行声明。内部函数进行nonlocal声明
# a = 10                         # 全局变量
# def outer():                   # 外函数
#     a = 5                      # 局部变量
#     def inner():               # 内函数
#         nonlocal a             # nonlocal会对上一级进行修改，即对outer()的a修改
#         a = 20
#         def inner2():          # 三级嵌套，由内向外
#             nonlocal a
#             a = 30
#             print("inner2函数中a的值：", a)
#         inner2()
#         print("inner函数中a的值：", a)
#     inner()
#     print("outer函数中a的值：", a)
# outer()

# 匿名函数
# 格式：  函数名 = lambda 形参: 返回值（表达式）
# 调用函数： 结果 = 函数名(实参)
# 对比
# 普通函数
# def add(a,b):
#     return a + b
# print(add(1, 3))
# # 匿名函数
# add = lambda a,b: a + b         # a, b 就是匿名函数，a + b是返回值的表达式
# print(add(1,3))
# lambda不需要return，表达式本身就是返回值

# lambda参数形式
# 无参
# 格式：  函数名 = lambda 形参: 返回值（表达式）
# funa = lambda: "一个苹果"
# print(funa())
# 一个参数
# funb = lambda name: name
# print(funb("zouke"))
# 默认参数
# func = lambda name, age = 18: (name, age)       # 返回值是以元组的形式，必须加括号
# print(func("zouke"))
# print(func("zouke", 19))                  # 没有设置就按照默认的age = 18来，设置了就按照设置了的age = 19来
# fune = lambda a, b, c = 12: a+b+c         # 默认参数必须写在非默认参数后面
# print(fune(1,2))

# 关键字参数
# fund = lambda **kwargs: kwargs              # **最关键
# print(fund(name = "bingbing",age = 18))     # 关键字参数的传值方式，返回一个字典

#  lambda结合if判断
# a = 5
# b = 8
# # 为真结果 if 条件 else 为假结果
# # print("a比b小") if a < b else print("a大于等于b")
# comp = lambda a,b: "a比b小" if a < b else "a大于等于b"        # a, b是形参，比较大小
# print(comp(5,8))
# print(comp(8,5))
# lambda只能实现简单逻辑，如果逻辑复杂且代码量大，不建议使用，会降低代码可读性，难以维护

# 内置函数
# 查看所有内置函数
# import builtins
# print(dir(builtins))
# 大写字母开头一般为内置常量名；小写字母开头一般为内置函数名
# abs()： 返回绝对值
# print(abs(-10))
# sum(): 求和
# print(sum(123))            # 报错，sum函数内要放可迭代对象，整型不是可迭代对象
# print(sum("abcd"))         # 报错，字符串不能进行相加
# print(sum([1,2,3]))          # 列表
# print(sum({1,2,3}))          # 集合
# print(sum((1,2,3)))          # 元组
# print(sum(1.4,3,6))          # 运算时有一个为浮点数，结果也为浮点数

# min(): 求最小值
# max(): 求最大值               # 同求和，只能放列表集合元组
# print(max(-8, 5, key = abs))  # 求绝对值大小，在后面加一个key = abs， 先求绝对值再比较大小

# zip(): 将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
# li = [1,2,3]
# li2 = ['a', 'b', 'c']
# print(zip(li, li2))     # 打印出来一个zip对象
# 第一种方式 for循环
# for i in zip(li, li2):
#     print(i)            # 返回一一对应的元组
#     # 如果元素个数不一致，就按照长度最短的返回
# 第二种方式 转换成列表打印
# print(list(zip(li,li2)))        # 强行转换成列表
# zip里面必须都是可迭代对象

# map() 映射函数
# map(func,iter1)   func:自己定义的函数       iter1:要放进去的可迭代对象
# li = [1,2,3]
# 两种表达式效果相同
# ①
# def funa(x):
#     return x + 5
# ②
# funa = lambda x: x+5

# a = map(funa,li)    # 把funa函数以依次作用于每个函数
# print(a)            # 返回一个对象
# 第一种for循环取出
# for i in a:
#     print(i)
# 转换列表打印
# print(list(a)) # 以列表形式返回

# reduce():先把对象中的两个元素取出，计算出一个值然后保存着，接下来把这个计算值跟第三个元素进行计算
# from functools import reduce      # 从functools模块中导入reduce库
# # reduce(function,sequence)       # function--函数：必须是有两个参数的函数  sequence--序列：可迭代对象
# li2 = [1,2,3,4]
# def add(x,y):
#     return x + y
# a = reduce(add, li2)
# print(a)

# 拆包：对于函数中多个返回数据，去掉元组、列表或字典，直接获取里面数据的过程
# tua = (1,2,3,4)
#① 要求元组内的个数与接受的变量相同，否则会报错
# a, b, c, d = tua
# print(a,b,c,d)
#②
# a, *b = tua
# print(a,b)          # 返回列表
# 一般在函数调用时使用
# def xhc(a,b,*args):
#     print(a,b,args)
# xhc(1,2,3,4,5)
# agr = (1,2,3,4,5)
# xhc(*agr)           # *是解包功能，相当于把(1,2,3,4,5)解包成1,2,3,4,5，去掉括号。

# 抛出异常 raise
# ①创建一个Exception("XXX")对象，xxx————异常提示信息
# ②raise抛出这个异常对象
# raise Exception("我抛出了一个异常")   # 报错显示是"我抛出了一个异常"
# def funa():
#     print("嘿嘿嘿")                # 放在raise前面的代码可以被执行
#     raise Exception("我抛出了一个异常")
#     print("哈哈哈")                # 执行了raise语法，后面的代码不会再执行
# funa()

# 案例：输入密码长度不足就报异常
# 异常抛出与捕获
# def login():
#     a = str(input())
#     if len(a) >= 6:
#         return "密码可以"
#
#     raise Exception("密码位数不足")
# try:                # 捕获异常：检测到异常时，代码还能继续往下运行，程序不会终止
#     print(login())
# except Exception as e:        # 将异常保存到变量e中，即将异常"密码位数不足"这个信息保存到e中打印
#     print(e)

# 模块：本质上是一个py文件，导入一个模块就是执行一个py文件
# 分类： 内置模块， 第三方模块（第三方库）， 自定义模块
# 内置模块： random,time,os,logging，直接导入就可以使用
# 第三方模块：下载：cmd窗口输入pip install 模块名（pygame）
# 自定义模块：自己在项目上定义的模块
# 注意：命名要遵循标识符规定以及变量的命名规范，且不要与内置模块起冲突


# 导入模块:
# 方式一：
# 格式： import 模块名1， 模块名2...
# 调用功能:
# 模块名.功能名
# import pytest00
# # 调用pytest00变量
# print(pytest00.name)
# # 调用pytest00函数
# pytest00.test_funa()

# 方式二：从模块中导入指定的部分
# 语法：
# from 模块名 import 功能1, 功能2
# 直接输入功能即可，不需要添加模块名
# from pytest00 import test_funa, name
# test_funa()             # 前面不用加pytest00.
# print(name)

# 方式三：
# 语法：
# from ... import *         # 导入所有功能
# from pytest00 import *
# test_funb()
# print(name)
# 不建议过多使用这种声明方式

# as 给模块起别名
# 语法： import 模块名 as 别名
# 给模块起别名pt
# import pytest00 as pt
# # 调用funa
# pt.test_funa()
# print(pt.name)

# as给功能起别名
# 语法： from 模块名 import 功能名 as 别名
# from pytest00 import test_funa as a, name, test_funb as b     # 起别名直接在后面加 as 别名
# a()
# b()
# print(name)

# 内置全局变量__name__
# 语法： if __name__ == "__main__":
# 作用：用来控制py文件在不同的应用场景执行不同的逻辑
# __name__
# 作用：
# 1.文件在当前程序（即自己执行自己）: __name__ == "__main__"
# 2.文件被当作模块被其他文件导入: __name__ == 模块名                 # 看具体看pytest01
# import pytest01
# pytest01.test()
# # 文件被当作模块导入时不会显示if后的内容，而在pytest01自己运行时会显示

# 包： 项目结构中的文件夹/目录
# 与普通文件夹的区别：包是含有__init__.py的文件夹
# 作用：将有联系的模块放到同一个文件夹下，有效避免模块名称冲突问题，让结构更清晰

# import 导入包时，首先执行__init__.py文件的代码
# import pack_01
# 导包方式: 导入这个包内的其他模块
# from pack_01 import register
# register.reg()      # 首先执行init代码，再执行register代码

# __all__： 本质上是一个列表，列表里的元素代表要导入的模块，可以控制要引入的东西
# 看 __init__文件说明
# from pack_01 import *
# register.reg()
# login.log()

# 递归函数：如果一个函数在内部不调用其他函数，而是调用他本身的话，这个函数就是递归函数
# 条件：
# ①必须有一个明确的结束条件（递归出口）
# ②每进行一次更胜一层的递归，问题规模相比上次递归都要有减少
# ③相邻两次重复之间有紧密的联系
# 普通函数实现累加和
# def add():
#     s = 0
#     for i in range(101):
#         s += i
#     print(i)
# 递归函数
# def add(n):
#     if n == 1:                # 条件① ，n == 1时给函数一个递归出口
#         return 1
#     # 如果不是1，就持续进行累加
#     return n + add(n-1)      # 条件② 。add(100)=add(99)+100 = add(98)+99+100.....
# print(add(100))

# # 斐波那契数列： n = (n-1) + (n-2)
# 自己写的
# def funa(n):        # n代表第n项
#     if n == 1:                     # 设置出口
#         return 1
#     if n == 2:
#         return 1
#     return funa(n-1) + funa(n-2)
# print(funa(6))
# 参考
# def funa(n):        # n代表第n项
#     if n <= 1:                     # 设置出口
#         return n
#     return funa(n-1) + funa(n-2)
# print(funa(2))

# 闭包：
# ①在嵌套函数的前提下
# ②内部函数使用了外部函数的变量
# ③外部函数的返回值是内部函数的函数名
# 一个完整的闭包函数
# def outer():        # 外层函数
#     n = 10          # 外层函数的局部变量
#     def inner():    # 内层函数
#         print(n)    # 内部函数使用了外部函数的变量
#     return inner    # 外部函数的返回值是内部函数的函数名
# print(outer())      # 返回的是内部函数的内存地址
# 第一种写法
# outer()()
# 第二种写法
# ot = outer()        # 调用外函数
# ot()                # 调用内函数

# 带参闭包函数
# def outer(m):   # 外函数，m是形参、外函数的局部变量
#     n = 10
#     def inner():# 内函数
#         print("计算结果：",m + n)
#     return inner
# ot = outer(20)      # 调用外函数
# ot()                # 调用内函数

# 函数引用
# id() ：判断两个变量是否是同一个值的引用
# a = 1 # a只是一个变量名，存了1这个内存地址
# print(id(a))
# print(id(1))        # 会发现这两个内存地址是一样的

# def test1():        # test1只是一个函数名，里面存了这个函数所在位置的引用
#     print("这是一个函数")
# test1()         # 通过引用调用这个函数
# print(test1)    # 内存地址

# 每次开启内函数都在使用同一份闭包变量
# def outer(m):
#     print("这是outer函数的值：",m)
#     def inner(n):
#         print("inner函数中的值：",n)
#         return m + n        # 在inner函数中返回m+n的值
#     return inner            # 外函数中调用内函数
# ot = outer(10)              # 调用外函数，给outer()传值
# # print(outer(10)(10))
# # 第一次调用内函数
# print(ot(20))               # 调用内函数，给inner()传值
# # 第二次调用内函数
# print(ot(30))               # 10+ 30
# # 每次开启内函数都在使用同一份闭包变量

# 装饰器：不需要做任何代码变动的前提下给代码增添新的功能
# 原函数
# def test02():
#     print("发信息")
# def test(fn):         # fn是普通形参
#     print("开始注册！")
#     fn()        # 调用要传入的函数
# test(test02)

# 装饰器: 将原有的函数名定义为以函数为参数的闭包
# 标准版装饰器
# def send():             # 被装饰的函数
#     print("发消息")
# def register():
#     print("加载")
# # 闭包
# def outer(fn,fn1):        # 外函数,fn是形参,往里传的是被装饰的函数名:send
#     # 既包含原有功能，又包含新功能
#     def inner():    # 内函数
#         print("登录...")
#         # 执行被装饰的函数
#         fn()    # send()
#         fn1()
#         # 相当于一个中间变量，代替了send
#
#     return inner
# # print(outer(send))        # 打印出一个内存地址
# ot = outer(send, register)            # 调用内函数
# ot()                        # 调用外函数

# 语法糖
# 格式: @装饰器名称
# 装饰器函数
# def outer(fn):
#     def inner():
#         print("登录")
#         # 执行被装饰的函数
#         fn()
#     return inner
# # 不加()是引用函数,加()是调用函数，返回该函数要返回的值
# # @outer 相当于outer(send)
# @outer      # 在被装饰的函数上面写
# def send():
#     print("发送消息：哈哈哈")
# send()
# @outer
# def another():
#     print("另一个")
# another()

# 被装饰的函数有参数
# def outer(fn):
#     def inner(name):        # name 内函数的形参
#         print(f"{name}是inner函数中的参数")
#         fn(name)    # 这里要传参,这里就相当于func(name)
#     return inner
# # 被装饰的函数
# @outer              # 等价于 func = outer(func),写在func("zk")上一行
# def func(name):     # 在被装饰的函数里也要传参
#     print("这是被装饰的函数")
# func("zk")

# 被装饰的函数带有可变参数*args, **kwargs
# 被装饰的函数
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# # func(name = "zk")
# # 装饰器函数
# def outer(fn):
#     def inner(*args, **kwargs):
#         fn(*args, **kwargs)
#     return inner
# ot = outer(func)
# ot("siuuu", "hahaha", name = "zk")        # siuuu以元组形式返回，name以键值对形式返回
# # 同一种类型放在一起，否则报错

# 多个装饰器
# 第一个
# def decol(fn):
#     def inner():
#         return "哈哈哈" + fn() + "呵呵呵"
#     return inner
# # 第二个
# def decol2(fn):
#     def inner():
#         return "niceeeee" + fn() + "let's goooooo"
#     return inner
# def decol3(fn):
#     def inner():
#         return "你好" + fn() + "666"
#     return inner
# # 被装饰的函数1
# @decol          # 此时把niceeeee学习pythonlet's goooooo当作整体传给fn
# @decol2
# @decol3
# def test1():
#     return "学习python"
# print(test1())
# # 多个装饰器装饰时，离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰











# ***
# 正则表达式
# 元字符：具有特殊意义的字符
# 元字符对应含义
# 这些元字符用来制作模式字符串，即下面的pattern部分，·
# . 匹配任意字符（除\n）
# \w 匹配数字字母下划线
# \W 匹配非字母数字下划线
# \s 匹配任意空白字符
# \S 匹配任意非空白字符
# \d 匹配任意十进制数
# \D 匹配任意非数字，即不是数字

# 匹配即把前面一个字符怎么怎么样
# ? 匹配前面的字符0或1次
# + 匹配前面的字符1或多次
# * 匹配前面的字符0或多次
# {n} 匹配前面的字符n次
# {n,} 匹配前面的字符最少n次
# {n,m} 匹配前面的字符n到m次

# 其他字符
# 区间字符[]        匹配区间里的指定字符
# 排除字符          匹配不在[]里的字符
# 选择字符|         匹配|左右两边的任意字符
# 转义字符          同python
# [\u4e00-\u9fa5]  匹配任意一个汉字
# 分组()            改变限定符作用

# import re               # 导入正则表达式模块
# pattern = r'\d\.\d+'    # \d表示随机0~9的一个整数；\.转义字符，此时直接表现“.”出来，因为原本“.”在python中是一个元字符
#                         # 这是一个特殊字符串，为模式字符串
# s = "I study python 3.11 every day Python 2.7 I love you"       # 这个是待匹配字符串
# match
# match = re.match(pattern, s, re.I)
# # print(match)
# s2 = "3.11 I study python "
# match2 = re.match(pattern, s2)    # 从字符串开始位置进行匹配，即开始位置不是数字就会打印None
# print(s2)
# print("匹配的起始位置：",match2.start())
# print("匹配的结束位置：",match2.end())
# print("匹配区间的位置元素：",match2.span())     # 返回匹配到的第一个范围，返回的是一个左包含右不包含的区间
# print("待匹配的字符串：",match2.string)
# print("匹配的数据：",match2.group())         # 会把3.11找出来

# search   寻找第一个符合的值
# import re               # 导入正则表达式模块
# pattern = r'\d\.\d+'
# match3 = re.search(pattern, s)
# print(match3)                # 找了3.11 但没有找2.7，因为sear是搜索第一个匹配值
#                             # 没有查找到就是None

# findall  寻找所有符合的值
# import re               # 导入正则表达式模块
# pattern = r'\d\.\d+'
# match4 = re.findall(pattern, s)
# print(match4)                # 找到所有符合的匹配值，并以列表形式返回

# sub 对字符串中指定子串的替换
# import re
# pattern = "黑客|破解|反爬"
# s = "我想学习python，想破解一些vip视频，python可以实现无底线反爬吗？"
# new_s = re.sub(pattern, "XXX", s) # re.sub(模式字符串, 修改后的内容, 要匹配的字符串)
# print(new_s)

# split     分割字符串
# import re
# pattern2 = '[?|&]'      # 拆分规则
# lst = "https://www.bil1rpWjevEip/?spm_id_from=333.788.videopod.episodes&vd_sour2"
# new_lst = re.split(pattern2, lst)           # 结果是一个列表
# print(new_lst)


# sys系统模块
# import sys     # 导入系统模块
# for line in sys.stdin:              # sys.stdin: 程序接收外部输入数据。这行代码意思是持续读取所有行的数据，直到所有数据被读取完
#     a, b = map(int, line.split())       # map(函数,可迭代对象) 将可迭代对象的每个数据都进行函数操作
#                                              # line.split() 把得到的line数据根据空白划分
#     print(a+b)