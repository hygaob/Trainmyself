# 練習1 - 尋找水仙花數 (Narcissistic number)。
# 水仙花數是指一個 3 位數，它的每個位上的數字的3次方和等於它本身（例如：1^3 + 5^3+ 3^3 = 153）。

def is_narcissistic_number(num):
    sum = 0
    for digit in str(num):   #將數字轉成字串後逐位取出
        sum += int(digit) ** 3   #判斷每位數字的3次方和
    return sum == num   #回傳是否等於原數字的布林值
for num in range(100, 2000):
    if is_narcissistic_number(num):
            print(f"{num} 是水仙花數")


# 練習2 - 尋找完美數 (Perfect number)。
# 完美數是指它的所有的真因子（除了自身以外的因數）和等於它本身（例如：1、2、3、6，除去它本身 6 外，1 + 2 + 3 = 6）
def is_perfect_number(num):
    sum = 0
    for i in range(1, num):  #尋找所有真因子
        if num % i == 0:
            sum += i   #計算真因子和
    return sum == num   #回傳是否等於原數字的布林值
for num in range(1, 1000):
    if is_perfect_number(num):
        print(f"{num} 是完美數")

# 練習3 - 百錢百雞問。

# 雞公一隻價值五元，雞母一隻價值三元，小雞三隻價值一元。
# 百元買百雞，問雞公、雞母、小雞各幾隻(每種雞至少買一隻)？
#雞公最多買20隻，雞母最多買33隻
for rooster in range(1,21):  # 雞公數量範圍
    for hen in range(1,34):  # 雞母數量範圍
        chick = 100 - rooster - hen  # 小雞數量
        if (5 * rooster + 3 * hen + chick / 3) == 100:  # 價格計算
            print(f"雞公: {rooster}隻, 雞母: {hen}隻, 小雞: {chick}隻")

# 練習4 - 斐波那契數列 (Fibonacci sequence)。
# 斐波那契數列是指這樣一個數列
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765........
# 如果設 F(n) 為該數列的第 n 項（n∈N*)，
# 那麼這句話可以寫成如下形式：F(n) = F(n-1) + F(n-2)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
for i in range(1, 21):
    print(f"{fibonacci(i)}", end=", ")
