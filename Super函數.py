#python中的Super函數

class Rectengle:     #方形
    def __init__(self, lenght,width):
        self.lenght=lenght
        self.width=width
        print("方形的初始化已執行")



class Square(Rectengle):    #正方形-->方形的一種
    def __init__(self, lenght, width):
        super().__init__(lenght, width)
        print("正方型的初始化已執行")
        print(f"正方形的長寬是{lenght},{width}")
        
Square_A=Square(500,500)

#立方體=長*寬*高
class Cude(Rectengle):
    def __init__(self, lenght, width, height):
        super().__init__(lenght, width)
        self.height=height  #高度並不含在方形中，需自行撰寫
        print(f"立方體的長寬高是{lenght},{width},{height}")

Cude_A=Cude(200,100,50)