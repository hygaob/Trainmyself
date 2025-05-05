#程式柴6小時學者課程
#https://youtu.be/lvH4-4iYjgs?si=xPKdLkr5fQ1Qz1e3
#python 利於數據分析
#一 變數
x= 0
print(x)
x= 5
print(x)

age = 25
print(f"我得年紀是{age}")

#整數
age=30
#float 浮點數
gpa= 3.3

print(f"我的GPA是{gpa}分")

#String字串
name='Peter'
print(f"我的名子是{name}")
print(type(name))
#Boolean True, False
is_online=True
print(f"在線上嗎?{is_online}")
print(type(is_online))

#型別轉換 Type Casting

name="John"
age=21
gpa=3.3
is_student=True

#顯式 隱式型別轉換
#顯式轉換
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#把age轉成浮點數
print(f"現在AGE={age}，是{type(age)}")
age= float(age)
print(f"現在AGE={age}，是{type(age)}")

#把is_student轉成字串
print(f"現在是否為學生={is_student}，是{type(is_student)}")
is_student=str(is_student)
print(f"現在是否為學生={is_student}，是{type(is_student)}")

#隱式型別轉換
x=10
y=2.0
x=x/y
print(x)
print(type(x))
#x會自動轉換成浮點數

#input 使用者輸入
# name=input("請輸入名子:")
# print(f"我的名子是{name}")
#練習一:填詞遊戲
# adj_1=input("請輸入第一個形容詞:")
# adj_2=input("請輸入第二個形容詞:")
# adj_3=input("請輸入第三個形容詞:")
# noun=input("請輸入一個名詞:")
# verb=input("請輸入一個動詞:")

# print(f"我今天去了一個{adj_1}的地方，看到了{noun}，這個{noun}很{adj_2}，正在{verb}，感到非常{adj_3}")

#練習二:計算矩形面積
# length=float(input("請輸入矩形長度:"))
# width=float(input("請輸入矩形寬度:"))

# area=length*width
# print(f"矩形面積為:{area}單位平方")

#練習三:購物車程式
# item=input("你想購買什麼物品:")
# price=float(input("價格是多少?"))
# quantity=int(input("你需要多少件?"))

# total=price*quantity
# print(f"你購買了{quantity}個{item}，購物總價是{total}元")

#Python中的數學

#加減乘除
#加法
apples=3
apples=apples+1
print(apples)
apples=apples+1
print(apples)
apples+=1
print(apples)

#減法
oranges=5
oranges=oranges-1
print(oranges)
oranges-=1
print(oranges)

#乘法
a=2
a=a*2
print(a)
a*=3
print(a)

#除法
b=100
b=b/4
print(b)
b/=5
print(b)

#指數
x=3
x=x**3
print(x)
x**=3
print(x)

#mod模數
#10 mod 3 等於 3 餘 1
print(10%3)
#11 mod 3 等於 3 餘 2
print(11%3)
#12 mod 3 等於 4 餘 0
print(12%3)

#內置數學函數
#次方pow
print(pow(3,2))
#最大值Max最小Min
x=1
y=2
z=3
print(max(x,y,z))
print(min(x,y,z))

#四捨五入 round
a=3.1415
print(round(a))
b= 3.6
print(round(b))
c= 3.4538
print(round(c,3))

#絕對值
d= -4
print(abs(d))

#四捨五入、無條件進位、無條件捨去
import math
x=9.543
print(round(x))
print(math.ceil(x))  #無條件進位
print(math.floor(x))  #無條件捨去

#圓周率
print(math.pi)

#計算圓周長2*pi*R
# radius=float(input("輸入半徑"))
# print(f"周長等於:{2*math.pi*radius}")
# print(f"周長等於:{round(2*math.pi*radius,2)}")  #四捨五入
# #計算圓面積pi*R**2
# print(f"圓面積等於:{(math.pi)*(radius**2)}")
# print(f"圓面積等於:{round((math.pi)*(radius**2),2)}")

#if else elif控制流程

#boolean
# for_sale = False
# if for_sale:
#     print("此項目正在出售")
# else:
#     print("此項目未出售")


# #if else
# age = int(input("請輸入你的年齡:"))
# if age>=18:
#     print("已成年")
# else:
#     print("未成年")


# #elif =>else if 簡寫
# if age>=100:
#     print("你的年紀太大，無法註冊")
# elif age>=18:
#     print("已成年，可以註冊")
# elif age<0:
#     print("你還沒出生")
# else:
#     print("未成年無法註冊")

#練習
#計算機程式
# operator=input("請輸入計算符號(加法:+，減法:-，乘法:*，除法:/): ")
# num1=float(input("請輸入第一個數字:"))
# num2=float(input("請輸入第二個數字:"))

# if operator =="+":
#     result = num1+num2
# elif operator =="-":
#     result = num1-num2
# elif operator =="*":
#     result = num1*num2
# elif operator =="/":
#     result = num1/num2
# else:
#     print("符號無效")

# print(f"{num1} {operator} {num2} = {result}")

#練習-體重轉換器

# weight=float(input('請輸入你的體重:'))
# unit = input("請輸入原始單位:(kg or lb)").upper

# print(f"你的體重是{weight} {unit}")

# if unit == "KG":
#     weightnew=weight*2.2
# elif unit =="LB":
#     weightnew=weight/2.2
# else:
#     print("輸入單位錯誤")

# print(f"體重轉換為{weightnew}")

#溫度轉換
# unit = input("請輸入當前溫度單位(攝氏:C，華氏:F):")
# temp = float(input("請輸入溫度值:"))

# if unit =="C":
#     #社是轉華氏
#     temp = round(9*temp/5+32)
#     print(f"當前溫度為{temp} F")
# elif unit=="F":
#     temp = round((temp-32)*5/9)
#     print(f"當前溫度是{temp} C")
# else:
#     print("單位輸入錯誤")

#Python 中的邏輯運算子(運算符)

#and or not
# temp = 25
# temp = int(input("請輸入現在溫度:"))
# if temp>0 and temp <30:  # true*false = false
#     print("溫度適宜")    
# else:
#     print("溫度是不適宜")

# if temp<=0 or temp >=30:  # true + false = True
#     print("溫度不適宜")
# else:
#     print("溫度是適宜")

# Python 的字串方法
# len()、find()、capitalize()、upper()、lower()、count()、replase()

#help(str)

#使用者的全名
# name = "高浩瑜的python code 練習"
# #幾個字元
# length= len(name)
# print(f"你的全名共有{length}個字元")

# #找到第一個空格
# space_pos= name.find(" ")
# print(f"第一個空格出現在{space_pos}位")

# #讓第一個字大寫
# name2 = "python Code"
# name2_capitalized = name2.capitalize()
# print(name2_capitalized)

# #全部大寫
# name2_upper=name2.upper()
# print(name2_upper)
# #全部小寫
# name2_lower=name2.lower()
# print(name2_lower)

# #count
# phone_number = input("請輸入電話號碼")
# dash_count=phone_number.count("-")
# print(f"電話號碼中有{dash_count}個 - ")

# #replace
# phone_number2= phone_number.replace("-","")
# print(f"電話號碼新格式為{phone_number2}")

#程式練習:驗證使用者輸入合法性
#-使用者名稱不得超過12字元
#-使用者名稱不得包含空格
#-使用者名稱不得包含數字
#-如果都符合，顯示 【歡迎+使用者名稱】

# username= input("請輸入你的使用者名稱:")

# if len(username)>12:
#     print("使用者名稱不得超過12字元")
# elif username.count(" ")>0:
#     print("使用者名稱不得包含空格")
# elif not username.isalpha():
#     print("使用者名稱包含數字")
# else:
#     print(f"【歡迎{username}】")


#字串索引
#用其得知字串中的序列，首位是0
credit_number="1234-5678-9876-5432"

first_char=credit_number[0]
print(f"第一個字元{first_char}")

second_char=credit_number[1]
print(f"第一個字元{second_char}")

first_four_num= credit_number[0:4]  #這裡要注意會列出0-3個字
print(f"前四個數字是{first_four_num}")

last_one=credit_number[-1]   #輸入零會回傳第0個=>1
print(f"最後一個字元是{last_one}")

last_tow=credit_number[-2]
print(f"最後第二位是{last_tow}")

#Email 字串分析
email="qaz011119@gmail.com"
index_At=email.index("@")
print("@在第",index_At)
print("email使用者為",email[:index_At])
print("email網域為",email[index_At+1:])

#f-string 的字串格式化
price_1=3.321
price_2=-77
price_3=15.11

#增加小數點精確度
print(f"價格1為{price_1:.2f}\n"
      f"價格2為{price_2:.1f}\n"
      f"價格3為{price_3:.2f}")

#增加正負號
print(f"價格1為{price_1:+.2f}\n"
      f"價格2為{price_2:+.1f}\n"
      f"價格3為{price_3:+.2f}")

#對齊<>^
print(f"價格1為{price_1:>10.2f}\n"
      f"價格2為{price_2:<10.1f}\n"
      f"價格3為{price_3:^10.2f}")  #位數會定為10位

#使用不同符號
print(f"價格1為{price_1:>+10.2f}\n"
      f"價格2為{price_2:<+10.1f}\n"
      f"價格3為{price_3:^-10.2f}")  #位數會定為10位