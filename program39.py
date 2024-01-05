
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def CountRange(no):
    temp = 0
    flag = 0 
    
    if no < 0:
        no = -no
    
    while no != 0:
        temp = no%10
        no = no/10
        no = int(no)
        if temp <= 7 and temp >= 3:
            flag += 1
    
    if temp <= 7 and temp >= 3:
        flag += 1
        
    return flag
        
def main():
    print("Enter a number : ")
    num = int(input())
    
    result = CountRange(num)
    
    print("Frequency in between 3 and 7 is : ",result)
    
if __name__ == "__main__":
    main()