
# function defines another function that is inside it
def marvellous(value1,value2):
    def add(A,B):
        return A+B
    
    ans  = add(value1,value2)
    return ans
    
def main():
    ret = marvellous(11,7)
    print(ret)
    
    
if __name__ == "__main__":
    main()