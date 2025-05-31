#function 函數
#又稱方法

def say_hello():
    print("嗨世界")

say_hello()

#傳遞參數

def greeting(name):
    print(f"你好，{name}!")

greeting("阿財")

def add(x,y):
    return x+y

result=add(3,5)
print(result)

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def devide(x,y):
    return x/y

def create_name(first_name,last_name):
    first_name=first_name.capitalize()  #capitalize()首字大寫
    last_name=last_name.capitalize()
    return first_name+" "+last_name

print(create_name("john","wick"))

#函式的預設引數(default arguments)

def greet(name,greeting="Hello"):  #預設引數必須寫在後面
    print(f"{greeting},{name}")

greet("HY")
greet("John")

#Python 中的關鍵字參數 keyword arguments
#一般調用法
def hello(greeting,title,firstname,lastname):
    print(f"{greeting},{title},{firstname} {lastname}")

hello("你好!","Mr","Orange","高")
#Keyword調用法
hello(greeting="你好!",title="Mr",firstname="Orange",lastname="陳")
#如此做可以避免輸入值對照錯誤，強制對應keyword
#練習2
def get_phone(country_code,area_code,first,last):
    return f"+{country_code}-{area_code}-{first}-{last}"

strphone=get_phone(country_code="886",area_code="06",first="209",last="4350")
print(strphone)