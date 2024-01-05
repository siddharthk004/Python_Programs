
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def CountEven(no):
    temp = 0
    flag = 0 
    
    if no < 0:
        no = -no
    
    while no != 0:
        temp = no%10
        no = no/10
        no = int(no)
        if temp % 2 == 0:
            flag += 1
        
    return flag
        
def main():
    print("Enter a number : ")
    num = int(input())
    
    result = CountEven(num)
    
    print("Frequency of Even number is : ",result)
    
if __name__ == "__main__":
    main()
    