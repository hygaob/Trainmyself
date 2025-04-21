# #函数定义与调用
# def greet(name):
#     print(f"Hello,{name}!")

# greet("Alice")

# #参数与返回值
# def add(a,b):
#     return a+b

# result=add(5,3)
# print(f"相加結果為:{result}")

# #lambda表达式
# square=lambda x:x*x
# print(square(4))
# specail_fun=lambda x,y:x**2*y**2
# print(specail_fun(2,3))

# #递归函数
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=int(input("請輸入一個數字:"))
# print(factorial(n))

# #高阶函数
# def apply_function(func,value):
#     return func(value)

# result=apply_function(lambda x:x*2,5)
# print(result)

# #闭包
# def outer_function(x):
#     def inner_function(y):
#         return x+y
#     return inner_function

# closure=outer_function(10)
# print(closure(5))

# # 1. 最基本的閉包示例
# def make_counter():
#     count = 0  # 外部變量
    
#     def counter():
#         nonlocal count  # 聲明非本地變量
#         count += 1
#         return count
    
#     return counter

# # 使用閉包
# counter = make_counter()
# print(counter())  # 輸出: 1
# print(counter())  # 輸出: 2
# print(counter())  # 輸出: 3
# print(counter())  # 輸出: 4

# #計算閏年
# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if 1900 <=year and year<=(10**5) :
#         if year % 4 == 0:
#             if year % 100 == 0:
#                 if year % 400==0:
#                     leap = True
#                 else:
#                     leap=False
#             else:
#                 leap = True
#         else:
#             leap=False
#     return leap

# year = int(input())
# print(is_leap(year))

# #輸入數字N，N介於1~9，根據輸入的數字
# def print_pattern(n):
#     if n>1 and n<10:
#         for i in range(1,n+1):
#             for j in range(1, i + 1):
#                 print(j, end='')
#             for j in range(i - 1, 0, -1):
#                 print(j, end='')
#             print()
#     else:
#         return False
# n= int(input("Enter a number:"))
# print_pattern(n)

# for i in range(1,int(input())):
#     print(i * (10**i)//9)

# from collections import defaultdict

# groupA = ['a', 'a', 'b', 'a', 'b']
# groupB = ['a', 'b', 'c']

# count_dict = defaultdict(int)
# for item in groupA:
#     count_dict[item] += 1

# for i in groupB:
#     print(count_dict[i] if count_dict[i] > 0 else '-1', end=' ')

# from collections import defaultdict

# d = defaultdict(list)
# n , m = map(int , input().split())
# for i in range(1 , n+1):
#     n_word = input()
#     d[n_word].append(i)
# for i in range(m):
#     m_word = input()
    
#     if m_word in d:
#         print(" ".join(map(str,d[m_word])))
#     else:
#         print(-1)

# from collections import defaultdict

# # 1. 基本示例
# # 創建一個默認值為 int 的 defaultdict
# d = defaultdict(int)
# # 訪問不存在的鍵時，會返回 int 的默認值 0
# print(d['不存在的鍵'])  # 輸出: 0
# d['a'] += 1
# print(d['a'])  # 輸出: 1

# # 2. 使用 list 作為默認值
# list_dict = defaultdict(list)
# # 可以直接對不存在的鍵追加元素
# list_dict['fruits'].append('蘋果')
# list_dict['fruits'].append('香蕉')
# print(list_dict['fruits'])  # 輸出: ['蘋果', '香蕉']

# # def word_count():
# words = ['蘋果', '香蕉', '蘋果', '橘子', '香蕉', '蘋果']
# counter = defaultdict(int)
    
# for word in words:
#     counter[word] += 1
    
# print(dict(counter))  # 輸出: {'蘋果': 3, '香蕉': 2, '橘子': 1}

# # 2. 分組
# def group_by_first_letter():
#     words = ['apple', 'ant', 'banana', 'cat', 'bear']
#     groups = defaultdict(list)
    
#     for word in words:
#         groups[word[0]].append(word)
    
#     print(dict(groups))  
#     # 輸出: {'a': ['apple', 'ant'], 'b': ['banana', 'bear'], 'c': ['cat']}
# print(group_by_first_letter())
# # 3. 嵌套字典
# def nested_dict():
#     nested = defaultdict(lambda: defaultdict(int))
#     nested['外層1']['內層1'] = 10
#     nested['外層1']['內層2'] = 20
#     print(dict(nested))
# print(nested_dict())

# # 1. int 類型（默認值為 0）
# int_dict = defaultdict(int)
# print(int_dict['新鍵'])  # 輸出: 0

# # 2. list 類型（默認值為空列表）
# list_dict = defaultdict(list)
# list_dict['新鍵'].append(1)
# print(list_dict['新鍵'])  # 輸出: [1]

# # 3. set 類型（默認值為空集合）
# set_dict = defaultdict(set)
# set_dict['新鍵'].add('元素')
# print(set_dict['新鍵'])  # 輸出: {'元素'}

# # 4. str 類型（默認值為空字符串）
# str_dict = defaultdict(str)
# print(str_dict['新鍵'])  # 輸出: ''

# # 5. 自定義默認值
# def custom_default():
#     return "自定義默認值"

# custom_dict = defaultdict(custom_default)
# print(custom_dict['新鍵'])  # 輸出: 自定義默認值
