#!/usr/bin/env python
# coding=utf-8
class MyList(object):            # 定义可迭代对象类

    def __init__(self, num):
        self.data = num          # 上边界


    def __iter__(self):
        return MyListIterator(self.data)  # 返回该可迭代对象的迭代器类的实例


class MyListIterator(object):    # 定义迭代器类，其是MyList可迭代对象的迭代器类

    def __init__(self, data):
        self.data = data         # 上边界
        self.now = 0             # 当前迭代值，初始为0

    def __iter__(self):
        return self              # 返回该对象的迭代器类的实例；因为自己就是迭代器，所以返回self

    def __next__(self):             # 迭代器类必须实现的方法
        while self.now < self.data:
            self.now += 1
            return self.now - 1  # 返回当前迭代值
        raise StopIteration      # 超出上边界，抛出异常


my_list = MyList(5)              # 得到一个可迭代对象
print(type(my_list))             # 返回该对象的类型

my_list_iter = iter(my_list)     # 得到该对象的迭代器实例，iter函数在下面会详细解释
print(type(my_list_iter))


for i in my_list:                # 迭代
    print(i)
# 容器是一系列元素的集合，str、list、set、dict、file、sockets对象都可以看作是容器，容器都可以被迭代（用在for，while等语句中），因此他们被称为可迭代对象。
def iter_something():
    datas=[1,2,3,4,5,6,7,1]
    for i in datas:
        yield i

itea=iter_something()
for i in itea:
    print("itea:"+str(i))

# 1、字符创创建迭代器对象
str1 = 'liangdianshui'
iter1 = iter ( str1 )

# 2、list对象创建迭代器
list1 = [1,2,3,4]
iter2 = iter ( list1 )

# 3、tuple(元祖) 对象创建迭代器
tuple1 = ( 1,2,3,4 )
iter3 = iter ( tuple1 )

# for 循环遍历迭代器对象
for x in iter1 :
    print ( x , end = ' ' )

print('\n------------------------')

# next() 函数遍历迭代器
while True :
    try :
        print ( next ( iter3 ) )
    except StopIteration :
        break
# 生成式
list1=list ( range (1,31) )
print(list1)

list1=[x * x for x in range(1, 11)]
print(list1)

list1= [x * x for x in range(1, 11) if x % 2 == 0]
print(list1)

# 生成器
def my_function():
    for i in range(10):
        yield i

print(my_function())

# 迭代多个序列
names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19, 20]
for name, age in zip(names, ages):
    print(name,age)
