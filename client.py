import marvellous 

def main():
    value1 = int(input("enter first number: "))
    value2 = int(input("enter second number: "))
    
    result = 0
    
    result = marvellous.Addition(value1,value2)
    print("Addition is: ",result)

    result = marvellous.division(value1,value2)
    print("division is: ",result)
    
    result = marvellous.Substraction(value1,value2)
    print("substraction is: ",result)
    
    result = marvellous.multiplication(value1,value2)
    print("multiplication is: ",result)

if __name__ == "__main__":
    main()