#1.1 解压序列赋值给多个变量

# 问题
# 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？

# 解决方案
# 任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多个变量。 
# 唯一的前提就是变量的数量必须跟序列元素的数量是一样的。
p=(4,5)
x,y=p
print(x,y)
# ValueError: not enough values to unpack (expected 3, got 2)
# x0,y0,z0=p 

data = ["tom", 30, 92.3, (2019, 7, 9)]
name,age,birth,date=data
print(name,age,birth,date)

# 有时候，你可能只想解压一部分，丢弃其他的值。
# 对于这种情况 Python 并没有提供特殊的语法。 但是你可以使用任意变量名去占位，和go一样，到时候丢掉这些变量就行了。
_,_,birth0,_=data
print(birth0)

# 实际上，这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。 
# 包括字符串，文件对象，迭代器和生成器。
s="hello"
a,b,c,d,e=s
print(a,b,c,d,e)