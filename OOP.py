
class arithmatic:
    def __init__(self,a,b):
        print("inside constructor")
        self.no1 = a
        self.no2 = b
        
    def addition(self):
        ans = 0
        ans = self.no1+self.no2
        return ans
        
    def substraction(self):
        ans = 0
        ans = self.no1-self.no2
        return ans
        
def main():
    value1 = int(input("enter first number: ")) 
    value2 = int(input("enter second number: "))
    
    obj1 = arithmatic(value1,value2)
    ret = obj1.addition()
    print("addition is : ",ret)
    
    ret = obj1.substraction()
    print("substraction is : ",ret)
    
if __name__ == "__main__":
    main()
