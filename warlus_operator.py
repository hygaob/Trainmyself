#python 獠牙運算符:=

#獠牙運算符
#賦值表達式:=
#賦值運算式=

#python 3.8後才新增功能
#可將值分配給變數

happy=True
print(happy)

print(happy:=True)
print(happy:=False)
#print(happy=True)  #會出錯

foods = []
# while True:
#     food = input('你喜歡吃甚麼食物?')
#     if food =='quit':
#         break
#     foods.append(food)

#使用獠牙運算符進一步簡化
while (food :=input('你喜歡吃甚麼食物?')) !='quit':
    foods.append(food)


print(foods)
