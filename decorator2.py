
# inbult function (we cannot modify the contents)
def sub(A,B):
    return A-B

#decorator
def SmartSub(FPTR):
    def Inner(A,B):
        if(A<B):
            A,B = B,A
        return FPTR(A,B)
    return Inner

def main():
    subX = SmartSub(sub)
    
    ret = subX(10,7)
    print("substraction is : ",ret)
    
    ret = subX(7,10)
    print("substraction is : ",ret)

if __name__ == "__main__":
    main()