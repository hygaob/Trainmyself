#Duck Typing
#此為一概念，指的是一個物件所屬的類別，不如他所屬的方法和類別重要

class Duck:
    def walk(self):
        print("鴨子在走路")

    def talk(self):
        print("鴨子在呱呱呱")

class Chicken:
    def walk(self):
        print("雞在走路")

    def talk(self):
        print("雞在咕咕叫")

#上述兩個類別都有同樣功能
#兩個類別，同樣功能，即使沒有繼承關係，也可以當成同一個類別使用

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()

Duck_a=Duck()
Chicken_a=Chicken()
person_a=Person()
person_a.catch(Duck_a)
person_a.catch(Chicken_a)