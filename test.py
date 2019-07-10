from dataclasses import dataclass
from typing import List

# @dataclass
class test:
    x=0
    def __init__(self):
        self.x=300

    def echo(self):
        print(self.x)


@dataclass
class demo:
    x = 0#被赋值了默认是，但是没有指定类型，可以不用放到所有变量最后面
    y:int

@dataclass
class C:
    x: int
    y: List[int] 
    t: int = 20  #被 赋值默认值并且指定类型的对象 一直在最后面(指定了类型)


class B:
    x = 0

    def __init__(self):
        self.x = 200


def add(a,b,c, d:1):
    pass
def add2(a,b,c, d:int):
    pass
def add3(a,b,c, d:int=10):
    pass


if  __name__=='__main__':
    t=test()
    t.echo()

    t = demo(y=10)
    print(t)

    b = B()
    print(b)
    a = [1, 2, 3]
    c = C(x=1, y=a)
    print(c)




