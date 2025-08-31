#數學方法

#加減乘除
apples=3
apples=apples+1
print(apples)
apples+=2
print(apples)
apples-=1
print(apples)
apples*=2
print(apples)
#指數
x=5
x=x**3
print(x)
x**=2
print(x)
#模數=>正除法
#10 mod 3 = 3...1
#11 mod 3 = 3...2
#12 mod 3 = 4...0

print(10 % 3)  #餘數
print(10 // 3) #倍數


#內建數學函數

#次方 pow
print(pow(3,3))

#最大值Max 與 最小值 min
x=1
y=2
z=3
print(max(x,y,z))
print(min((x,y,z)))

#四捨五入 round

a=3.14
print(round(a))

b=3.5
print(round(b))

#絕對值
c=-10
print(abs(c))

# #四捨五入、無條件進位、無條件捨去
# import math
# x=9.5
# print(round(x)) #四捨五入
# print(math.ceil(x)) #無條件進位
# print(math.floor(x)) #無條件捨去

# #圓周率pi
# print(math.pi)

# #圓周長計算
# r=float(input("請輸入半徑"))
# 周長=2*math.pi*r
# print(f"圓周長為{round(周長,2)}")
# #圓面積計算pi*r**2
# 面積=math.pi*r**2
# print(f"圓面積為{round(面積,2)}")

#邏輯運算符號
#and or not

# temp=int(input("請輸入現在溫度:"))

# #and
# if temp >0 and temp<30:
#     print("溫度是適宜的")
# else:
#     print("溫度是不適宜的")

# #or
# if temp <0 or temp>=30:
#     print("溫度是不適宜的")
# else:
#     print("溫度是適宜的")


#python的字串方法
#len()、find()、capitalize()、upper()、lower()、count()、replase()

#可用help(str)查詢完整語法
name="code traning HY"

#幾個字元
length=len(name)
print(f"全名 {name} 共有 {length} 個字元")

#找到第一個空格
space_pos=name.find(" ")
print(f"全名 {name} 的空格在 {space_pos} 個字元")

#capitalize()、upper()、lower()
#自首大寫
name2=name.capitalize()
print(name2)
#全數大寫
name3=name.upper()
print(name3)
#全數小寫
name4=name3.lower()
print(name4)

# #count() 計算指定字元數量
# phone_number=input("請輸入你的電話號碼")
# dash_count=phone_number.count("-")
# print("你的電話號碼裡有",dash_count,"個 - 個 - ")
# #replase() 替代指定字元
# new_phone_number=phone_number.replace("-","")
# print("你的電話號碼是",new_phone_number)


# #練習
# #請輸入使用者名稱
# #使用者名稱不能超過12字元
# #使用者名稱不能包含空格
# #使用者名稱不能包含數字
# #如果都符合的話，顯示 歡迎+使用者名稱

# username=input("請輸入你的使用者名稱 : ")

# if len(username) >12:
#     print("使用者名稱超過12個字元")

# elif " " in username:
#     print("使用者名稱包含空格")

# elif not username.isalpha():  #isalpha是指是否為英文
#     print("使用者名稱包含數字")

# else:
#     print("歡迎 ",username)

# 字串索引
credit_card_number="1234-5678-9876-5432"

first_char=credit_card_number[0]
print("第一個字元: ",first_char)

second_char=credit_card_number[1]
print("第二個字元: ",second_char)

first_4_char= credit_card_number[0:4]
print("前四個字元",first_4_char)

last_char=credit_card_number[-1]
print("last char is",last_char)

last_two_char=credit_card_number[-2]
print("最後第二個字元是",last_two_char)

#index 字串索引
my_Mail="qaz011119@gmail.com"

at_index=my_Mail.index("@")
print("@在第",at_index,"個字元")
print("電子郵件帳號為",my_Mail[:at_index])
print("電子郵件網域為",my_Mail[at_index:])

#f-string 字串格式化用法

price_1=3.321
price_2=-77
price_3=15.11

print(f"價格1為{price_1}\n"
      f"價格2為{price_2}\n"
      f"價格3為{price_3}")

#小數點精確度
print(f"價格1為{price_1:.2f}\n"
      f"價格2為{price_2:.2f}\n"
      f"價格3為{price_3:.2f}")

#加上正負符號
print(f"價格1為{price_1:+.2f}\n"
      f"價格2為{price_2:+.2f}\n"
      f"價格3為{price_3:+.2f}")

#對齊 < > ^
print(f"價格1為{price_1:>+10.2f}\n"
      f"價格2為{price_2:<+10.2f}\n"
      f"價格3為{price_3:^+10.2f}")  #10位元寬度

#混合不同符號
print(f"價格1為{price_1:>+10.2f}\n"
      f"價格2為{price_2:<+10.2f}\n"
      f"價格3為{price_3:^+10.2f}")  #10位元寬度

#while

# name=input("請輸入你的名子:")
# while name=="":
#     name=input("請輸入你的名子:")
# print(f"你好 {name}")

# food = input("請輸入你喜歡吃的食物:")
# while food !="q":
#     print(f"你喜歡的食物是{food}")
#     food = input("請輸入你喜歡吃的食物:")
# print("再見")

# #輸入1到10之間的數字:
# num=int(input("請輸入1到10之間的數字:"))
# while num<1 or num >10:
#     print(f"你輸入的數字{num}是無效的")
#     num=int(input("請輸入1到10之間的數字:"))

# print(f"你輸入{num}")

for x in range(1,11):
    print(x)

for x in reversed(range(1,11)):
    print(x)
print("Happy new year")

credit_card_number="1234-5678-9876-5432"
for x in credit_card_number:
    print(x)

#continue-跳過9
credit_card_number="1234-5678-9876-5432"
for x in credit_card_number:
    if x=="9":
        continue
    else:
        print(x)

#break-遇到9跳出迴圈
credit_card_number="1234-5678-9876-5432"
for x in credit_card_number:
    if x=="9":
        break
    else:
        print(x)

#字典dictionary
#鍵:key  值:value
my_dict={"a":1,"b":11,"c":111}
for x in my_dict:
    print(x)   #此時只會印出鍵  值沒有呼叫

for x,y in my_dict.items():
    print(x,y)

import os
import time

#跑馬燈練習
# def main():
#     content = "我要挑戰IT鐵人"
#     while True:

#         os.system("cls")  #清除螢幕上的輸出(on windows)
#         print(content)

#         time.sleep(0.2)  #休眠200ms
#         content=content[1:]+content[0]

# if __name__=="__main__":
#     main()

#驗證碼練習
import random

def generate_code(code_len=4):
    all_chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos=len(all_chars)-1 #計算全部字元長度
    code=""
    for i in range(code_len):
        index=random.randint(0,last_pos)
        code+=all_chars[index]
    return code

def main():
    print(generate_code())
    print(generate_code(5))
    print(generate_code(7))
    print(generate_code(2))

if __name__ == "__main__":
    main()

def get_suffix (filename, has_dot=False):

    # filename : 文件名 has_dot : 返回的檔案型態文字是否需要带點
    pos = filename.rfind('.')       # 找到文件名中'.'的位置
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1    
        return filename[index:]     # 文件名中點或點 + 1 後的所有文字
    else:
        return ''
        
def main() :
    print(get_suffix('name.py',True))
    print(get_suffix('picture.png',False))

if __name__ == '__main__':
    main()


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:   # 判斷最大的元素
            m2 = m1
            m1 = x[index]
        elif x[index] > m2: # 判斷第二大的元素
            m2 = x[index]
    return m1, m2
    
def main() :
    print(max2('qazwsxedc'))
    print(max2('abcdefgh'))

if __name__ == '__main__':
    main()


def is_leap_year (year):  # 判斷是否為閏年
    
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day (year, month, date):
    # python 的 bool，也就是 True 和 False，實質上是 int，也就是 1 和 0
    # True = 1，False = 0
    # 函數返回 True 即為返回 list[1]，反之 list[0]
    days_of_month = [ 
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ] [is_leap_year(year)]
    total = 0
    for index in range (month - 1):
        total += days_of_month[index]
    return total + date

def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))

if __name__ == '__main__':
    main()


def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num                     # 在一個串列中建立指定列數的空串列
    for row in range (len(yh)):
        yh[row] = [None] * (row + 1)    # 將串列中每個空串列所需要的元素設為 None
        for col in range (len(yh[row])):
            if col == 0 or col == row:  # 判斷串列中每個串列的頭和尾並將其設為 1
                yh[row][col] = 1
            else:                 # 其餘的值為上一列同一行的值 + 上一列前一行的值 
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end = '\t')
        print()

if __name__ == '__main__':
    main()


from random import randrange, randint, sample

def display (balls):                     # 輸出雙色球選號
    # enumerate 函數能同時列出串列中的元素的數據和位置
    for index, ball in enumerate(balls): 
        if index == len(balls) - 1:      # 在最後一個數據前印出 '|'
            print('|', end =' ')
        print('%02d' % ball, end =' ')
    print()

def random_select():                      # 隨機選擇一組號碼
    
    red_balls = [x for x in range(1, 34)] 
    selected_balls = []                   
    # sample 函數用意為從列表中選擇不重複 n 個元素
    selected_balls = sample(red_balls, 6) 
    selected_balls.sort()                 # 將產生的 6 個隨機數排序
    selected_balls.append(randint(1, 16)) # 加入隨機產生 1 ~ 16 的數
    return selected_balls

def main():
    n = int(input('輸入選擇下注的數量: '))
    for _ in range(n):
        display(random_select())

if __name__ == '__main__':
    main()



# 練習3 - 井字遊戲。
import os,random

def print_board(board):         # 輸出井字的樣子
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

def main():
    init_board = {
        '1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' ' }
    begin = True
    while begin:
        curr_board = init_board.copy()  # 複製初始的空字典
        begin = False
        turn = random.choice(['x','o']) # 隨機讓兩者開始
        counter = 0
        print_board(curr_board)
        while counter < 9:
            move = input('輪到 %s ,請輸入位置: ' % turn)
            if curr_board[move] == ' ': # 判斷位置是否為' '，空則記錄現在的 turn
                counter += 1
                curr_board[move] = turn 
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            print_board(curr_board)
        choice = input('再玩一局 ? (yes | no) ')
        begin = choice == 'yes'

if __name__ == '__main__':
    main()