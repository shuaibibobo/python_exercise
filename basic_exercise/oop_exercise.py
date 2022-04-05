
from basic_exercise import tool

# 多态 继承 封装 类 对象 实例化 标识 实例属性 实例方法 类属性 类方法
# 封装
class Foo:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def eat(self):
        print("%s,%s岁,%s,吃奶" %(self.name,self.age,self.gender))
    def drink(self):
        print("%s,%s岁,%s,喝茶" %(self.name,self.age,self.gender))
a=Foo("jack",10,"男")
a.eat()
a.drink()
b=Foo("aleen",12,"女")
# 继承
class Animal:
    def eat(self):
        print("%s 吃 " %self.name)
    def drink(self):
        print("%s 喝 " %self.name)
class Cat(Animal):
    def __init__(self,name):
        self.name=name
        self.bread="猫"
    def cry(self):
        print("喵喵叫")
class Dog(Animal):
    def __init__(self,name):
        self.name=name
        self.bread="狗"
    def cry(self):
        print("汪汪叫")
c1=Cat("猫one")
c1.eat()

# 多态
class A:
    def prt(self):
        print("A")
class B(A):
    def prt(self):
        print("B")
class C(A):
    def prt(self):
        print("C")
class D(A):
    pass
class E:
    def prt(self):
        print("E")
class F:
    pass
def test(arg):
    arg.prt()
a = A()
b = B()
c = C()
d = D()
e = E()
# f = F()
test(a)
test(b)
test(c)
test(d)
test(e)
# test(f)
# 成员修饰符
class a:  # 说明父类的私有成员无法在子类中继承
    def __init__(self):
        self.ge=123
        self.__gene=456
        

class b(a):
    def __init__(self,name):
        a.__init__(self)
        self.name=name
        self.__age=18
        # super(b,self).__init__()  # 这一行会报错
    def show(self):
        print(self.name)
        print(self.__age)
        print(self.ge)
        # print(self.__gene)  # 这一行也会报错
obj=b("xiaoming")
print(obj.name)
print(obj.ge)
# print(obj.__gene)  # 这个也会报错
obj.show()

# 反射/自省

operation=input("请输入URL:")
if operation in tool.__dict__:
    getattr(tool,operation)()
else:
    print("404")



