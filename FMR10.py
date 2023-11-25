CheakEven = lambda no : (no % 2 == 0)    
Increase =lambda no: no + 2
Add = lambda a,b:a+b    

# task = name of function
#elements = list of data elements

def filterX(Task,Elements):
    Result = []
    for no in Elements:
        if(Task(no) == True):
            Result.append(no)
    return Result

def mapX(Task,Elements):
    Result = []
    for no in Elements:
        ret = Task(no)
        Result.append(ret)
    return Result

def ReduceX(Task,Elements):
    Result = 0
    for no in Elements:
        Result = Task(Result,no)
    return Result

def main():
    data = []
    print("enter the value you want to store: ")
    no = int(input())
    
    print("Enter value : ");
    for i in range(no):
        value = int(input())
        data.append(value)
        
    print("input data",data)
    output = list(filterX(CheakEven,data))
    print("output after filter : ",output)
     
    output1 = list(mapX(Increase,output))
    print("output after map : ",output1) 
    
    output2 = ReduceX(Add,output1)
    print("output after reduce : ",output2)  
    
if __name__ == "__main__":
    main()