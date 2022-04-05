# class A():
#     def __init__(self):
#         self.num1 = 100
#         self.__num2 = 200
#     def __test(self):
#         print("私有方法 "+str(self.num1)+str(self.__num2))
#     def test(self):
#         print("父类的公有方法中访问父类的私有属性"+str(self.__num2))
#         self.__test()  #父类的共有方法中访问父类的私有方法
# class B(A):
#     def demo(self):
#         print("访问父类的公有属性"+str(self.num1))
#         self.test()
# b = B()
# b.demo()

# class a:  # 说明父类的私有成员无法在子类中继承
#     def __init__(self):
#         self.ge=123
#         self.__gene=456
#
# class b(a):
#     def __init__(self,name):
#         self.name=name
#         self.__age=18
#         # super(b,self).__init__()  # 这一行会报错
#     def show(self):
#         print(self.name)
#         print(self.__age)
#         print(a.ge)
#         # print(self.__gene)  # 这一行也会报错
# obj=b("xiaoming")
# print(obj.name)
#
# # print(obj.__gene)  # 这个也会报错
# obj.show()
