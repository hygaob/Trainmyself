import selenium
import bs4
from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
import time
import csv

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome("./chromedriver",chrome_options=chrome_options)
driver.get("https://mbasic.facebook.com/groups/534081100134530/")

post=[]
soup=BeautifulSoup(driver.page_source,"lxml")
first=soup.find_all(class_="text_exposed_root")
for i in first:
    post.append(i.text)

timme=soup.find_all("abbr")
real=[]
for i in timme:
    if i.get("title")!=None:
        real.append(i.get("title"))

while real[-1].split(" ")[0]!="2022/2/28":
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    post=[]
    soup=BeautifulSoup(driver.page_source,"lxml")
    first=soup.find_all(class_="text_exposed_root")
    for i in first:
        post.append(i.text)

    timme=soup.find_all("abbr")
    real=[]
    for i in timme:
        if i.get("title")!=None:
            real.append(i.get("title"))
    print(real[-1].split(" ")[0])


print(len(post))

driver.close() 