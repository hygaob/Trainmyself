principal = 5000000
annual_loan_rate = 0.0099
annual_invest_rate = 0.20
loan_years = 7
invest_years=10
#months = years * 
loan_months = loan_years * 12
invest_months = invest_years * 12

monthly_loan_rate = annual_loan_rate / 12
monthly_invest_rate = annual_invest_rate / 12

# 計算每月還款金額（等額本息公式）
A = principal * (monthly_loan_rate * (1 + monthly_loan_rate) ** loan_months) / ((1 + monthly_loan_rate) ** loan_months - 1)

investment = principal-1800000
profits = []

for m in range(1, invest_months + 1):
    investment *= (1 + monthly_invest_rate)  # 投資複利成長
    if m <= loan_months:
        investment -= A                         # 扣除每月還款
    profits.append(investment)

# 列印每月獲利
for idx, profit in enumerate(profits, 1):
    print(f"第{idx}月，投資帳戶餘額：{round(profit, 2)}")
print(f"\n{invest_years}年後總獲利：{round(profits[-1], 2)}")
print(f"月繳金額為:{round(A, 2)}")