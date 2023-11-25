
# function accept parameter and return parameter
def marvellous(value1,value2):
    if(value1 > value2):
        return value1
    else:
        return value2

def main():
    ret = marvellous(75,44)
    print("largest value is: ",ret)
    ret = marvellous(51,99)
    print("largest value is: ",ret)
    
if __name__ == "__main__":
    main()