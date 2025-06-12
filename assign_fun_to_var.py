#Python 將函式指派給變數

#幾乎所有東西都可視為物件

def hello():  #定義方法
    print("hello")

hi=hello  #將hello指派給hi
print(hello)
print(hi)
#上兩者位置一樣

hi()

#同理，內建函式也可以指派給變數
say=print
say("hello")
say("hi")
