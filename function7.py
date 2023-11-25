
def Add(A,B):
    return A+B

def sub(A,B):
    return A-B

def mult(A,B):
    return A*B

def div(A,B):
    return A/B

# function accept parameters and call another function from it
def marvellous(value1,value2):
    ret = Add(value1,value2)
    print(ret)
    
    ret = sub(value1,value2)
    print(ret)
    
    ret = mult(value1,value2)
    print(ret)
    
    ret = div(value1,value2)
    print(ret)
    
def main():
    marvellous(11,7)
    
if __name__ == "__main__":
    main()