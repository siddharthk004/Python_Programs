
# function defines another function that is inside it 
# and return as its return value

def marvellous():        # 0x100
    def add(A,B):        # 0x200
        return A+B
    
    return add           # return 0x200
    
def main():              # 0x300
    ans = marvellous()   # 0x100()
    ret = ans(10,7)      # 0x200(10,7)
    print("addition is : ",ret)
    
    
if __name__ == "__main__":
    main()               # 0x300()