import yfinance as yf
import pandas as pd

# 獲取微軟股票的歷史數據
msft = yf.Ticker("TSM")
hist = msft.history(period="max")

# 計算微軟股票的布林通道
sma20 = hist["Close"].rolling(window=20).mean()
std20 = hist["Close"].rolling(window=20).std()
upper_band = sma20 + 2 * std20
lower_band = sma20 - 2 * std20

balance_history = {}

# 計算策略的報酬率
balance = 100000  # 初始資金
stock = 0  # 持有股票數量
for i in range(len(hist)):
    if hist["Close"].iloc[i] > upper_band.iloc[i] and stock == 0:
        # 買入股票
        stock = balance // hist["Close"].iloc[i]
        balance -= stock * hist["Close"].iloc[i]
    elif hist["Close"].iloc[i] < lower_band.iloc[i] and stock > 0:
        # 賣出股票
        balance += stock * hist["Close"].iloc[i]
        stock = 0
    
    balance_history[hist.index[i]] = (balance + stock * hist['Close'].iloc[i])

# 計算最終的報酬率
final_value = balance + stock * hist["Close"].iloc[-1]
return_rate = (final_value - 100000) / 100000
print("最終報酬率：%.2f%%" % (return_rate * 100))