
def Add(A,B):
    return A+B

def sub(A,B):
    return A-B

def mult(A,B):
    return A*B

def div(A,B):
    return A/B

# function accept parameters and call another function from it and return multiple value in it
def marvellous(value1,value2):
    ret1 = Add(value1,value2)
    ret2 = sub(value1,value2)
    ret3 = mult(value1,value2)
    ret4 = div(value1,value2)
    
    return ret1,ret2,ret3,ret4

def main():
    ans = marvellous(11,7)
    print(ans[0])
    print(ans[1])
    print(ans[2])
    print(ans[3])
    
    
if __name__ == "__main__":
    main()