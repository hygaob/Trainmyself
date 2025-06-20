#Python Zip函式

#ZIP可把多個可迭代物件聚合起來

username=["Bob","Steven","Sam"]

password=("123","321","555")

dates=["1998-02-05","1995-10-10","1993-07-06"]

users=zip(username,password,dates)

print(users)

for i in users:
    print(i)

users_list=list(users)
print(users_list)

user_dict=dict(users)
print(users_list)  #key -> username

for key, value in user_dict.items():
    print(key+":"+value)