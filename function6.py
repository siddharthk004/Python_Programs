
# function accept multiple parameters and return multiple parameter
def marvellous(value1,value2):
    Addition = value1 + value2
    substraction = value1 - value2
    multiplication = value1 * value2
    division = value1 / value2
    
    return Addition,substraction,multiplication,division
    

def main():
    ret = marvellous(11,6)
    print("Addition is: ",ret[0])
    print("substraction is: ",ret[1])
    print("multiplication is: ",ret[2])
    print("division is: ",ret[3])   
    
    
if __name__ == "__main__":
    main()