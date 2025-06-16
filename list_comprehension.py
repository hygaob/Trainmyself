#python 中的列表推導式(list_coomprehension)

#更少的語法推導列表的方法

#比lambda更精進

def square(x):
    return x**2
list=[]
for i in range(1,11):
    list.append(square(i))

print(list)

square2=[j*j for j in range(1,11)]
print("列表推導式")
print(square2) 

#ex 學生分數及格
grades=[100,90,66,80,46,29,88,40]
passed_grades=[g for g in grades if g>=60]
print(passed_grades)
no_passed_grades=[g for g in grades if g<60]
print(no_passed_grades)

#