class Rectangle:
    
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid



    def area(self):
        recArea = self.len * self.wid  
        return recArea
    

rectangle1 = Rectangle(10, 5)

recArea1 = rectangle1.area()

print(recArea1)
        


    
        