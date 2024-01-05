
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Factorial(no):
    sum = 1
    for i in range(no,1,-1):
        sum = sum * i
    return sum
    
def main():
    print("Enter a number : ")
    num = int(input())
    
    result = Factorial(num)
    
    print("Factorial of number is : ",result)

if __name__ == "__main__":
    main()