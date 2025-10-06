# 輸入年份判斷是不是閏年。

year= int(input("請輸入年份:"))
is_leap=(year%4==0 and year%100!=0) or (year%400==0)
if is_leap:
    print(f"{year}是閏年")
else:
    print(f"{year}不是閏年")