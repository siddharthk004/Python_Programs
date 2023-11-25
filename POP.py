
def addition(no1,no2):
    ans = 0
    ans = no1 + no2
    return ans

def substraction(no1,no2):
    ans = 0
    ans = no1 - no2
    return ans

def main():
    value1 = int(input("enter first number: ")) 
    value2 = int(input("enter second number: "))
    
    ret = addition(value1,value2)
    print("addition is : ",ret)
    
    ret = substraction(value1,value2)
    print("substraction is : ",ret)
    
    
    
if __name__ == "__main__":
    main()
