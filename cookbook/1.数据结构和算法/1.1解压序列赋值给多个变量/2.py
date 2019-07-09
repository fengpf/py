# 1.2 解压可迭代对象赋值给多个变量

# 问题
# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？

# 解决方案
# Python 的星号表达式可以用来解决这个问题。比如，你在学习一门课程，在学期末的时候， 你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。如果只有四个分数，你可能就直接去简单的手动赋值， 但如果有 24 个呢？这时候星号表达式就派上用场了：
grades=70,80,90,100,65



def  drop_first_last(grades):
    f,*m,l=grades
    print(f,l)
    # return avg(*m)
    print(m) #m解压出来永远都是列表类型，不管数量是多少

def test():
    record=('tom','tom@example.com','121233','232233','23322323')
    name,email,*phone_nums=record
    print(name,email)
    print(phone_nums)

    *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
    print(trailing)
    print(current)

records=[
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4),
]

def do_foo(x,y):
    print('foo', x,y)

def do_bar(s):
    print('bar',s)

#py main函数之外也可以执行代码
for tag,*args in records:
    if tag=='foo':
        do_foo(*args)
    elif tag=='bar':
        do_bar(*args)



# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
line='nobody:*:2:/data/app/python'
uname,*fields,homedir=line.split(':')
print(uname,homedir)
print(fields)

# 有时候，你想解压一些元素后丢弃它们，你不能简单就使用 * ， 但是你可以使用一个普通的废弃名称，比如 _ 或者 ign （ignore）。
record=('acme', 50, 123.34, (7,9,2019))
name, *_, (*ign, year)=record ##如果被忽略是两个_,则后面将会覆盖前面的
print(name, _, ign, year)
# 输出 acme [50, 123.34] [7, 9] 2019
# 看到这，py确实牛逼~~

# 在很多函数式语言中，星号解压语法跟列表处理有许多相似之处。比如，如果你有一个列表， 你可以很容易的将它分割成前后两部分：
items=[1,2,3,4,5,6,7,8,9,10]
head,*tail=items
print(head)
print(tail)

# 如果你够聪明的话，还能用这种分割语法去巧妙的实现递归算法。比如：

def sum(items):
    head, *tail = items
    return head+sum(tail) if tail else head

#py 函数调用必须在声明之后？？
def main():
    drop_first_last(grades)
    test()
    print(sum(items))

if __name__ == "__main__":
        main()