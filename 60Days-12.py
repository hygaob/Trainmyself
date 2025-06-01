#使用python進行檔案偵測

#OS標準庫

import os

#C:\Users\Fish\桌面\workspace\

#str = "C:\Users\Fish\桌面\workspace\"  
#=>  \ 無法顯示 要改r   計算機基本規則
str = r"C:\Users\Fish\桌面\workspace"
print(str)

if os.path.exists(str):
    print(f"路徑存在!")
else:
    print(f"路徑不存在!")

if os.path.isfile(str):
    print(f"該路徑為檔案!")
elif os.path.isdir(str):
    print(f"路徑為目錄!")
else:
    print(f"該路徑為其他類型!")

#讀取檔案

str_text=r"C:\Users\Fish\桌面\workspace\test.txt"

try:  #加入異常處理
    with open(str_text) as file:
        print(file.read())

except FileNotFoundError:
    print("檔案不存在!")

#寫入檔案  此模式會直接覆蓋，如果原始路徑有存在，則內容會直接被蓋過

str_path=r"C:\Users\Fish\桌面\workspace\test2.txt"

text="Hi write a file test\n sec row"
try:
    with open(str_path,"w") as file:
        file.write(text)
        print("寫入完成")
except FileNotFoundError:
    print("路徑不存在!")

try:  #加入異常處理
    with open(str_path) as file:
        print(file.read())

except FileNotFoundError:
    print("檔案不存在!")


#插入模式  此模式是在原本的狀態下面新增
text_in="\ngo go"
try:
    with open(str_path,"a") as file:
        file.write(text_in)
        print("插入完成")
except FileNotFoundError:
    print("路徑不存在!")

try:  #加入異常處理
    with open(str_path) as file:
        print(file.read())

except FileNotFoundError:
    print("檔案不存在!")