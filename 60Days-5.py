#python 字典

#鍵-->值對
#key->value

capital={
    "United States":"Washington DC",
    "Japan":"Tokyo",
    "France":"Paris",
    "Russia":"Moscow"
}

#get()取得鍵值對
print(capital.get("Japan"))

#Update()更新鍵值對
capital.update({"Germany":"Berlin"})
print(capital)

#pop()刪除->用拿出的方式
capital.pop("United States")
print("刪除後的字典",capital)

#value()獲取所有的值
print(capital.values())

#items()獲取所有鍵值對
print(capital.items())

#應用-購物車菜單系統
menu={
    "披薩":300,
    "爆米花":200,
    "薯條":90,
    "洋于片":60,
    "軟麵包條":120,
    "蘇打水":60,
    "檸檬水":90
}

total =0
cart=[]
print(f"菜單")
print("------------------------------------")

for item, price in menu.items():print(f"{item}:{price}")
    
while True:
    food = input("請輸入一個菜單項目(輸入q結束)")
    if food == "q":
        break
    elif menu.get(food) is None:
        print("沒有這個商品")
    else:
        cart.append(food)
        total += menu.get(food)
        print(food,end=" ")
    
print(f"總共:{total}元")

