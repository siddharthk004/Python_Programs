
from functools import reduce

def CheakEven(no):
    if(no % 2 == 0):
        return True
    else:
        return False
    
def Increase(no):
    return no + 2

def Add(a,b):
    return a+b    

def main():
    data = []
    print("enter the value you want to store: ")
    no = int(input())
    
    print("Enter value : ");
    for i in range(no):
        value = int(input())
        data.append(value)
        
    print(data)
    output = list(filter(CheakEven,data))
    print(output)
     
    output1 = list(map(Increase,output))
    print(output1) 
    
    output2 = 0
    output2 = reduce(Add,output1)
    print(output2)  
    
if __name__ == "__main__":
    main()