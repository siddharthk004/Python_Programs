
class demo:
    
    def __init__(self,value1,value2):   # constructor
        print("Inside init method")
        self.no1 = value1
        self.no2 = value2
        
    def display(self):
        print("value of no1",self.no1)
        print("value of no2",self.no2)

def Starter():
    print("demonstration of object orientation")
    
    obj1 = demo(10,20)
    obj2 = demo(11,21)
    
    obj1.display()
    obj2.display()
    

if __name__ == "__main__":
    Starter()