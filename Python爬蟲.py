#爬蟲練習
#請求頻率不宜太高
#了解/robot.txt爬蟲規則

#發送http請求:Hypertext Transfer Protocol
#HTTP請求方式: 
#GET 獲取
#POST 創建

#標準HTTP請求
#   請求行
#   請求頭
#   請求體

#Requests庫
import requests
response = requests.get("http://books.toscrape.com/")  
#範例網站 http://books.toscrape.com/
print(response)
print(response.status_code)

if response.ok:
    print(response.text)
else:
    print("請求失敗")


#模仿瀏覽
import requests
  
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}  #模仿瀏覽器
response = requests.get("https://movie.douban.com/top250",headers=headers)
if response.ok:
    print(response.text)
else:
    print("請求失敗"+ str(response))

#網頁有三大結構要素
#HTML:定義網頁結構和信息
#CSS:定義網頁樣式
#JavaScript:定義用戶和網頁的交互邏輯

#主要是抓取HTML來蒐集數據
#經典HTML架構
# <!DOCTYPE HTML>   >>告知瀏覽器此網頁是以html為樣式
# <html>            >>起始標籤
#   <body>
#         <h1>這是標題</h1>
#         <p>這是一段文字<p>
#   </body>
# </html>           >>結束標籤
#如果樣式要好看要搭配CSS

#標題
# <h1>一級標籤</h1>
# <h2>二級標籤</h2>
# <h3>三級標籤</h3>...

# <hN>N級標籤</hN>

#內文
# <p>這是內文內容</p>
# <p>會自動換行</p>
# <p>同段強制<br>換行</p>
# <p>字體<b>加粗</b>範例</p>

# 圖片
# <img src="圖片網址"
#     width="圖片寬度px"
#     height="圖片高度px">

#超連結
# <a herf="網址">超連結文字</a>
# <a herf="網址" target="_self">超連結文字</a> 在當前瀏覽器頁面跳轉
# <a herf="網址" target="_blank">超連結文字</a> 在瀏覽器新頁面跳轉

