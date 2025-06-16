#python 中的map

#map(可迭代的[列表],函式)

store=[
    ('襯衫',20),  #美金
    ('褲子',30),
    ('夾克',50),
    ('襪子',10)
]

to_euros=lambda data:(data[0],data[1]*0.82)  #美金轉歐元

store_euros=list(map(to_euros,store))
print(store_euros)

to_NTD=lambda data:(data[0],data[1]*30)  #美金轉台幣

store_NTD=list(map(to_NTD,store))
print(store_NTD)

NTD_to_US=lambda data:(data[0],data[1]/30)  #台幣轉美金

store_US=list(map(NTD_to_US,store_NTD))

for item in store_US:
    print(item)