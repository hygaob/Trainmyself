#random 隨機數
import random
#help(random)

#randint()隨機整數
print(random.randint(1,10))
#random()
print(random.random())

#列表中隨機選擇一個元素
options=["剪刀","石頭","布"]
rand_option=random.choice(options)
print(f"電腦選擇的是:{rand_option}")

#將一個列表打亂
cards=["2","3","4","5","6"]
random.shuffle(cards)
print(cards)

#猜數字遊戲
# low=1
# high=100
# number=random.randint(low,high)
# guesses=0
# while True:
#     #猜數字
#     guess=int(input(f"請猜一個介於{low}~{high}之間的數字: "))
#     guesses+=1
#     if guess <number:
#         print("猜的數字太小了")
#     elif guess > number:
#         print("猜的數字太大了")
#     else:
#         print(f"恭喜答對:{number}")
#         print(f"總共猜了{guesses}次")
#         break


#猜拳遊戲

#石頭(Rock)
#剪刀(Scissors)
#布(Paper)

# player=None
# computer=None

# running=True
# options=["剪刀","石頭","布"]
# while running:
#     player= input("請輸入剪刀、石頭、布:")
#     while player not in options:
#         input("輸入錯誤，請輸入剪刀、石頭、布:")
#     computer=random.choice(options)
#     print(f"玩家: {player}，電腦:{computer}")
#     if player == computer:
#         print("平手")
#     elif player == "剪刀" and computer=="布":
#         print("玩家勝利")
#     elif player == "布" and computer=="石頭":
#         print("玩家勝利")
#     elif player == "石頭" and computer=="剪刀":
#         print("玩家勝利")
#     else:
#         print("電腦獲勝")
#     play_again=input("再玩一局?(y/n)").lower()
#     if not play_again =="y":
#         running=False
# print("謝謝遊玩")

#骰子遊戲

dice_art = {    #字典檔
    1: (        #元組
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐", # 0
        "│ ●   ● │", # 1
        "│ ●   ● │", # 2
        "│ ●   ● │", # 3
        "└───────┘", # 4
    ),
}

#print(dice_art.get(6))  #印出會變一行
number=5
def get_dict_number(number):
    for i in range(5):
        print(dice_art.get(number)[i])

get_dict_number(number)

num_dice=int(input("請輸入要擲幾個骰子:"))
dice=[]
for i in range(num_dice):
    dice_number=random.randint(1,6)
    dice.append(dice_number)
print(dice)

for i in dice:
    get_dict_number(i)
print(f"總和{sum(dice)}")


