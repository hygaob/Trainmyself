#python中的方法重寫(Method overrriding)

class Animal:
    def eat(self):  #父類別先定義方法
        print("動物正在吃東西")

class Rabbiit(Animal):
    def eat(self):    #子類別可以重寫方法
        print("兔子正在吃紅蘿蔔")

animal_A=Animal()
animal_A.eat()
rabbit_A=Rabbiit()
rabbit_A.eat()

#哺乳類Mammal
class Mammal(Animal):
    def hi(self):
        print("我是哺乳類")
    pass
#貓Cat
class Cat(Mammal):
    def eat(self):
        print("貓正在吃魚")
#狗Dog
class Dog(Mammal):
    def eat(self):
        print("小狗正在啃骨頭")

cat_A=Cat()
cat_A.eat()
cat_A.hi()
dog_A=Dog()
dog_A.eat()