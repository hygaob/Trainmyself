#python 中的類別變數

class Car:
    
    wheels=4

    def __init__(self,make,model,year,color):  #初始化
        #屬性
        self.make=make  #廠牌
        self.model=model #型號
        self.year=year #年分
        self.color=color #顏色

    def drive(self):
        print(self.model+"正在行駛")
    
    def stop(self):
        print(self.model+"已經停止")


car1=Car("Toyota","Altis",2021,"blue")
car2=Car("Ford","focus",2023,"white")

print(f"汽車{car1.model}有{car1.wheels}個輪子")

car2=Car("三陽","競戰",2020,"black")
print(f"機車{car2.model}有{car2.wheels}個輪子")
#此時直接變數修改
car2.wheels=2
print(f"機車{car2.model}有{car2.wheels}個輪子")