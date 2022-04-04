

# 无序性 确定性 不重复性
s={1,12,"张大大","阿竹"}
# 增加元素
s.add("good")
s.add(32)
print(s)
c=s.copy()
print(c)
# 删除元素
s.clear()
print(s)
s={1,12,13,"张大大","阿竹"}
# 随机删除
s.pop()
print(s)
s={1,12,13,"张大大","阿竹"}
s.remove(1)
print(s)
s={1,12,13,"张大大","阿竹"}
s.discard(1)
s.discard("good")
print(s)
# 交集运算
x1 = ["a", "b", "c", "d", "e"]
x2 = ["c", "d", "e", "f", "g"]
x3 = []
for x in x1:
    if x in x2:
        x3.append(x)
print("在x1和x2相同元素:"+str(x3))

s_x1 = set(x1)
s_x2 = set(x2)
# 取交集
inter = s_x1.intersection(s_x2)
print("x1和x2交集:"+str(inter))
# 交集符号运算
print(s_x1 & s_x2)
# update 交集覆盖
s_x1.intersection_update(s_x2)
print(s_x1)
# set 并集运算
x1 = ["a", "b", "c", "d", "e"]
x2 = ["c", "d", "e", "f", "g"]
s_x1 = set(x1)
s_x2 = set(x2)
uni = s_x1.union(s_x2)
print(uni)
# 并集符号运算
print(s_x1 | s_x2)
# update
s_x1.update(s_x2)
print(s_x1)
# set 差集运算
x1 = ["a", "b", "c", "d", "e"]
x2 = ["c", "d", "e", "f", "g"]
s_x1 = set(x1)
s_x2 = set(x2)
dif_x1 = s_x1.difference(s_x2)
print(dif_x1)
dif_x2 = s_x2.difference(s_x1)
print(dif_x2)
# 差集符号运算
print("差集:"+str(s_x1 - s_x2))
print(s_x2 - s_x1)
# update
s_x1.difference_update(s_x2)
print("difference_update:"+str(s_x1))
s_x2.difference_update(s_x1)
print(s_x2)
# set 对称差集运算满足交换律：A△B = B△A
s_x1 = set(x1)
s_x2 = set(x2)
sym = s_x1.symmetric_difference(s_x2)
print("对称集:"+str(sym))
# 对称差集符号运算
print(s_x1 ^ s_x2)
print(s_x1 - s_x2 | s_x2 - s_x1)
print((s_x1 | s_x2) - (s_x2 & s_x1))
# update
s_x1.symmetric_difference_update(s_x2)
print(s_x1)
# 判断
# Return True if two sets have a null intersection.
# 交集
x1 = {"a", "e", "c"}
x2 = {"e", "f", "g"}
inter = x1.isdisjoint(x2)
print(inter)
# 子集
# Report whether another set contains this set.
x1 = {"a", "b", "c"}
x2 = {"a", "b", "c", "e", "f", "g"}
inter = x1.issubset(x2)
print(inter)
# 父集
# Report whether this set contains another set.
x1 = {"a", "b", "c", "e", "f", "g"}
x2 = {"a", "b", "c"}
inter = x1.issuperset(x2)
print("父集:"+str(inter))
