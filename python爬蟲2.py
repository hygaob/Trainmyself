#引用BeautifulSoup

from bs4 import BeautifulSoup

import requests
content=requests.get("http://books.toscrape.com/").text
soup=BeautifulSoup(content,"html.parser")
#找價格
all_prices=soup.findAll("p",attrs={"class":"price_color"})
for price in all_prices:
    #print(price)
    print(price.string)
    print(price.string[2:])

#找書名
all_titles =soup.findAll("h3")
for title in all_titles:
    all_links=title.findAll("a")
    for link in all_links:
        print(link.string)

