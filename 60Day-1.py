#開始學習python
#第一天:變數練習
#1. 基本變數範例
name="小明"
age=20
height=170
weight=60
is_student=True

print(f"姓名:{name}")
print(f"年齡:{age}")
print(f"身高:{height}")
print(f"體重:{weight}")
print(f"是否為學生:{is_student}")

#2. 數據類型轉換
str_age="20"
#轉換為整數
int_age=int(str_age)
#轉換為浮點數
float_age=float(str_age)
#轉換為布林值
bool_age=bool(str_age)
str_age2=str(bool_age)

print(f"原始字串為:{str_age} , 類型為{type(str_age)}")
print(f"字串轉換為整數:{int_age} , 類型為{type(int_age)}")
print(f"字串轉換為浮點數:{float_age} , 類型為{type(float_age)}")
print(f"字串轉換為布林值:{bool_age} , 類型為{type(bool_age)}")

 #3. 串列練習[]
fruits=["蘋果","香蕉","橘子"]
print(f"原始串列為:{fruits}")

#新增元素
fruits.append("西瓜")
print(f"新增元素後的串列為:{fruits}")

#刪除元素
fruits.remove("香蕉")
print(f"刪除元素後的串列為:{fruits}")

#修改元素
fruits[1]="芒果"
print(f"修改元素後的串列為:{fruits}")
print(f"第2樣水果為:{fruits[1]}")

#4. 字典練習{}
student={"name":"小明","age":20,"height":170,"weight":60}
print(f"原始字典為:{student}")

#新增元素
student["gender"]="男"
print(f"新增元素後的字典為:{student}")

#刪除元素
del student["age"]
print(f"刪除元素後的字典為:{student}")

#修改元素
student["name"]="小華"
print(f"修改元素後的字典為:{student}")

#5. 集合練習{}
numbers={1,2,3,4,5,6,7,8,9,10}
print(f"原始集合為:{numbers}")

#新增元素
numbers.add(11)
print(f"新增元素後的集合為:{numbers}")

#刪除元素
numbers.remove(3)
print(f"刪除元素後的集合為:{numbers}")

#6. 元組練習()
colors=("紅色","藍色","綠色")
print(f"原始元組為:{colors}")

#新增元素
colors=colors+("黃色",)
print(f"新增元素後的元組為:{colors}")

#7. 字串練習
text="Hello, World!"
print(f"原始字串為:{text}")

#新增元素
text=text+"Python"
print(f"新增元素後的字串為:{text}")

#8. 布林值練習
is_true=True
is_false=False

print(f"布林值為:{is_true}")
print(f"布林值為:{is_false}")

#9. 運算符練習
a=10
b=3

#加法
sum=a+b
print(f"加法結果為:{sum}")

#減法
difference=a-b
print(f"減法結果為:{difference}")

#乘法
product=a*b
print(f"乘法結果為:{product}")

#除法
quotient=a/b
print(f"除法結果為:{quotient}")

#取餘數
remainder=a%b
print(f"取餘數結果為:{remainder}")

#10. 條件判斷練習
score=85

if score>=60:
    print("及格")
else:
    print("不及格")

#11. 迴圈練習
for i in range(1,11):
    print(i)

#12. 函數練習
def add(a,b):
    return a+b

print(f"1+2={add(1,2)}")

#13. 類別練習
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person=Person("小明",20)
person.say_hello()

#14. 檔案練習
with open("test.txt","w") as file:
    file.write("Hello, World!")

with open("test.txt","r") as file:
    content=file.read()
    print(f"讀取的內容為:{content}")

with open("Test0418.txt","w") as file:
    file.write("測試寫入文件")

with open("Test0418.txt","r") as file:
    content2=file.read()
    print(f"讀取的內容為:{content2}")

#15. 正則表達式練習
import re

text="Hello, World! 1234567890"

#尋找數字
numbers=re.findall(r"\d+",text)
print(f"尋找數字結果為:{numbers}")

#尋找字母
letters=re.findall(r"[a-zA-Z]+",text)
print(f"尋找字母結果為:{letters}")

#尋找空白字元
spaces=re.findall(r"\s+",text)
print(f"尋找空白字元結果為:{spaces}")

#尋找標點符號
punctuations=re.findall(r"[^\w\s]+",text)
print(f"尋找標點符號結果為:{punctuations}")

#尋找所有字元
all_chars=re.findall(r".",text)
print(f"尋找所有字元結果為:{all_chars}")

#16. 網路爬蟲練習
import requests

url="https://www.google.com"

response=requests.get(url)

print(f"網路爬蟲結果為:{response.text}")

#17. 資料庫練習
import sqlite3

conn=sqlite3.connect("test.db")

cursor=conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")

cursor.execute("INSERT INTO users (name, age) VALUES ('小明', 20)")

conn.commit()

cursor.execute("SELECT * FROM users")

rows=cursor.fetchall()

for row in rows:
    print(row)

conn.close()

#18. 網路爬蟲練習
# import requests
# from bs4 import BeautifulSoup4

# url="https://www.google.com"

# response=requests.get(url)

# soup=BeautifulSoup(response.text,"html.parser")

# print(f"網路爬蟲結果為:{soup}")

#while迴圈練習
count=0
while count<10:
    print(count)
    count+=1

#for迴圈練習
for i in range(1,11):
    print(i)

#if-else条件语句
score=input("請輸入成績:")
score=int(score)

if score>=60:
    print("及格")
else:
    print("不及格")

#if elif else条件语句
score=input("請輸入成績:")
score=int(score)

if score>=90:
    print("優秀")
elif score>=80:
    print("良好")
elif score>=70:
    print("中等")
else:
    print("不及格")
    
#break和continue语句
for i in range(1,11):
    if i==5:
        break
    print(i)
#continue语句練習
for i in range(1,11):
    if i==5:
        continue
    print(i)

#for迴圈練習

