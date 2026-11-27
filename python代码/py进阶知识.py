# 面向过程：需要实现一个功能的时候，着重的是过程，分析出一个个步骤，并把一个个步骤用一个个函数表示，再依次去调用一个个函数（每个步骤都需要自己手写）
# 面向对象：需要实现一个功能的时候，着重的是谁去帮我做这件事情
# 类：对一些列具有相同属性和行为的事务的统称，是一个抽象感念
# 对象：类的具体表现，面向对象思想的核心
# 在开发中，现有类再有对象

# 类的三要素：
# 类名
# 属性： 对象的特征描述
# 方法： 对象具有的功能(行为)，用来说明能做什么

# 定义类
# 基本格式
# class 类名:           # 类名必须符合标识符规定，同时遵循大驼峰命名法
     # 代码块
# class Washer:
#     height = 800        # 类属性，类所拥有的属性
# 查看类属性：类名.属性名
# print(Washer.height)
# # 新增类属性：类名.属性名 = 值
# Washer.width = 200
# print(Washer.width)
# 创建对象
# 创建对象的过程也叫实例化对象
# 实例化对象的基本格式： 对象名 = 类名()
# wa = Washer()
# print(wa)       # 默认显示对象在内存中的地址
# wa2 = Washer()
# print(wa2)      # 内存地址不同，说明是不同的对象，可以实例化多个对象

# 实例方法和实例属性
# 实例方法：由对象调用，至少有一个self参数，执行实例方法的时候，自动将调用该方法的对象赋值给self
# class Washer:
#     height = 800
#     def Wash(self):         # self参数是类中的实例方法，必须具备的
#         print("我会洗衣服")
#         print(self)         # self表示当前调用方法的对象 跟w = Washer()有关，地址改变，self跟着改变
# w = Washer()        # 实例化对象                      ←
# print(w)
# w.Wash()           # 对象调用方法
# self代表对象本身，当对象用实例方法时，python会自动将对象本身的引用作为参数，传递到实例方法的第一个参数self里面

# 实例属性
# 格式：self.属性名
# class Person:
#     name = "zk"     # 类属性
#     def introduce(self):
#         print("我是实例方法")
#         print(f"{Person.name}的年龄是{self.age}")   # self.age是实例属性
#         # 这里可以用self.name访问"zk"，因为类属性是公共的，都可以访问，而self.age是introduce下特有的实例属性.
# pe = Person()       # 实例化对象
# pe.age = 19         # 实例属性，这里pe.age = 19 等价于 self.age = 19
# pe.sex = "男"
# # print(pe.age)       # 实例属性用对象名访问可以
# # print(Person.age)   # 实例属性用类名访问不可以
# # print(pe.name)       # 类属性用对象名访问可以
# # print(Person.name)   # 类属性用类名访问可以
# pe2 = Person()
# print(pe2.sex)          # 会报错，因为pe.sex = "男"是给pe对象新增的属性，其他对象，如pe2仍是没有这个属性的
# pe.introduce()

# 类属性是属于类的，是公共的，大家都可以访问；实例属性是属于对象的，是私有的，只能由对象名访问，不能由类名访问
# 每实例化一次就需要添加一次，导致效率不高，因此有构造函数

# 构造函数__init__():
# 作用：用来做属性初始化或者赋值操作

# 在类实例化对象的时候会被自动调用
# class Test:
#     def __init__(self):     # self --- 实例方法
#         print("这是__init__()函数")
# te = Test()     # 被自动调用了， 正常还需要在后面加一个te.函数名()起调用作用

# class Person:
#     def __init__(self):
#         self.name = "zk"        # 有self.的就是实例属性
#         self.age = 18
#         self.height = 180
#     def play(self):
#         print(f"{self.name}在玩游戏")
#     def introduce(self):
#         print(f"{self.name}的年龄是{self.age}，身高是{self.height}cm")
# # 实例化对象
# pe = Person()
# pe.play()
# pe.introduce()
# # 实例化第二个对象
# pe2 = Person()
# pe2.play()
# pe2.introduce()

# 这样太麻烦了，就有了下面这个形参版本

# class Person:
#     def __init__(self,name, age, height):
#         self.name = name        # 有self.的就是实例属性
#         self.age = age
#         self.height = height
#     def play(self):
#         print(f"{self.name}在玩游戏")
#     def introduce(self):
#         print(f"{self.name}的年龄是{self.age}，身高是{self.height}cm")
# # 实例化对象
# pe = Person("zk", 19,180)
# pe.play()
# pe.introduce()
# pe = Person("xhc", 19,0)
# pe.play()
# pe.introduce()


# # 析构函数 __del__()
# # 删除对象的时候，解释器会默认调用__del__()方法
# class Person:
#     def __init__(self):
#         print("我是__init__()方法")
#     def __del__(self):
#         print("被销毁了")
#
# p = Person()        # 实例化对象
# del p   # 删除p这个实例化对象
# # del p语句执行后，内存立即被回收，系统会自动调用__del__()方法
# print("这是最后一行代码")
# # 正常运行时，不会调用__del__()，对象执行结束后，系统自动调用__del__()


# 封装
# 面向对象三大特性：封装，继承，多态
# 封装：隐藏对象中不希望被外部访问到的属性或方法
# class Person:
#     name = "zk"     # 类属性
# pe = Person()
# print(pe.name)          # 通过对象名访问
# Person.name = "kz"      # 通过类名来修改
# print(Person.name)

# 隐藏属性，只允许在类的内部使用，无法通过对象访问
# 在属性名或者方法名前面加__
# class Person:
#     name = "James"      # 类属性
#     __age = 28          # 隐藏属性
#     def funa(self):    # 实例方法
#         Person.__age = 18
#         print(f"{Person.name}的年龄是{Person.__age}")   # 在实例方法中访问类属性和隐藏属性
#
# pe = Person()
# print(pe.name)

# print(pe.age)       # 会报错，一般不可以在类的外部访问类的隐藏属性
# 两种方法访问
# 1.（了解） 不建议用，属于取巧
# 隐藏属性实际上是将名字修改为了  _类名__属性名    _Person__age
# print(pe._Person__age)
# pe._Person__age = 10
# print(pe._Person__age)  # 通过这种方式实现隐藏属性的修改

# 2. 在类中创建一个函数就可以访问到隐藏属性了（常规方法）
# pe.funa()

# 私有方法
# 1. xxx 普通属性，如果是类定义的，则类可以在任意地方使用
# 2. __xxx 隐藏属性，如果定义在类中，无法在外部直接访问，子类无法继承，要访问只能通过间接访问，
                # 另一个py文件中通过from import * 导入的时候，也无法导入
# 3. _xxx  私有属性或方法，如果定义在类中，外部可以使用，子类也可以继承
                            # 但是在另一个py文件中通过from import *导入时，无法导入
# class Person:
#     name = "sxqy"
#     __age = 54             # 隐藏属性
#     _sex = "不男不女"       # 私有属性
# pe = Person()
# # 隐藏属性要通过对象名._属性名调用
# print(pe._sex)

# 隐藏方法
# class Man:
#     def __play(self):      # 隐藏方法
#         print("玩手机")
#     def funa(self):         # 实例方法
#         print("实例方法")
#         Man.__play(self)        # 在实例方法中调用私有方法， 法二
#         self.__play()           # 效果跟上面一样，更推荐
#
# ma = Man()
# ma.funa()       # 可以访问到
# # ma.__play()     # 会报错
# ma._Man__play()     # 法一

# 私有方法
# class Girl:
#     def _buy(self):     # 私有方法
#         print("整天买买买")
# girl = Girl()     # 实例化对象
# girl._buy()       # 可以在函数外调用


# 继承：让类和类之间转变为父子关系，子类默认继承父类的所有属性和方法
# 语法：class 类名(父类名):

# # 1. 单继承
# class Person:
#     def eat(self):
#         print("吃饭")
#     def sing(self):
#         print("唱歌")
# class Girl(Person):     # Person类的子类
#     pass        # 占位符，没什么实际含义，自动跳过
# class Boy(Person):
#     pass
# girl = Girl()
# girl.eat()          # 可以调用父类的属性
# boy = Boy()


# 继承的传递（多重继承）
# class Father:
#     def eat(self):
#         print("吃饭")
#     def sleep(self):
#         print("睡觉")
# class Son(Father):
#     pass
# class Grandson(Son):
#     pass
#
# son = Son() # 实例化对象
# grandson = Grandson()
# grandson.sleep()


# 方法的重写：在子类中定义与父类相同名称的方法
# 覆盖父类方法
# class Person:
#     def money(self):
#         print("100万")
# class Man(Person):
#     def money(self):
#         print("再赚1000万")
# man = Man()
# man.money()     # 只会有子类覆盖后的内容，继承内容被覆盖

# 对父类方法的扩展，继承父类的方法，子类也可以增加自己的功能
# 三种方法
# 1.父类名.方法名(self)
# class Person:
#     def money(self):
#         print("100万")
# class Man(Person):
#     def money(self):
#         Person.money(self)
#         print("再赚1000万")
# 2. super().方法名()      推荐
# super在python里是一个特殊的类，super()是使用super创建出来的对象，可以调用父类中的方法
# class Person:
#     def money(self):
#         print("100万")
#     def sleep(self):
#         print("困安币")
#
# class Man(Person):
#     def money(self):
#         super().money()
#         super().sleep()
#         print("再赚1000万")
# 3.super(子类名,self).方法名()
# class Person:
#     def money(self):
#         print("100万")
# class Man(Person):
#     def money(self):
#         super(Man,self).money()
#         print("再赚1000万")
#
# man = Man()
# man.money()     # 只会有子类覆盖后的内容，继承内容被覆盖


# 新式类写法
# 经典类
# 1. class A:          # 不由任意内置类型派生出来的类，即不同于父类的方法
#     pass
# class Animal:
#     def walk(self):
#         print("我会走路")
# class Dog(Animal):
#     pass            # 不是派生类
# class Dog1(Animal):
#     def bite(self):
#         print("我会咬人")      # 派生类
# 2. class A():
# 新式类： 继承了object类或者该类的子类都是新式类，括号里面有东西
# class A(object)
# object -- 对象，python为所有对象提供的基类（父类），提供了一些内置的属性和方法，可以使用函数来查看，可用dir()查看
# print(dir(object))



# 多继承
# 子类可以拥有多个父类，并且具有所有父类的属性和方法
# class Father(object):   # 第一个父类
#     def money(self):
#         print("有钱")
# class Mother(object):
#     def appearance(self):
#         print("美貌")
#
# class Son(Father, Mother):      # 子类
#     pass
#
# son = Son()
# son.money()
# son.appearance()

# 不同父类存在同名的方法 : 调用就近原则，谁前调用谁
# class Father(object):   # 第一个父类
#     def money(self):
#         print("有钱")
# class Mother(object):   # 第二个父类
#     def money(self):
#         print("没钱")
#
# class Son(Father, Mother):      # 子类
#     def money(self):
#         super().money()
#         print("给了")
#
# son = Son()
# son.money()
#
# # 方法搜索顺序： __mro__
# print(Son.__mro__)


# 多态：同一种行为具有不同的表现形式
# 前提：
# 继承
# 重写
# class Animal(object):
#     """父类： 动物类"""
#     def shout(self):
#         print("动物会叫")
# class Cat(Animal):
#     """子类： 猫类"""
#         def shout(self):
#             print("小猫喵喵喵")
# class Dog(Animal):
#     """子类： 狗类"""
#     def shout(self):
#         print("狗")
# cat = Cat()
# cat.shout()
# dog = Dog()
# dog.shout()

# # 多态性：一种调用方式，不同的执行结果
# class Animal(object):
#     """父类： 动物类"""
#     def eat(self):
#         print("吃吃吃")
# class Pig(Animal):
#     """子类： 猪类"""
#     def eat(self):
#         print("吃猪饲料")
# class Dog(Animal):
#     """子类： 狗类"""
#     def eat(self):
#         print("吃狗粮")
#
# # 多态性： 定义一个统一的接口，一个接口多种实现
# def test(obj):
#     obj.eat()
# animal = Animal()
# test(animal)

# 静态方法：使用@staticmethod来进行修饰
# 静态方法与类无关，可以被转换成函数使用
# 格式： class 类名:
            # @staticmethod
            # def 方法名(形参):
                # 方法体
# 调用：
# 类名.方法名(实参)
# 对象名.方法名(实参)
# class Person(object):
#     def funa(self):         # 如果没有静态方法，后面就会默认带一个self参数
#         pass
#     @staticmethod   # 静态方法
#     def study(name):
#         print(f"{name}学习")
# # 静态方法既可以使用对象访问，又可以使用类访问
# Person.study("乐乐")      # 类名访问
# pe = Person()            # 实例化对象
# pe.study("乐乐")          # 对象访问

# 类方法：使用装饰器@classmethod来标识其为类方法
# 第一个参数必须为类对象，一般是以cls作为第一个参数
# class 类名：
#     @classmethod
#     def 方法名(cls,形参):
#         方法体

# 类方法内部可以访问类属性，或者调用其他类方法
# class Person(object):
#     name = 'zk'         # 类属性
#     @classmethod
#     def sleep(cls):     # cls表示调用哪个类，就指的是那个类本身，cls用在多态情况下可以更加灵活
#         # print(cls)      # cls代表类对象本身，类本身就是一个对象
#         print("睡觉")
#         # print(Person.name)
#         # print(cls.name)     # 代表类本身

# cls详解，例如
# class Boy(Person):
#     def play(self):
#         print("踢足球")
# class Girl(Person):
#     def see(self):
#         print("看手机")

# 以下操作只有在sleep里面有cls时才能实现，否则会报错
# a = Person()
# a.sleep()
# b = Boy()
# b.sleep()
# g = Girl()
# g.sleep()

# 总结
# class Person(object):
#     name = '小明'            # 类属性，类中定义的属性，公共的
#     def __init__(self):
#         self.age = 18       # 实例属性：类中的对象私有的
#     def play(self):         # 实例方法
#         # 在实例方法中访问类属性
#         print(f"{self.name}在玩游戏")   # 相当于Person.name
#         # 访问实例属性
#         print(self.age)     # 这个self指的就是p1,p2这些具体实例化对象
#     @staticmethod           # 定义一个静态方法，类中的函数，形参没有限制
#     def introduce():
#         print(f"我是{Person.name}")   # 静态方法可以访问到类属性，但这是没有意义的
#         # 静态方法不支持访问实例属性
#     @classmethod    # 类方法：针对类本身的方法
#     def introduction(cls):      # 代表类对象本身
#         print(f"我是{cls.name}")  # 类方法可以访问到类属性，相当于Person.name
#         # 类属性访问不支持访问实例属性
#
# p1 = Person()
# p1.play()
# p2 = Person()
# p1.age = 99
# # self实例表示p1为p1自己的,p2为p2自己的，修改p1的不会影响p2的
# print(p1.age)
# print(p2.age)
#
# p1.introduce()
# p1.introduction()


# __init__()和__new__()
# __init__()：初始化对象
# class Test(object):
#     def __init__(self):
#         print("这是__init__()方法")
# te = Test()     # 实例化对象的时候会自动调用__init__()方法，但不是最先调用

# __new__()：由object基类提供的内置的静态方法
# 作用：在内存中为对象分配空间； 返回对象的引用
# class Test(object):
#     def __init__(self):
#         print("这是__init__()方法")
#
#     def __new__(cls, *args, **kwargs):      # 代表类本身
#         print("我是__new__()")
#         # 对父类方法进行扩展 super().方法名()
#         return super().__new__(cls)         # 有了这一步才能走到__init__()那一步
#         # __new__(cls)返回对象的引用，因此要用return
#
# te = Test()     # 实例化对象的时候会自动调用__init__()方法，但不是最先调用

# class Person(object):
#     def __new__(cls, *args, **kwargs):
#         print("我是__new__()")
#         print("返回值：",super().__new__(cls))      # 返回一个引用
#         return super().__new__(cls)
#
#     def __init__(self, name):
#          self.name = name       # 实例属性
#          print("名字是",self.name)
#
# pe = Person("zk")
# print(pe)
# __new__()创建对象   返回对象引用  类级别的方法
# __init__()初始化对象 定义实例属性 实例级别的方法


# 单例模式
# 可以理解为一个特殊的类，这个类只存在一个对象
# 方式：
# 1.@classmethod
# 2.通过装饰器实现
# 3.通过重写__new__()实现
# 4.通过导入模块实现


# 实现单例模式   对象的内存地址都是一样的，只有一个对象
# 通过重写__new__()方法实现单例模式
# 设计流程
# 定义一个类属性，初始值为None，用来记录单例对象的引用
# 重写__new__()方法
# 进行判断，如果类属性是None，把__new__()返回的对象保存进去
# 返回类属性中记录的对象的引用
# 用obj创建一个空类代表一个仓库，判断是第一次创建对象表示仓库是空的，然后将生成的对象放进去填满仓库，之后每一次调用的都是在使用整个仓库，但这个仓库是唯一且固定不变的
# class Singleton(object):
#     # 记录第一个被创建的引用
#     obj = None  # 空的
#     def __new__(cls,*args,**kwargs):
#         print("这是new方法")
#         if cls.obj == None:
#             cls.obj = super().__new__(cls)
#         return cls.obj
#     def __init__(self):
#         print("我是init")
# s = Singleton()
# print("s",s)
# s2 = Singleton()
# print("s2",s)

# 单例模式，每一次实例化所创建的对象都是同一个，内存地址都一样

# 通过导入模块实现单例模式
# 最简单也是最美管的方式
# from pytest02 import te as te01
# from pytest02 import te as te02
# print(te01)
# print(te02)
# 地址是一样的，因为只是给同一个库起了别名

# 魔法方法&魔法属性
# __doc__：类/函数的描述信息
# class Person(object):
#     """人类——类的描述信息"""    # 这个内容本身也可以当作注释
#     pass
# print(Person.__doc__)   # 打印出三个引号框起来的内容

# __module__:属性  表示当前操作所在的模块
# __class__:属性   表示当前操作所在的类
# import pytest04
# b = pytest04.B()        # 实例化对象
# b.funa()
# print(b.__module__)     # 可以找到是pytest04
# print(b.__class__)      # 可以找到pytest04.B

# __str__()：方法  对象的描述信息
# 如果类中定义了此方法，那么在打印对象时，默认输出该方法的返回值，也就是打印方法中的return的数据
# 注意：__str__()必须返回一个字符串
# 用于当类被调用很多次的时候，用__str__可以快速更改所有调用情况的值，不用每次都一个个改
# class C:
#     def __str__(self):
#         return "这里是str返回值"      # 这里必须有字符串的返回值，否则会报错
# c = C()
# print(c)

# __del__()：析构函数，程序结束时调用，或者在删除某个对象时会被调用
# class P:
#     def __init(self):
#         print("这是init函数")
#     def __del__(self):
#         print("当你删除实例化对象时，他就会自动调用__del__()")
# p = P()
# del p

# __call__()：方法  使一个实例对象成为一个可调用对象，就像函数那样可以调用
# 可调用对象：函数、内置函数和类都是可调用对象，凡是可以把一对()应用到某个对象身上，都可以称之为可调用对象
# callable()： 判断一个对象是否是可调用对象
# def func():
#     print("111")
# func()
# class A:
#
#     def see(self):
#         print("这是see方法")
#
#
#     def __call__(sel, *args, **kwargs):
#         print("这是__call__")
# a = A()
# a()     # 没有call方法时，这样写是会报错的,有了__call__方法，那么这么写其实就是在调用__call__()方法
# a.see() # 写了__call__()，依旧可以用普通的调用方法

# __dict__: 属性  对于实例对象来说，__dict__ 存放的是该对象自己独有的属性（通常在 __init__ 中赋值的变量）
# class Student(object):
#     """类属性"""
#     school = "北大清华"
#     def __init__(self, name, age):
#         # 实例属性（属于具体对象自己）
#         self.name = name
#         self.age = age
#     def study(self):
#         print("学习中...")
# # 创建实例对象
# s1 = Student("张三", 18)
# # 查看实例的 __dict__
# print(s1.__dict__)
# print(Student.__dict__)


# 文件操作
# 步骤：打开文件->读写文件->关闭文件
# 文件对象的方法
# open()：创建一个file对象，默认以只读模式打开
# read(n)：n表示从文件中读取的数据的长度，没有传或者传的是复数就默认读取所有内容
# write()：将指定内容写入文件
# close()：关闭文件
# 文件名.name：返回要打开的文件的文件名，可以包含文件的具体路径
# 文件名.mode：返回文件的访问模式
# 文件名.closed:检测文件是否关闭，关闭就返回True，否则返回False

# 打开文件
# f = open('pytest01.txt')
# try:
#     print(f.name)   # 返回文件名
#     print(f.mode)   # r表示只读模式
#     print(f.closed) # 返回False，没关闭
#
# except Exception as e:
#     f.close()   # 有打开就一定要有关闭

# 读写操作
# read方法(n)
# f = open('pytest01.txt',encoding = 'UTF-8')
# q = open(r'C:\Users\14775\Desktop\text（spe）.txt',encoding = 'UTF-8')
# # 加个r可以把原本表示转义字符的\还原为地址分号
# # 右键点击文件，点击属性，找到“位置”，复制粘贴下来，并在后面加上\文件名.txt  ！！！
#
# print(f.read(5))
# print(q.read(5))
#
# f.close()
# q.close()

# readline()方法 一次只读取一行内容，方法执行完，会把文件指针移到下一行，准备再次读取
# f = open('pytest01.txt',encoding = 'UTF-8')
# # print(f.readline())     # 第一行
# # print(f.readline())     # 会读取第二行，并且自动换行
# # 读取所有行，但行数未知
# while True:
#     text = f.readline()     # 读取一行内容
#     if not text:
#         break
#     print(text)
# f.close()

# readlines():按照行的方式把文件内容一次性读取，返回的是一个列表，每一行的数据就是列表中的一个元素
# f = open('pytest01.txt',encoding = 'UTF-8')
# text = f.readlines()      # 返回列表
# # \n是换行符
# for i in text:
#     print(i)
# f.close()

# 访问模式
# 'r'：只读模式
# 'w'：只写模式，文件存在，就会先清空文件内容，再写入添加内容，不存在就创建新文件
# file = open('pytest01.txt', 'w',encoding = 'UTF-8')
# file.write('请输入文本...')
# print(file.read())
# file.close()

# + ： 既可以读又可以写
# 如果使用加号，会影响文件的读写效率
# r+：可读写文件，文件不存在就会报错
# w+：先写再读，文件存在，就会先清空文件内容，再写入添加内容，不存在就创建新文件
# f = open('pytest01.txt', 'w+',encoding = 'UTF-8')
# f.write('w+')       # 此时去pytest01文件看就会发现w+被写进去了
# f.close()

# a:追加模式，不存在就创建新文件进行写入，存在就在原有内容的基础上添加新的内容
# a+同上
# f = open('pytest01.txt', 'a+',encoding = 'UTF-8')
# f.write("\n请输入文本")  # \n换行
# f.close()

# 文件指针：标记从哪个位置开始读取数据
# f = open('pytest01.txt', 'w+',encoding = 'UTF-8')
# f.write("Hello world")
# f.close()
# # 关闭文件后，再次以只读的模式打开
# f = open('pytest01.txt', 'r',encoding = 'UTF-8')
# print(f.read())
# f.close()

# 文件定位操作
# tell()：显示文件内当前位置，即文件指针当前位置
# seek(offset, whence)：移动文件读取指针到指定位置
# offset表示偏移量：要移动的字节数;  whence表示起始位置，移动字节的参考位置，默认值是0，
# 0代表文件开头作为参考位置；1代表当前位置作为参考位置；2代表结尾位置作为参考位置
# f = open('pytest01.txt', 'w+',encoding = 'UTF-8')
# f.write("Hello world")
# print('当前文件光标的位置:',f.tell())
# f.seek(0,0)
# print(f.read())
# f.close()

# with open：代码执行完，系统会自动调用close()方法
# with open("pytest01.txt",'w+',encoding = 'UTF-8') as f:     # f是对象
#     f.write('请输入文本2')
#     f.seek(0,0)
#     print(f.read())

# 图片复制：读取二进制模式：'rb'模式
"""
读取图片
图片是一个二进制图片
写入图片
"""
# 读取图片
# with open("C:\\Users\\14775\\Desktop\\pyc\\pic\\图片.jpg",'rb') as file:
#     img = file.read()
#     print(img)
# # 读取的内容写入到当前文件
# with open("C:\\Users\\14775\\Desktop\\pyc\\图片.jpg",'wb') as f:
#     f.write(img)        # 就会在pyc文件夹中得到一个图片.jpg

# 导入模块
# import os
# """文件的重命名os.rename(旧名字,新名字)"""
# # os.rename('pytest00.txt','pytest01.txt')
# """删除文件os.remove(要删除的文件名或路径＋文件名)"""
# # os.remove('pytest01.txt')
# """创建文件夹os.mkdir()"""
# # os.mkdir("zk")
# """删除文件夹os.rmdir()"""
# # os.rmdir("zk)
# """获取当前目录os.getcwd()"""
# # print(os.getcwd())
# """获取目录列表os.listdir(路径)默认是当前路径"""
# # print(os.listdir())
# print(os.listdir('../'))    # 获取上一级目录列表


# 可迭代对象Iterable：可以被for...in...遍历的对象
# str,list,,tuple,dict,set等
# 两个条件：
# 1.对象实现了__iter_()方法
# 2.__iter()方法返回了迭代器对象
# isinstance():去判断一个对象是否是可迭代对象或者是一个已知的数据类型
# from collections.abc import Iterable,Iterator    # 导入库
# st = '123'
# # isinstance(o,t)   o：对象   t:类型（直接或者间接类名、基本类型或者元组
# print(isinstance(st,Iterable))      # 会返回布尔值
# print(isinstance(123,int))
# print(isinstance('123',(int,str)))  # 判断是不是int或str两个数据类型的一种

# 迭代器Iterator
# 可以记住遍历位置的对象
# iter():获取可迭代对象的迭代器
# next():一个个去取元素，去完元素后会引发一个异常
# li = [1,2,3,4]
# # 创建迭代器对象
# li2 = li.__iter__()
# 等效于li2 = iter(li)
# # print(li2)
# # 获取下一条数据
# print(next(li2))    # 取到1
# print(next(li2))    # 取到2
# print(next(li2))    # 取到3
# print(li2.__next__()) # 取到4 与print(next(li2))作用是一样的
# 如果打印了五次，超过了列表的范围就会报错，引发StopIteration异常


# 迭代器协议
# 对象必须提供一个next方法，执行该方法要么就返回迭代中的下一项，要不就引发StopIteration异常

# 自定义迭代器类
# 1.__iter__()    2.__next__()

# 普通的类：↓
# class Test(object):
#     """初始值为1，逐步递增"""
#     def __init__(self):
#         self.num = 1
#     def funa(self):
#         print(self.num)
#         self.num += 1
# t = Test()
# t.funa()        # 取出1
# t.funa()        # 取出2
# t.funa()        # 取出3
# for i in range(5):
#     t.funa()    # 取4-8

# 迭代器类
# import time     # time.sleep()
# class MyIterator(object):
#     def __init__(self):
#         self.num = 1
#     def __iter__(self):
#         return self     # 返回的是当前迭代器的实例对象
#     def __next__(self):
#         """结束条件"""
#         if self.num == 10:
#             raise StopIteration("终止迭代")     # raise + 异常名,表示抛出异常
#         self.num += 1
#         return self.num
# mi = MyIterator()
# print(mi)
# print(next(mi))     # 取到2
# for i in mi:
#     print(i)
#     time.sleep(0.5) # 间隔0.5秒


# 生成器generator：python中一边循环一边计算的机制
# 列表推导式：
# li = [i*5 for i in range(5)]
# print(li)
# # 生成器表达式:
# gene = (i*5 for i in range(5))
# print(gene)

# 生成器函数：使用了yield关键字的函数
#yield:
# 1.类似于return，将指定值或者多个值返回给调用者
# 2.yield语句一次返回一个结果，在每个结果中间，挂起函数，执行next()函数。再重新从挂起点往下执行
# 使函数中断，并保存中断状态
# def gen():
#     print("开始了")
#     yield 'a'   # 返回一个a并暂停了函数，在此挂起，下次再从此处恢复运行
#     yield 'b'
#     yield 'c'
# g = gen()
# print(g)
# print(next(g))
# print(next(g))

# def func(path):
#     with open(path) as f:
#         for line in f:
#             yield line.strip()      # 读取到一行然后停下，等到下面那个for循环第二次读取时再读取第二行，以此类推
#             """如果使用return，函数读取完第一行之后直接结束，那么for循环始终都在读取第一行"""
# for line in func("pytest01"):
#     print(line)

# 线程
# from threading import Thread    # 导入线程模块
# import time
# # 线程之间共享资源（全局变量）
# li = []
# # 写入数据
# def wdata():
#     for i in range(5):
#         li.append(i)
#         time.sleep(1)   # 休眠1秒
# # 读取数据
# def rdata():
#     print(li)
#
# if __name__ == "__main__":  # 只有在当前模块才会执行，如果此时文件是被其他文件导入的，下面的代码就不会被执行
#     # 创建子线程
#     t1 = Thread(target=wdata)
#     t2 = Thread(target=rdata)
#     # 开启子线程
#     t1.start()
#     # 阻塞线程
#     t1.join()   # join()方法：等待t1任务执行再往下执行
#     t2.start()
#     t2.join()

# 资源竞争问题
# from threading import Thread
#
# a = 0
# b = 1000000
# def add():
#     for i in range(b):
#         global a        # a如果要进行赋值操作，系统会自动认为他是局部变量，因此要全局声明
#         a += 1
#         # num = 0       # 如果a只是读取作用，会遵循LEGB顺去依次去找，即使是全局变量也可以进行读取操作
#         # num += a
#     print("第一次：",a)
#
# def add2():
#     for i in range(b):
#         global a
#         a += 1
#     print("第二次：",a)
# # add()
# # add2()
# if __name__ == "__main__":
#     first = Thread(target=add)
#     second = Thread(target=add2)
#     first.start()
#     second.start()

# 线程同步
# join()
# 互斥锁 acquire() 加锁
      # release() 解锁
# 这两个方法必须成对出现
# from threading import Thread,Lock
# a = 0
# b = 1000000
# # 创建互斥锁
# lock = Lock()   # 全局变量
# def add():
#     lock.acquire()  # 上锁
#     for i in range(b):
#         global a
#         a += 1
#     print("第一次：",a)
#     lock.release()  # 解锁
# def add2():
#     lock.acquire()
#     for i in range(b):
#         global a
#         a += 1
#     print("第二次：",a)
#     lock.release()
#
# # 互斥锁是多个线程一起去抢，抢到锁的线程先执行
# if __name__ == "__main__":
#     first = Thread(target=add)
#     second = Thread(target=add2)
#     first.start()
#     second.start()



# 进程：一个运行的程序或者软件就是一个进程
# 进程的状态
# 1.就绪状态：运行条件已经满足，正在等待cpu执行
# 2.执行状态：cpu正在执行功能
# 3.等待状态：等待某些条件满足，如sleep休眠状态
# print("1") # 执行状态
# a = input()# 等待状态

# 进程语法结构
# multiprocessing模块提供了一个Process类代表进程对象
# Process 类参数
# 1.target：执行的目标任务名，即子进程要执行的任务
# 2.args: 以元组的形式传参
# 3.kwargs：以字典的形式传参
# 方法：
# start()：开启子进程
# is alive()：判断子进程是否还活着，存活就返回True，死亡就返回False
# join():主进程等待子进程执行结束
# 常用属性
# name：当前进程的别名，默认为process_N
# pid：当前进程的进程编号

# """导入模块"""
# from multiprocessing import Process
# import os
#
# def sing():
#     """os.getpid()获取当前进程的编号"""
#     """os.getppid()获取当前父进程的编号"""
#     print(f"sing子进程的进程编号：{os.getpid()},当前父进程编号：{os.getppid()}")
#     print("唱歌")
# """ 处于同一个py文件下面，父进程编号就是py文件主进程的编号，是一样的"""
# def dance():
#     print("跳舞")
#     print(f"dance子进程的进程编号：{os.getpid()},当前父进程编号：{os.getppid()}")
# if __name__ == "__main__":
#     # 创建子进程
#     p1 = Process(target=sing,name="第一子进程")      # 修改子进程名称的第一种方法
#     p2 = Process(target=dance,name="第二子进程")
#     # 开启
#     p1.start()
#     p2.start()
#     # 第二种修改子进程名称方式
#     p1.name = "第二种修改方式"
#     # 访问name属性  子进程名.name
#     print("p1:",p1.name)
#     print("p2:", p2.name)
#     # 查看子进程的进程编号
#     print("p1:",p1.pid)
#     print("p2:", p2.pid)
#     print(f"主进程编号：{os.getpid()},主进程的父进程编号：{os.getppid()}")

# import time
# from multiprocessing import Process
# import os

# def sing(name):
#     print(f"{name}唱歌")
# def dance(name):
#     print(f"{name}跳舞")
#
# if __name__=="__main__":
#     p1 = Process(target=sing, args=("人",))
#     p2 = Process(target=sing, args=("动物",))
#     p1.start()
#     p1.join()       # 主程序处于等待状态，p1是运行状态
#     p2.start()
#     p2.join()
#     print("p1存活状态:",p1.is_alive())
#     print("p2存活状态:", p2.is_alive())


# 进程中的通信
"""要导入模块"""
# from queue import Queue
# Queue(队列)
# q.put():      放入数据
# q.get():      取出数据
# q.empty():    盘对队列是否为空
# q.qsize():    返回当前队列包含的消息数量
# q.full():     判断队列是否满了

# 初始化一个队列对象
# q = Queue(3)    # 最多可以接受3条消息,没写或负值认为没有上线
# q.put("1")
# q.put("2")
# print("是否满了:",q.full())
# q.put("3")
# print("size:",q.qsize())
# print(q.get())      # 获取队列中的一条消息,然后将其从队列中移除
# print(q.get())
# print(q.get())
# print(q.empty())    # 判断是否为空,返回True

# # 进程间不共享全局变量
# import time
# from multiprocessing import Process,Queue
# li = ["128","7272","31763","4752"]
# # 写入数据
# def wdata(q1):
#     for i in range(5):
#         print(f"{i}已被放入")
#         q1.put(i)
#         time.sleep(0.2)
#     print("写入的数据是:",li)
# # 读取数据
# def rdata(q2):
#     while not q2.empty():
#         print("取出的数据:",q2.get())
#
# """通过Queue（队列）来实现进程间的通信"""
# """进程间的全局变量不共享，没法用li作为进程间通讯的桥梁"""
#
# if __name__ == "__main__":
#     # 创建队列对象
#     q = Queue()
#     p1 = Process(target=wdata,args = (q,))
#     p2 = Process(target=rdata,args = (q,))
#     p1.start()
#     p1.join()       # 依旧是空的，因为进程不共享全局变量，写入的和读取的不是同一个变量
#     p2.start()

# 多线程：同时运行多个线程
# 线程与进程
# 线程：是cpu调度的基本单位，每一个进程至少有一个线程，这个线程通常就是我们的主线程
# 进程：是操作系统进行资源分配的基本单位，每打开一个程序至少都有一个进程
# 一个进程默认有一个线程，进程里面可以创建多个线程，线程是依附在进程里面的
# 导入线程模块
# import threading,time
# # Thread线程类参数
# # target:执行的任务名
# # args：函数里面有参数时，以元组的形式给任务传参
# # kwargs：以字典的形式给任务传参
# # args传参时要一一对应，kwargs传参数只需要在字典里将键值对对应就可以
# def sing(name):
#     print(f"{name}在唱歌")
#     time.sleep(0.2)
#     print("唱完了")
# def dance(name):
#     print(f"{name}在跳舞")
#     time.sleep(0.2)
#     print("跳完了")
#
# if __name__ == "__main__":
#     # 创建子线程
#     t1 = threading.Thread(target=sing,kwargs={"name":'张三'},daemon=True)
#     t2 = threading.Thread(target=dance, kwargs={"name": '李四'},daemon=True)
#     # 守护线程：主线程执行结束，子线程也会跟着结束。 *** 要写在创建子线程的后面，daemon = True
#     # 开启子线程
#     t1.start()
#     t2.start()
#
#     # 阻塞主线程join():暂停的作用，等子线程执行结束后，主线程才会继续执行
#     t1.join()
#     t2.join()
#
#     # 获取线程名字
#     print(t1.name)
#     print(t2.name)
#
#     # 更改线程名字
#     t1.name = "新的sing名字"
#     t2.name = "新的dance名字"
#     print("结束")

# import threading,time

# 线程之间执行是无序的
# def task():
#     time.sleep(1)
#     print("当前线程是：",threading.current_thread().name)
#
# if __name__=="__main__":
#     for i in range(5):
#         t = threading.Thread(target=task)
#         t.start()

# 线程之间共享资源
# li = []
# # 写入数据
# def wdata():
#     for i in range(5):
#         li.append(i)
#         time.sleep(0.2)
#     print("此时li列表为：",li)
# # 读取数据
# def rdata():
#     for i in li:
#         print("li中的数据有",i)
#
# if __name__=="__main__":
#     # 先读取到li有0，然后打印，再读取到li有五个数据
#     t1 = threading.Thread(target=wdata)
#     t2 = threading.Thread(target=rdata)
#     t1.start()
#     t2.start()
#     # 加个join就可以避免

# 进程池：事先准备好一批进程，放在池子里备用，需要的时候直接拿出来，不需要的时候放回去待命
# 导入pool模块
# from multiprocessing import Pool
# import time
#
# # 这是一个需要执行的任务
# def task(x):
#     time.sleep(1)  # 模拟耗时操作
#     return x * x
#
# if __name__ == '__main__':
#     # 创建一个包含 4 个工作进程的进程池
#     # 注意：Windows 系统下这行必须放在 if __name__ == '__main__': 下面
#     with Pool(processes=4) as pool:     # 理解为提前准备了4个进程，那么在下面运行是就是四个四个进行，会比一个个进行快
#         # 准备 10 个任务（比如计算 1 到 10 的平方）
#         tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#         # map 方法会将 tasks 分发给池子里的进程去并发执行
#         # 最终返回结果列表
#         # 语法：pool.map(执行的函数名,执行的任务名--可迭代对象)
#         results = pool.map(task, tasks)
#
#         print(results)

# 协程：单线程下的开发，又称微线程
# 线程和进程的操作是由程序触发系统接口，最后的执行者是系统，协程的操作则是程序员
# 简单实现协程
# def task1():
#     yield 'a'
# def task2():
#     yield 'b'
#
# if __name__ == '__main__':
#     t1 = task1()
#     t2 = task2()
#     print(next(t1))
#     print(next(t2))


# greenlet：由c语言实现的协程模块，通过设置switch()来实现任意函数之间的切换
# 安装    windows+R 输入cmd 然后输入pip install 模块名
# 卸载    windows+R 输入cmd 然后输入pip uninstall 模块名
# 查看    windows+R 输入cmd 然后输入pip list
# greenlet属于手动切换，当遇到IO操作，程序会阻塞，而不能自动切换
# 通过greenlet实现任务切换
# 导入greenlet模块
# from greenlet import greenlet
# def sing():
#     print("在唱歌")
#     g2.switch()     # 此时会跳到dance函数那里
#     print("唱完了")
# def dance():
#     print("在跳舞")
#     print("跳完了")
#     g1.switch()     # 此时会跳回去运行g1剩下的部分，不会从头再来
#
# if __name__ == "__main__":
#     # 创建协程对象  greenlet(任务名)
#     g1 = greenlet(sing)
#     g2 = greenlet(dance)
#     # 切换到g1中去运行
#     g1.switch()
#     # 切换到g2中去运行
#     g2.switch()
#     # switch()本质是可以实现在不同程序跳来跳去
#     # switch会保留函数的执行现场，即switch只是把这个函数挂起了，等到再次运行他时会从switch处开始


# gevent：遇到io操作时，会进行自动切换，属于主动式切换
# 使用
# import gevent       # 导入模块
# import time
# gevent.spawn(函数名,返回值) # 创建协程对象
# gevent。sleep()     # 睡眠操作
# 协程对象.join()       # 阻塞，等待某个协程执行完毕
# gevent.joinall(协程对象列表)    # 等待所有的协程对象都执行结束再退出
# def sing():
#     print("在唱歌")
#     gevent.sleep(0.2)
#     print("唱完了")
# def dance():
#     print("在跳舞")
#     gevent.sleep(0.4)   # 休眠
#     print("跳完了")
# def run(name):
#     for i in range(5):
#         gevent.sleep(0.2)   # 这里用time就是张三先跑五次，李四再跑五次，用gevent就是一人一次来
#         print(f"{name}第{i}次在跑步")
#
# if __name__ == '__main__':
#     # 创建协程对象
#     # g1 = gevent.spawn(sing)
#     # g2 = gevent.spawn(dance)
#     gevent.joinall([
#         gevent.spawn(run,"张三"),
#         gevent.spawn(run, "李四")
#     ])
    # 阻塞
    # g1.join()   # 等待g1执行结束
    # g2.join()
# joinall([协程1，协程2...]) 等待所有协程都执行结束再退出

# monkey补丁，拥有在模块运行时替换的功能

# from gevent import monkey   # 猴子补丁
# monkey.patch_all()    # 作用是把卡住整个程序的函数（如 time.sleep、socket ）替换成 gevent 自己的协作式版本。
# # 这句话必须放在被打补丁的前面
# def run(name):
#     for i in range(5):
#         time.sleep(0.2)   # 这里用time就是张三先跑五次，李四再跑五次，用gevent就是一人一次来
#         print(f"{name}第{i}次在跑步")
#
# if __name__ == '__main__':
#     # 创建协程对象
#     # g1 = gevent.spawn(sing)
#     # g2 = gevent.spawn(dance)
#     gevent.joinall([
#         gevent.spawn(run,"张三"),
#         gevent.spawn(run, "李四")
#     ])

# gevent协程，如果协程g1遇到gevent.sleep()休眠就会立刻跳到其他协程g2上去运行，如果在其他协程g2还在运行且没有另一个gevent.sleep()同样跳回来时，
# 系统会直接切断g2的运行，继续将g1运行完


# 正则表达式
# 字符串处理工具
# import re   # 导入re模块
# 步骤：
# 使用match方法进行匹配操作：
#    re.match()能匹配出以xxx开头的字符串
# re.match(pattern,string)
# pattern：要匹配的正则表达式；string：要匹配的字符串
# res = re.match("kd","kdweqxfjorngknvkerjnk")
# print(res)
#    如果起始位置没有匹配成功，返回None
# 如果上一步数据匹配成功，使用group()提取数据
# print(res.group())
# 注意：match是从开始位置进行匹配，匹配不到就没有，匹配的是表达式整体

# 正则表达式
# 元字符：具有特殊意义的字符
# 元字符对应含义
# 这些元字符用来制作模式字符串，即下面的pattern部分，·
# . 匹配任意字符（除\n）
# \w 匹配数字字母下划线
# \W 匹配非字母数字下划线
# \s 匹配任意空白字符
# \S 匹配任意非空白字符
# \d 匹配0-9
# \D 匹配任意非数字，即不是数字
# []匹配[]中列举的字符
# res1 = re.match('.','hello')
# print(res1.group())
# res2 = re.match('[he]','hello')      # 只要首字符是中括号里的任意一个就可以匹配到
# print(res2.group())                                # [a-zA-Z]可以匹配到任意大小写
# res3 = re.match('[0-9]','819874')   # 想要跳过某个数[0-46-9] 跳过5
# print(res3.group())
# res4 = re.match(r'\d\d','19874')    # 匹配两个字符
# print(res4.group())
# res5 = re.match(r'\D','、he5lo')
# print(res5.group())
# res6 = re.match(r'\s..','  hello')
# print(res6.group())

# 匹配多个字符
# ? 匹配前面的字符0或1次
# + 匹配前面的字符1或多次
# * 匹配前面的字符0或多次
# {n} 匹配前面的字符n次     超出位数无法匹配
# {n,} 匹配前面的字符最少n次
# {n,m} 匹配前面的字符n到m次     会尽可能打印出全部

# ^ 匹配字符串开头和结尾；表示对......取反
# res = re.match('^py',"python pycharm")
# print(res.group())
# 取反
# ^在[]中表示不匹配
# res = re.match('[^py]','thon')  # 表示除了py之外的字符
# print(res.group())
# $ 匹配字符串结尾
# res = re.search(r's$','mdkosgns')   # search+s$在字符串里找最后一个s
# print(res.group())

# 导入re模块
import re
# 一、匹配分组
# 1. |  匹配左右任意一个表达式
# res = re.match('abc|def','abcd')    # 先匹配左边的，再匹配右边的
# print(res.group())
#
# # 2.(ab) 将括号中的字符作为一个分组      将ab作为一个整体，突出用在重复匹配时，(ab)+表示重复匹配ab，而ab+只表示重复匹配b
# res1 = re.match('\\w*@(163|qq).com','123@163.com')
# print(res1.group())
# res2 = re.match('(ab)+','ababababab')
# print(res2.group())         # 括号里不填或者填0表示获取所有分组
# print(res2.group(0))        # 会获取所有分组
# print(res2.group(1))        # 只会获取第一个分组

# 3. \num 匹配分组num匹配到的字符串
# res = re.match(r'<(\w*)>\w*</\1>','<html>login</html>')
# print(res.group())
# res1 = re.match(r'<(\w*)><(\w*)>.*</\2></\1>','<html><body>login</body></html>')   # \2表示第二个括号里的内容
# print(res1.group())      # (要复制的内容)    \1 --- 表示第几个组

# 4.(?P<name>)    分组起别名
# res1 = re.match(r'<(?P<l1>\w*)><(?P<l2>\w*)>.*</(?P=l2)></(?P=l1)>','<html><body>login</body></html>')
# print(res1.group())
# 5.(?P=name)     引用别名为name分组匹配到的字符串
# 如果要分组匹配的内容过多时，可以让他有一个名字的方式便于后面重复匹配，不需要\1,\2...\100这样一个个自己去数谁对应谁了

# 匹配网址
# li = ["www.baidu.com", "www.python.org","http.jd.cn","www.py.en","www.abc.cn"]
# for i in li:
#     res = re.match(r'www(\.)\w*(\1)(com|cn|org)',i)
#     if res:
#         print(res.group())

# 高级用法
# match 匹配成功会返回一个match对象，search也会返回match对象，findall返回一个列表对象
# 1.search():扫描整个字符串，并返回第一个成功匹配的对象，如果匹配失败就会返回None
# res = re.search('th','python')
# print(res.group())

# 2.findall():从头到尾匹配，找到所有匹配成功的数据，并返回一个列表
# res = re.findall('th','pythonthononthsdcth')
# print(res)

# 3.sub(pattern,repl,string,count)
# pattern:正则表达式  代表需要被替换的，也就是字符串里面的旧内容
# repl： 新内容
# string： 原字符串
# count: 指定替换的次数
# res = re.sub(r"\d+",'q','zk112507')
# print(res)

# 4.split(pattern,string,maxsplit)
# pattern:正则表达式
# string： 原字符串
# maxsplit: 指定最大分割次数，未指定就是全部分割
# res = re.split("p","didcsygpxnshufpajenrqp",1)
# print(res)

# 贪婪与非贪婪（匹配）
# 贪婪匹配：满足匹配时，匹配尽可能长的字符串
# res = re.match('em*','emmmm')
# print(res.group())      # *表示0或无数，那么根据贪婪匹配原则，它会匹配所有m
#
# # 非贪婪匹配：满足匹配时，匹配尽可能短的字符串，使用？来表示非贪婪匹配
# res = re.match('em*?','emmmm')
# print(res.group())      # *表示0或无数，那么根据非贪婪匹配原则，它会匹配0个m

# 原生字符串
# print(r"zzz\tttkkk")
# res = re.match(r"\\\\\\",r"\\\game")
"""
这里用r是为了防止python自带的转义符和正则表达式的转义符”打架“报错
python拿到6个\后会先将他转换成3个\再拿给正则表达式，结果正则表达式那里就只有3个\导致无法继续转换了，这是需要转换两步的
如果想不用r，那就需要写12个r，让他两次转换后才为3个\。
"""
# print(res.group())

# os模块：用于用户和操作系统进行交互
import os
"""
通用操作
获取平台信息
对目录的操作
判断操作
"""
# 1.os.name  # 返回操作系统类型
# print(os.name)
# 对于Windows返回nt，对于Linux，返回posix
# 2.os.getenv(环境变量名称)   # 读取环境变量
# print(os.getenv("path"))    # 在 Linux/macOS 中是 PATH
# 3.os.split()  # 把目录名和文件名分离，以元组的形式接受，第一个元素是目录路径，第二个元素是文件名
# print(os.path.split(r"C:\Users\14775\Desktop\pyc\py进阶知识.py"))
"""可以用于获取文件的后缀名并修改，且不变文件的位置"""

# 4.os.path.dirname   # 显示split分割的第一个元素，即目录
# 5.os.path.basename  # 显示split分割的第二个元素，即文件名
# print(os.path.dirname(r"C:\Users\14775\Desktop\pyc\py进阶知识.py"))
# print(os.path.basename(r"C:\Users\14775\Desktop\pyc\py进阶知识.py"))
# print(os.path.dirname(r"C:\Users\14775\Desktop\pyc/"))   # 如果路径以/结尾，那么就会正常根据路径的目录和文件名返回，如果是\会报错

# 6.os.path.exists()    # 判断路径是否存在，存在就返回True，不存在就返回False
# print(os.path.exists(r"C:\Users\14775\Desktop\pyc\py进阶知识.py"))

# 7.os.path.isfile()    # 判断是否存在文件（存在，且要是个文件）
# print(os.path.isfile(r"C:\Users\14775\Desktop\pyc\py进阶知识.py"))      # 是文件  True
# print(os.path.isfile(r"C:\Users\14775\Desktop\pyc/"))      # 不是文件，是一个目录   False

# 8.os.path.isdir()     # 判断是否存在目录（存在，且要是目录）
# print(os.path.isdir(r"C:\Users\14775\Desktop\pyc\py进阶知识.py"))       # 是文件  False
# print(os.path.isdir(r"C:\Users\14775\Desktop\pyc/"))                   # 是目录  True

# 9.os.path.abspath()   # 获取当前路径下的绝对路径
# print(os.path.abspath("py进阶知识.py"))
# os.path.isabs() 判断是否为绝对路径   返回布尔值
# print(os.path.isabs(r"C:\Users\14775\Desktop\pyc\py进阶知识.py"))
