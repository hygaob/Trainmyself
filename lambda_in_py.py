#Python中的lambda
#lambda有函式的功能 一行就可以寫完

#ex1 double

def double(x):
    return x*2

print(double(5))

#lambda

double2=lambda x: x*2
print(double2(50))

#ex2 乘法
multiply=lambda x,y : x*y  #lambda可以傳入多個參數
print(multiply(7,8))

#ex3 if else 條件語句

result=lambda x: f"{x}是偶數" if x%2==0 else f"{x}是奇數"

print(result(15))

#ex4 處理字串

full_name=lambda first_name, last_name: f"{first_name} {last_name}"
print(full_name("高","浩瑜"))