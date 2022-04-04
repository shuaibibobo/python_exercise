# Python字典是另一种可变容器模型,可存储任意类型对象。如字符串、数字、元组等其他容器模型
# 因为字典是无序的所以不支持索引和切片。
dict={"name":"aleen","age":12,"sex":"男"}
dict1={}
print(dict)
print(dict1)
# 增加元素
dict["score"]=100
print(dict)
# 删除元素
del dict["name"]
print(dict)
# 查找元素
value=dict["sex"]
print(value)
# 更改元素
dict["name"]="张大大"
print(dict)
# 清空字典
dict.clear()
print(dict)
dict={"name":"aleen","age":12,"sex":"男"}
print("键值对个数为:"+str(len(dict)))
print("所有key:"+str(dict.keys()))
print("所有值:"+str(dict.values()))
print("所有键值对:"+str(dict.items()))
if 20 in dict.values():
    print("我是20")
if "张大大" not in dict.values():
    print("张大大不在")
#     取值
print(dict["name"])
# setdefault key存在返回value
# key不存在 返回none 将新值保持字典中
# key不存在但是设置了value 返回设置的value
print(dict.setdefault("name"))
print(dict.setdefault("name","ada"))
print(dict)

# print(dict.setdefault("name2"))
# print(dict)
print(dict.setdefault("name2","af"))
print(dict)
my_dict={"name":"小红","age":20,"sex":"女"}
#如果key存在返回对应的value
print(my_dict.get("name"))
print(my_dict.get("name","李四"))
#如果key不存在,返回None,设置的不加入字典中
print(my_dict.get("name2"))
print(my_dict.get("name2","王五"))
print(my_dict)
for i in my_dict.keys():
    print(i)

for i in my_dict.values():
    print(i)

for i in my_dict.items():
    print(i)
#4.依次打印key和value,通过索引
for key,value in my_dict.items():
    print(key,value)
#5.元素值和对应的下标索引  enumerate(列表名)
for i in enumerate(my_dict):
    print(i)