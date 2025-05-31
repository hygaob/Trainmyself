#Python 中的作用域

#變數範圍與作用域
#LEGB作用域順序(優先級)

#L-local 區域
#E-enclosed
#G-Global 全域
#B-built-in


#變數範圍
c=10
a=11

def function_one():
    a=1
    print("a:",a)

    def function_two():
        b=2
        print("b:",b)
        print("a:",a)   #enclosed  會使用 fun_a的變數
        print("c:",c)
    function_two()

function_one()

#B built-in  內建
from math import e

print(e)
print(round(e))

def function_e():
    print(e)

function_e()