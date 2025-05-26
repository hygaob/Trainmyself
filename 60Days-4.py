# import time

# my_time=int(input("請輸入秒數:"))

# for x in range(my_time):
#     seconds=my_time%60
#     minutes=my_time//60
#     print(f"{minutes:02}:{seconds:02}")
#     time.sleep(1)
#     my_time-=1
# print("時間到")

#python 中的List,sets,tuple

#List
fruits=["蘋果","柳橙","香蕉","椰子"]

print(fruits[1])

for f in fruits:
    print(f)

fruits.append("芭樂")
print(fruits)

fruits.remove("香蕉")
print(fruits)

print(fruits.index("柳橙"))

#列表可以傳入重複的值
fruits.append("蘋果")
print(fruits)

print(fruits.count("蘋果"))

#反轉
fruits.reverse()
print(fruits)

#Set
fruits_set={"葡萄","柳橙","檸檬","香蕉"}
print(fruits_set)

for f in fruits_set:
    print(f,end=" ")

#set不會加入重複值
fruits_set.add("檸檬")
fruits_set.add("西瓜")

print(fruits_set)

if "西瓜" in fruits_set:
    print("有一個西瓜")

#tuple元組
fruits_tuple=("香蕉","葡萄","柳橙","檸檬","香蕉")
print(fruits_tuple)
result=fruits_tuple.count("香蕉")
print(result)

result2=fruits_tuple.index("柳橙")
print(result2)

#tuple是不能用add，只能重新宣告
# fruits_tuple.add("西瓜")  #=>顯示錯誤
#Python 購物車程式

#List set tuple

goods=[] #列表List
prices=[]

while True:
    good = input("請輸入想購買的商品:")
    if good.lower()=="q":
        break
    price= float(input(f"請輸入 {good} 的價格"))
    goods.append(good)
    prices.append(price)
    

print(f"商品為: {goods}")
print(f"價格為: {prices}")

#enumerate 索引
for index,good in enumerate(goods):
    print(f"第{index+1}個商品 {good} 的價格{prices[index]:2}")
    
#計算總價
total=sum(prices)
print(f"總價格為{total}")