
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 



def nonFact(no1):
    sum = 0
    for i in range(1,no1):
        if no1 % i == 0:
            pass
        else:
            sum = sum + i
    return sum

def main():
    print("Enter a number : ")
    num = int(input())
    
    result = nonFact(num)
    
    print("Summation of non factor is : ",result)

if __name__ == "__main__":
    main()
