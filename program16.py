
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 



def FactDiff(no1):
    sum1 = 0
    sum2 = 0
    
    for i in range(1,no1):
        if no1 % i == 0:
            sum1 = sum1 + i
        else:
            sum2 = sum2 + i
    return sum1-sum2

def main():
    print("Enter a number : ")
    num = int(input())
    
    result = FactDiff(num)
    
    print("difference of non factor and factor summation is : ",result)

if __name__ == "__main__":
    main()
