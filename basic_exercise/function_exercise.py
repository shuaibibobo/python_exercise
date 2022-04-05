

def hello(str):
    print(str)
str="aleen"
hello(str)

# 可变类型参数 list dict
def hello(str):
    str="asfdasf"
str="aleen"
hello(str)
print(str)

def change(list):
    list.append(["baldwin","jack","tony"])  # 改变参数

list = ["tom","jsaon"]
print(list)
change(list)
print(list)
# 关键字参数
def printBaldwin(name,age):
    print(name+"`s age is " + age)
printBaldwin(name="Baldwin",age="18")
printBaldwin(age="19",name="Baldwin")
# 不定长参数
# formal_args：普通函数形参
# *var_args_tuple：不定长形参（元组）
# **var_args_dict：不定长形参（字典）

def printBaldwin(name,age, *money):
    print("普通形参 : name=",name)
    print("普通形参 : age=",age)
    print("不定长形参 ：money=",money)
printBaldwin("Baldwin","18",1,1,1,1)

def printBaldwin(name,age, **money):
    print("普通形参 : name=",name)
    print("普通形参 : age=",age)
    print("不定长形参 ：money=",money)


printBaldwin("Baldwin","18",a=1,b=2,c=3)

def printBaldwin(name,age,*wallet, **money):
    print("name=",name)
    print("age=",age)
    print("wallet=",wallet)
    print("money=",money)


printBaldwin("Baldwin","18", 1, 1, 1, a=1, b=2, c=3)
# 匿名函数

num2 = 100
sum1 = lambda num1 : num1 + num2 ;
num2 = 10000
sum2 = lambda num1 : num1 + num2 ;
print( sum1( 1 ) )
print( sum2( 1 ) )