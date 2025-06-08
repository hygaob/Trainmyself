#物件導向OOP
#創建物件
#物件(object)是類別(class)的實例(instance)
#透過程式，模擬現實中的物體
#car(物件) 4個輪子(屬性) car按喇叭(方式)
#car.bow()
#車=>類別class
#每台生產出的車=>物件object

class Car:
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

print(car1.make)
print(car1.make,car1.model,car1.year,car1.color)
print(car2.make)

car1.drive()
car2.stop()





