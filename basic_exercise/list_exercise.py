
import numpy as np

list1=[1,2,3,4,5,1,2,3,4]
print(list1)
print(list1.count(1))
# 第一个出现的索引下标
print(list1.index(2))
# 从末尾增加元素
list1.append(12)
print("append后:"+str(list1))
list1.insert(1,16)
print("insert后："+str(list1))
# 更改索引为0的值
list1[0]=18
print("更改索引为0后的list1:"+str(list1))
del list1[0]
print("删除索引为0后的list1:"+str(list1))
# num.pop 默认删除最后一个元素
# num.pop(0)写入索引，删除指定元素
list1.pop(0)
print("pop删除指定索引为0后的list1"+str(list1))
list1.remove(2)
# 默认删除首次出现值
print("remove值为2后的list1:"+str(list1))
while list1.count(3)>0:
    for i in list1:
        if i==3:
            list1.remove(3)
list1.reverse()
print("reverse后的list1:"+str(list1))
# list1.sort（）升序
# list1.sort(reverse=true) 降序
# list1[-1] 最后一个元素
list2 = ['a', 'b', 'c']
list1.extend(list2)
print("list1通过extend后list2的list:"+str(list1))
print("clear后的list:"+str(list1.clear()))

# 二维数组
list4=[1,2,3,4,[5,6,7,8,9]]

list1=[[1.73,1.68,1.71,1.89,1.78],
       [54.4,59.2,63.6,88.4,68.7]]
list3=[1.73,1.68,1.71,1.89,1.78]
list4=[54.4,59.2,63.6,88.4,68.7]
list5=np.array([1.73,1.68,1.71,1.89,1.78])
list6=np.array([54.4,59.2,63.6,88.4,68.7])
#构造二维数组
list=np.array([[1.73,1.68,1.71,1.89,1.78],
               [54.4,59.2,63.6,88.4,68.7]])
print(type(list1))
print(list1[0][1])
print(list5/list6)
print(type(list)) #结果：<type 'numpy.ndarray'>
print(list.shape)  #结果：(2, 5) 二行5列二维数组
print(list[0][2]) #结果：1.71 ,取第0行第二列数值，即第三列1.71
print(list[0,2] )  #结果：1.71 ,取第0行第二列数值，即第三列1.71
print(list[:,1:3] )#结果：[[  1.68   1.71] [ 59.2   63.6 ]]，取所有行的，第一列和第三列数据
print(list[1,:]) #结果：[ 54.4  59.2  63.6  88.4  68.7]，取第一行的所有数值
# 切片
List4 = [1, 2, 3, 4, 5, ["a", "b", "c", ["d", "e"]]]
cut1=list4[3:6]
print("3到6的元素:"+str(cut1))
print("从头到2元素:"+str(list4[:3]))
print("取索引为1到4的值步长为2:"+str(list4[1:5:2]))
print("去所有值步长为2:"+str(list4[::2]))
print("步长为负数从后往前取值:"+str(list4[::-1]))

