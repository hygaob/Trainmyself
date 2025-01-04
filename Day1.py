# #練習-預測大學學費
# tuition = 50000
# year = 0
# while tuition < 60000:
#     tuition = tuition * 1.05
#     year += 1
# print("In", year, "years, the tuition will be over $60,000")
# #Ex 使用while 刪除串列內apple字串
# fruits = ["apple", "banana", "cherry","apple","apple","grauva"]
# fruit= "apple"
# while fruit in fruits:
#     fruits.remove(fruit)
# print(fruits)
# #Ex 有一個串列buyer 此串列內有購買者的名字和消費金額，如果消費金額大於1000，則歸類為VIP買家，否則為gold買家
# #請用while迴圈將串列中的資料分類
# buyers = [["John", 1000], ["David", 500], ["Paul", 2000], ["Tom", 700]]
# goldbuyers=[]
# vipbuyers=[]
# while buyers:
#     buyer = buyers.pop()
#     if buyer[1] > 1000:
#         vipbuyers.append(buyer)
#     else:
#         goldbuyers.append(buyer)
# print("VIP Buyers:", vipbuyers)
# print("Gold Buyers:", goldbuyers)
# #ex enumerate()函數
# drinks = ["coffee", "tea", "wine"]
# for drink in enumerate(drinks):
#     print(drink)
# for count, drink in enumerate(drinks):
#     print(count, drink)
# print("**************************")
# for drink in enumerate(drinks, 10):
#     print(drink)
# for count, drink in enumerate(drinks, 10):
#     print(count, drink)
# #ex 計算得分前十的數據
# scores=[60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
# index = 1
# for score in scores:
#     if score >= 100:
#         print("The top 10 scores are:", index, score)
#         index += 1
# print("*************方法2*************")
# for count, score in enumerate(scores, 1):
#     if score >= 100:
#         print("The top 10 scores are:", count, score)
# #ex 設計購物車系統
# store = "7-11"
# products = ["電視", "冰箱", "洗衣機", "冷氣", "電風扇"]
# cart=[]
# print("Welcome to", store)  
# print(products,"\n")
# while True:
#     product = input("請輸入要購買的商品(按q離開):")
#     if product == "q":
#         break
#     elif product in products:
#         cart.append(product)
#         print(cart)
#     else:
#         print("此商店無販售此商品")
#Ex 設計真實的成績系統排序
#姓名, 國文, 英文, 數學, 總分, 平均, 排名
# sc=[[1,"John", 90, 80, 88, 0, 0, 0], 
#     [2,"David", 80, 87, 95, 0, 0, 0], 
#     [3,"Paul", 70, 65, 99, 0, 0, 0], 
#     [4,"Tom", 60, 75, 89, 0, 0, 0], 
#     [5,"Bob", 50, 60, 70, 0, 0, 0]]
# #計算總分與平均
# print("原始成績單",sc)
# print("計算總分與平均")
# for i in range(len(sc)):
#     sc[i][5] = sum(sc[i][2:5])
#     sc[i][6] = round((sc[i][5] / 3), 1)
#     print(sc[i])
# sc.sort(key=lambda x:x[5], reverse=True)
# print("依總分排序",sc)
# print("計算排名")
# for i in range(len(sc)):
#     sc[i][7] = i + 1
#     print(sc[i])
# print("依座位排序")
# sc.sort(key=lambda x:x[0])
# print("座位排序後成績單")
# for i in range(len(sc)):
#     print(sc[i])
# #ex 計算圓周率
# #萊布尼茲公式
# #pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...+4*(-1)**(n+1) /(2n+1)=sum(4(-1**(n+1)/(2n-1))))
# n=1000001
# pi=0
# for i in range(1,n+1):
#     pi += 4*((-1)**(i+1)/(2*i-1))
#     if i !=1 and i % 100000 == 0:
#         print("第",i,"次計算結果:",pi)  #每隔100000顯示一次結果

# #有一串列內部元素是一系列圖檔，依照檔案類型分類jpg, png, gif
# picturefiles=["dog.jpg", "cat.png", "bird.gif", "fish.jpg", "elephant.png", "tiger.gif"]
# jpgfiles=[]
# pngfiles=[]
# giffiles=[]
# for picturefile in picturefiles:
#     if picturefile.endswith("jpg"):
#         jpgfiles.append(picturefile)
#     elif picturefile.endswith("png"):
#         pngfiles.append(picturefile)
#     elif picturefile.endswith("gif"):
#         giffiles.append(picturefile)
# print("JPG Files:", jpgfiles)
# print("PNG Files:", pngfiles)
# print("GIF Files:", giffiles)  

# #有一球員資料串列，包含球員姓名及身高，請依照身高排序
# players=[["John", 180], ["David", 175], ["Paul", 190], ["Tom", 185], ["Bob", 170]]
# players.sort(key=lambda x:x[1], reverse=True)
# print("依照身高排序",players)
# #請將超過(含)180公分球員列出
# for player in players:
#     if player[1] >= 180:
#         print(player)
# # #本金利率計算程式
# # money=int(input("請輸入本金:"))
# # rate=float(input("請輸入利率:"))
# # years=int(input("請輸入年數:"))
# # for i in range(1, years):
# #     money = money * (1+rate)
# #     print("第", i, "年本金和:", round(money, 2))
# #假設今年是50公斤，每年增加1.3公斤，請計算10年後的體重
# weight=50
# for i in range(1, 11):
#     weight  += 1.3
#     print("第", i, "年體重:", round(weight, 2))
# #輸入n,m，m必大於n，請計算n到m的總和
# while True:
#     n=int(input("請輸入n:"))
#     m=int(input("請輸入m:"))
#     if m > n:
#         break
#     else:
#         print("m必須大於n")
# total_sum=sum(range(n, m+1))
# print(f"{n}到{m}總和: {total_sum}")
# #編寫數字1-5之間的，2個數字的各種組合
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i, j)
#ex 計算數學常數e
#e=sum(1/i!)
# e=0
# i=100
# stages=1
# for n in range(0, i+1):
#     if n == 0:
#         stages=1
#     else:
#         stages=stages*n
#     e+=1/stages
#     if n % 10 == 0: print("第", n, "次計算結果:", e)
# print("e=", e)
# # 列印9*9乘法表
# title="九九乘法表"
# print(title.center(70, "="))
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i}x{j}={i*j}", end="\t")
#     print()
# #列出前20個質數，然後放在串列並列印
# primes=[]
# count=0
# n=2
# while count < 20:
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         primes.append(n)
#         count += 1
#     n += 1
# print("前20個質數:", primes)
#輸入兩個數，這個程式會找出兩者間最大公約數
a=int(input("請輸入第一個數:"))
b=int(input("請輸入第二個數:"))
#法1
# while b != 0:
#     a, b = b, a % b
# print("最大公約數:", a)
#法2
max_num = 0
for i in range(1, a+1):
    for j in range(1, b+1):
        if a % i == 0 and b % j == 0 and i == j:
            print("公約數:", i)
            max_num = i
            break
print("最大公約數:", max_num)
#有一個水果串列，請列出加上編號
fruits=["apple", "banana", "cherry", "grape", "orange"]
num_fruits=[]
for index, fruit in enumerate(fruits, 1):
    print(index, fruit)
    num_fruits.append((index, fruit))
print(num_fruits)