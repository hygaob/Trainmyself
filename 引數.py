#python物件當成引數

class Car:    #建立一個類別
    color=None

def change_color(car,color):  #建立一個方法  引數類別
        car.color=color

Car1=Car()
Car2=Car()
Car3=Car()

print(Car1.color)
print(Car2.color)
print(Car3.color)

change_color(Car1,"Red")
change_color(Car2,"blue")
change_color(Car3,"black")

print("Car1's color is",Car1.color)
print("Car2's color is",Car2.color)
print("Car3's color is",Car3.color)

#建立好的物件欲修改，可用引數方式修改物件