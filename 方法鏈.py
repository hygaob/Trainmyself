#Python 中的方法鏈 Method Chaining

#cat.turn_on().drive().brake().turn_off()

class Car:
    def turn_on(self):
        print("啟動引擎")
        #回傳物件本身
        return self
    def drive(self):
        print("開車")
        return self
    def brake(self):
        print("你踩了煞車")
        return self
    def turn_off(self):
        print("熄火")
        return self
    
car_A=Car()
car_A.turn_on().turn_off().brake().drive()  #使用了return self 可以回傳物件本身使其串接方法
