
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 



def multFact(no1):
    sum = 1
    for i in range(1,no1):
        if no1 % i == 0:
            sum = sum*i
    return sum        

def main():
    
    print("Enter a number : ")
    num = int(input())
    
    value = multFact(num)
    
    print("multiplication is : ",value)
    
if __name__ == "__main__":
    main()
