from functools import reduce
def main():
    data = []
    print("enter the value you want to store: ")
    no = int(input())
    
    print("Enter value : ");
    for i in range(no):
        value = int(input())
        data.append(value)
        
    print("input data",data)
    output = list(filter(lambda no : (no % 2 == 0),data))
    print("output after filter : ",output)
     
    output1 = list(map(lambda no : no + 2,output))
    print("output after map : ",output1) 
    
    output2 = reduce(lambda a,b : a+b,output1)
    print("output after reduce : ",output2)  
    
if __name__ == "__main__":
    main()