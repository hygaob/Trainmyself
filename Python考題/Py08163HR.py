import math

# result=math.log2(2)
# print(result)
# a=pow(2,3)
# print(a)

str_a="Hello"
print(str_a,"\n" ,"next")
print(str_a[1:3])
print(len(str_a))
print(str_a[-1])
print(str_a[len(str_a)-1])

#空值
N=None
print(N)

print(type(N))

b1=True
b2=False
#print(len(b1))  #會出錯 布林值無法算長度

#BMI=體重/(身高**2)
# user_weight=float(input("請輸入體重"))
# user_height=float(input("請輸入身高"))/100
# user_BMI=user_weight/(user_height**2)
# print(f"{user_BMI:>10.5f}")

#f-string
num=62
print(f"{num} 二進制{num:b}  八進制{num:o}  十六進制{num:x}")

#邏輯運算符號
#not>and>or

#購物清單
#清單
shopping_list=["鍵盤","滑鼠"]
print(shopping_list)
#append 方法 用於列表增加項目
shopping_list.append("螢幕")
print(shopping_list)
shopping_list.append(True)
print(shopping_list)
shopping_list[3]="桌子"
print(shopping_list)
shopping_list.clear()
print(shopping_list)
shopping_list=[]
shopping_list.append("鍵盤")
shopping_list.append("滑鼠")
shopping_list.append("螢幕")
shopping_list.append("桌子")
print(shopping_list)
price_list=[799,599,850,1020]
print(max(price_list))
print(min(price_list))
print(sorted(price_list))
price_list.reverse()
print(price_list)
print(sorted(price_list,reverse=True))

#字典  key不能重複
contacts={"小明":"130000",
          "小明":"17000"}
print(contacts)
contacts={"小明":"130000",
          "小華":"17000"}
print(contacts)
print(len(contacts))

# #網路關鍵字字典
# slang_dict={"核能":"核三重啟",
#             "大罷免":"區域立委罷免案"}
# #增加關鍵字
# slang_dict["地震"]="2024年的地震不論規模、次數都創下台灣十四年來的的新高"
# slang_dict["颱風"]="天災的震撼到了11月更是驚人，極少出現颱風的11月在今年居然史無前例的有三個強颱造訪"
# print(slang_dict)

# query=input("請輸入想查詢的關鍵字: ")
# if query in slang_dict:
#     print(f"查詢關鍵字 {query} 簡述如下{slang_dict[query]}")

# else:
#     print("您查詢的關鍵字未收錄")


#for loop
#for 變量名 in 可迭代對象:
    #對每一變量執行程序
    #...
temperature_dict={"111":36.4,"112":36.2,"113":36.5,"114":37.8,"115":35.5,"116":39.2}

for staff_id, temp in temperature_dict.items():
    if temp>=38:
        print(staff_id)

#for 結合 range
sum=0
for i in range(1,101):
    sum+=i

print(sum)

#while循環
#while 條件:
    #程序
#須注意對條件進行變化，否則進入無限循環

#計算器
# total = 0
# count = 0
# user_input=input("請輸入數字(完成所有數字輸入後，清輸入q中止程序)")
# while user_input!="q":
#     num = float(user_input)
#     total += num
#     count += 1
#     user_input=input("請輸入數字(完成所有數字輸入後，清輸入q中止程序)")
# if count ==0:
#     result=0
# else:
#     result = total/count
# print(f"您輸入的數字平均值為{result:.2f}")

#計算扇形面積
#DRY原則
#自定義函數
def calculate_sector_1():
    #接下來是定義函數的代碼
    central_angle_1=160
    radius_1=30
    sector_area_1=central_angle_1/360*3.14*radius_1**2
    print(f"此扇形面積為:{sector_area_1}")
calculate_sector_1()

def calculate_sector_2(angle,radius):
    #接下來是定義函數的代碼
    #central_angle_1=angle
    #radius_1=radius
  
    sector_area_1=angle/360*3.14*radius**2
    print(f"此扇形面積為:{sector_area_1}")
    return    #使用return把結果傳到外面

calculate_sector_2(30,30)

#使用return可以返回定義函數內的值
def calculate_sector_2(angle,radius):
    #接下來是定義函數的代碼
    #central_angle_1=angle
    #radius_1=radius
  
    sector_area_1=angle/360*3.14*radius**2
    print(f"此扇形面積為:{sector_area_1}")
    return sector_area_1    #使用return把結果傳到外面


"""
寫一個BMI函數，函數名為calculate_BMI
1. 可以計算任意體重和身高的BMI值
2. 執行過程中打印一句話，"您的BMI分類為 XX類"
3. 返回計算出的BMI

BMI=體重/(身高**2)

BMI分類
偏瘦:BMI<=18.5
正常:18.5<BMI<=25
偏胖:25<BMI<=30
肥胖:BMI>30
"""

def calculate_BMI(weight,height):
    BMI=weight/(height**2)
    if BMI <=18.5:
        category="偏瘦"
    elif BMI<=25:
        category="正常"
    elif BMI<=30:
        category="偏胖"
    else:
        category="肥胖"
    print(f"您的BMI為{BMI},分類為{category}")
    return BMI

result_BMI=calculate_BMI(70,1.8)
print(result_BMI)

#import 引入函數庫

#import statistics
#要使用statistics中的median
#可以引入python官方函式庫，但如果需引入第三方函式庫，需下載後引入
#第三方需使用終端機pip install *函示庫名*

#物件導向(面向對相)(C#、python)OOP 介紹
#對比為 函式導向(面向過程)(java、C)，程式拆分為單一步驟，一行行執行
# 物件導向可以減少程式碼數量，依需求調用物件
#模擬真實世界，將所有物件定義為類別，將物件綁定類別屬性，更有利於邏輯判斷撰寫

#class 分類
#  屬性
#  方法


#範例 定義ATM類
class ATM:  #分類
    def __init__(self,編號,銀行,支付):  #屬性
        self.編號=編號
        self.銀行=銀行
        self.支付=支付

# 創建兩個ATM對象
atm1=ATM("001","國泰世華","網路銀行")
atm2=ATM("002","中國信託","實體銀行")

#定義紙幣類
class 紙幣:
    def __init__(self,編號,面值,發行年分):
        self.編號=編號
        self.面值=面值
        self.發行年分=發行年分

#創建兩個紙幣對象
紙幣1=紙幣("AA00000",50,"2015")
紙幣2=紙幣("AA00001",100,"2017")        

print(atm1.編號)
print(紙幣1.編號)

#封裝、繼承、多模態
#封裝:使用封裝可以將多行函示封裝在裡面，調用只需呼叫方法屬性即可有功能
#繼承
    #父類:學生
    #子類:小學生、大學生
#方法:寫作業

#範例
# class CutCat:
#     def __init__(self):
#         #接下來是一些構造函數代碼
#         self.name="Lambton"
#         #...
class CutCat:
    def __init__(self,cat_name,cat_color,cat_age):  #基礎屬性
        #接下來是一些構造函數代碼
        self.name=cat_name
        self.age=cat_age
        self.color=cat_color
        #...
    #def method  定義方法 
    def speak(self):
        print("貓咪叫"+"喵"*self.age)  #注意可以調用其他def中的函數


cat1=CutCat("Jojo","橙色",3)
#print(f"貓咪名子是{cat1.name}")
print(f"貓咪名子是{cat1.name}，顏色是{cat1.color}，年齡是{cat1.age}")
cat1.speak()

#定義一個學生類別
#要求
#1. 屬性包括學生姓名、學號、國英數三科成績
#2. 能夠設置學生某科成績
#3. 能夠打印出該學生所有科目成績

class Student:
    def __init__(self,student_name,student_id):
        self.name=student_name
        self.student_id=student_id
        self.grades={"國文":0,"數學":0,"英文":0}  #初始化成績為0

    def set_grade(self,course,grade):  #方法更改成績
        if course in self.grades:      #如果科目存在則執行
            self.grades[course]=grade   
        else:
            print("無此科目")
    
    def print_grades(self):   #列印所有成績
        print(f"學生{self.name}，學號{self.student_id}的成績為")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")


chen=Student("小陳","10025")
zeng=Student("小曾","12345")

print(chen.name)
print(zeng.grades)

zeng.set_grade("國文",95)
print(zeng.grades)

chen.set_grade("國文",88)
chen.set_grade("數學",55)
chen.set_grade("英文",95)

chen.print_grades()