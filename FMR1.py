from functools import reduce

def CheakEven(no):
    if(no % 2 == 0):
        return True
    else:
        return False
    
def Increase(no):
    return no + 2

def Add(a,b):
    a+b    

def main():
    data = [5,4,9,8,13,17,12,18]
    print(data)
    output = list(filter(CheakEven,data))
    print(output)
     
    output1 = list(map(Increase,output))
    print(output1) 
    
    output2 = 0
    output2 = reduce(Add,output1,output2)
    print(output2)  
    
if __name__ == "__main__":
    main()