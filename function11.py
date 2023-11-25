
def Add(A,B):
    return A+B

def sub(A,B):
    return A-B

def mult(A,B):
    return A*B

def div(A,B):
    return A/B

# function accept parameters as another function
def marvellous(FPTR1,FPTR2,FPTR3,FPTR4):
    print(type(FPTR1))
    print(type(FPTR2))
    print(type(FPTR3))
    print(type(FPTR4))
    ans = FPTR1(11,7)
    print("Addition is:",ans)
    
    ans = FPTR2(11,7)
    print("substraction is:",ans)
    
    ans = FPTR3(11,7)
    print("multiplication is:",ans)
    
    ans = FPTR4(11,7)
    print("division is:",ans)
    
def main():
    marvellous(Add,sub,mult,div)
    
    
if __name__ == "__main__":
    main()