class abc:
    def __init__(self,age):
        self.age=age
    def __add__(self,obj):
        return self.age+obj.age
a1=abc(18)
print(abc.__dict__)
print(a1.__dict__)