#OOP - python中的繼承
#父類別<->子類別

#父-動物
class Animal:
    aLive=True

    def eat(self):
        print("這個動物在吃東西")
    def sleep(self):
        print("這個動物在睡覺")

#子-魚
class Fish(Animal):
    def swim(self):
        print("魚正在游泳")

#子-兔子
class Rabbit(Animal):
    def jump(self):
        print("兔子跳")

animal_A=Animal()
animal_A.eat()
animal_A.sleep()

rabbit_A=Rabbit()
rabbit_A.jump()
#animal_A.jump()  #父類別不能執行子類別
rabbit_A.eat()  #子類別可以執行父類別

#子-老鷹
class Hawk(Animal):
    def fly(self):
        print("老鷹正在飛")


fish_A=Fish()
fish_A.swim()
fish_A.eat()

hawk_A=Hawk()
hawk_A.fly()
hawk_A.eat()



