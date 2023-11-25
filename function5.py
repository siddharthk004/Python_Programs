
# function accept multiple parameters and return multiple parameter
def marvellous(value1,value2):
    Addition = value1 + value2
    substraction = value1 - value2
    multiplication = value1 * value2
    division = value1 / value2
    
    return Addition,substraction,multiplication,division
    

def main():
    ret1,ret2,ret3,ret4 = marvellous(11,6)
    print("Addition is: ",ret1)
    print("substraction is: ",ret2)
    print("multiplication is: ",ret3)
    print("division is: ",ret4)   
    
    
if __name__ == "__main__":
    main()