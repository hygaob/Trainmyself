# https://medium.com/@starfish_go/python-ch01-3-%E7%B7%B4%E7%BF%92%E9%A1%8C-53e3dbe42710
# (1) 請算出 (1+2)*(3²)+5 的值
ans=(1+2)*(3**2)+5
print(ans)

# (2) 請問 4+6.5 的資料類型是什麼? (可用type檢查)
print(type(4+6.5))
# (3) 用 input() 讀入一個數值儲存在變數 a 中，最後用 print 指令印出 ''我的v幸運數字是▯''。
# a=input("a=")

# print(f"我的幸運數字是{a}")
# (4) 將 ''Python'' 的每個字元都取出來。
for ch in "Python":
    print(ch)
# (5) 將 ''I love python'' 裡的三個字取出來。
str="I love python"
word1=str[str.find(" ")-1]
print(word1)
#print(str.find(" "))
word2=str[(str.find(" ")+1):(str.find(" ",str.find(" ")+1)+1)]
print(word2)
word3=str[(str.find(" ",str.find(" ")+1)+1):]
print(word3)
# (6) 利用迴圈 印出l love you so so so … much. so要重複100次！
print("I love you",end=" ")
for so in range(1,100,1):
    print("so",end=" ")
print("much.")
# (7) 請將 123.456789 用 f_string 輸出成小數點後3位。
k=123.456789
print(f"{k:.3f}")
# (8) 請將 0.25 用 f_string 表示成 25%。
j=0.25
print(f"{j:.0%}")
# (9) 假設 score 是小明每次考試的成績，score=[‘小明’=68,72,84,96,88]，請
# 計算成績的最大、最小以及平均值，並從小到大排序成績
score_old=[68,72,84,96,88]
# score_new=[]
# for score in score_old:
#     score_new[score]
score_new=sorted(score_old)
print(score_new)
print(max(score_new))
print(min(score_new))
avg_score=sum(score_new)/len(score_new)
print(avg_score)
