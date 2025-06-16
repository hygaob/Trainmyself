#python filter 過濾
#可用來過濾可迭代的資料結構(list,....)

friends=[
    ("Bob",18),
    ("Steven",17),
    ("Micheal",19),
    ("Susan",16)
]

age_filter=lambda data: data[1]>=18

can_drink_friends=list(filter(age_filter,friends))
print(can_drink_friends)

for friend in can_drink_friends:
    print(friend)