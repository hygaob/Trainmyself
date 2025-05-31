# Python 中的Module

# import math
# #help(math) #可得到模組介紹

# print(math.pi)
# print(math.pow(3,2))
# print(math.pow(3,3))

# import math as m  #可簡化調用模組的代號

# print(m.pi)
# print(m.pow(3,2))
# print(m.pow(3,3))

# num=20.635
# #ceil 無條件進位
# print(m.ceil(num))

# #floor 無條件捨去
# print(m.floor(num))

# #round 四捨五入
# #print(m.round(num)) #無法執行 因為round已改至內建函數執行
# print(round(num))

# #單獨引入子模組
# from math import pi
# print(pi)

#自訂模組
#建立一個自訂模組名稱的.py檔=>這裡用my_module.py來看
import my_module as m

print(m.pi)
print(m.square(3))
print(m.cube(4))
print(m.area(5))

