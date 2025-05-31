#args=> arguments 任意數量的參數 * =>打包進tuple
#kwargs=>關鍵字+args(keyword args) ** =>打包進dictionary

#args
# 
# def add(a,b):
#     return a+b
# print(add(1,2))

#new*

def add(*args):   #如此可以任意數量參數
    total = 0
    for arg in args:
        print(f"arg: {arg}")
        total += arg
    print(total)
    return total
    
print(add(1,2,3))
add(2,3,4)

#kwargs => 關鍵字 + args(keyword args) ** =>dictionary

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key}  value: {value}")

print_info(name="Alice",age="25",occupation="Engineer")
