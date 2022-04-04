

temp=()
print(type(temp))
temp=(1,)
print(type(temp))
temp=(1)
print(type(temp))
print(8*(8))
print(8*(8,))
temp=("阿竹","小黑","波波")
temp=temp[:2]+("花花",)+temp[2:]
print(temp)
temp=temp[:2]+temp[3:]
del temp
list1=[1,2,3]
temp=(1,2,list1)
list1[0]=1
