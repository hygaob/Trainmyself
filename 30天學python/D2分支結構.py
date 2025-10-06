#單位轉換程式
# value=float(input("請輸入長度:"))
# unit = input("請輸入單位(公尺/公分/英吋):")
# if unit=="公尺":
#     meter=value
# elif unit=="公分":
#     meter=value/100
# elif unit=="英吋":
#     meter=value*0.0254
# else:
#     meter=-1
# if meter==-1:
#     print("無效的單位")
# else:
#     print(f"{value} {unit} = {meter} 公尺")

#  擲骰子遊戲
# from random import randint
# 骰子數=int(input("請輸入骰子數:"))
# total=0
# for i in range(骰子數):
#     face = randint(1,6)
#     if face==1:
#         print("一點")
#     elif face==2:
#         print("兩點")
#     elif face==3:
#         print("三點")
#     elif face==4:
#         print("四點")
#     elif face==5:
#         print("五點")
#     else:
#         print("六點")
#     total+=face
# print(f"總點數為{total}")

#輸入三邊長如果可以構成三角形就計算周長和面積
# import math

# a=float(input("請輸入第一邊長:"))
# b=float(input("請輸入第二邊長:"))
# c=float(input("請輸入第三邊長:"))
# if a+b>c and a+c>b and b+c>a:
#     print("可以構成三角形")
#     perimeter=a+b+c
#     s=perimeter/2
#     area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#     print(f"周長為{perimeter:.2f},面積為{area:.2f}")
# else:
#     print("無法構成三角形")

#循環結構
#for in

#求1-100的總和
# total=0
# last_number=int(input("請輸入最後一個數字:"))
# step_number=int(input("請輸入遞增數字:"))
# for i in range(0,last_number+1,step_number):
#     total+=i
# print(f"1-{last_number}的{step_number}遞增總和為{total}")

#while
#猜數字遊戲
# import random
# ans=random.randint(1,100)
# guess=0
# count=0
# while True:
#     count+=1
#     guess=int(input("請輸入1-100的數字:"))
#     if guess==ans:
#         print(f"恭喜你猜對了,答案是{ans},你總共猜了{count}次")
#         break
#     elif guess<ans:
#         print("太小了")
#     else:
#         print("太大了")
# print(f"總共猜了{count}次")

#判斷質數
# from math import sqrt

# num=int(input("請輸入一個正整數:"))
# end = int(sqrt(num))
# is_prime=True
# # 1和0不是質數，自2開始檢查，只需檢查到平方根即可，
# # 除以任何大於平方根的數字都會得到一個小於平方根的商
# for i in range(2,end+1):
#     if num%i==0:
#         is_prime=False
#         break

# if is_prime:
#     print(f"{num}是質數")
# else:
#     print(f"{num}不是質數")

# 輸入兩個正整數，計算最大公約數和最小公倍數。
# x=int(input("請輸入第一個正整數:"))
# y=int(input("請輸入第二個正整數:"))
# if x>y:
#     x,y=y,x

# for factor in range(x,0,-1):
#     if x%factor==0 and y%factor==0:
#         gcd=factor
#         break
# lcm=x*y//gcd
# print(f"最大公約數為{gcd},最小公倍數為{lcm}")

#印出三角形圖案

# row= int(input("請輸入列數:"))
# #等腰三角形
# for i in range(1,row+1):
#     for j in range(row-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()
# #左下直角三角形
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# #右下直角三角形
# for i in range(1,row+1):
#     for j in range(row-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()

# #菱形
# #先印出上三角
# for i in range(1,row+1):
#     for j in range(row-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()
# #再印出下三角
# for i in range(row-1,0,-1):
#     for j in range(row-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()

import math

def draw_polygon(sides):
    if sides < 3:
        print("錯誤：邊數必須大於或等於 3")
        return
    
    # 設定多邊形大小
    radius = 10
    angle = 2 * math.pi / sides
    
    # 計算並繪製多邊形的每個點
    for i in range(sides):
        # 計算每個頂點的位置
        x = int(radius * math.cos(i * angle))
        y = int(radius * math.sin(i * angle))
        
        # 使用空格和星號繪製
        for j in range(y + radius):
            for k in range(x + radius):
                if abs(x - k) < 1 and abs(y - j) < 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

# 測試程式
try:
    sides = int(input("請輸入要繪製的多邊形邊數（3-8）："))
    draw_polygon(sides)
except ValueError:
    print("錯誤：請輸入有效的數字")