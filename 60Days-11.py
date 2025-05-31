#python 中的例外處裡(erro handling,異常處理)

#exception

#try1:

# x=int(input("請輸入一個整數:"))
# y=int(input("請輸入另一個整數"))
# print(x/y)  #當y輸入0時會出錯 exception

#改用下列寫法

try:
    x=int(input("請輸入一個整數:"))
    y=int(input("請輸入另一個整數"))
    print(x/y)  #當y輸入0時會出錯 exception


# except ZeroDivisionError:
#     print("除數不能為零")

# except ValueError:
#     print("請輸入整數")

#增進
except (ValueError,ZeroDivisionError):
    print("出現錯誤，請重新輸入!")
else:
    print("無錯誤")


finally:  #不論正確或錯誤皆會接續執行
    print("無論是否正常皆會執行")

