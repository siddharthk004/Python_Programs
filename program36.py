
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Count(no):
    temp = 0
    flag = 0 
    
    if no < 0:
        no = -no
    
    while no != 0:
        temp = no%10
        no = no/10
        no = int(no)
        if temp <= 6:
            flag += 1
        
    return flag
        
def main():
    print("Enter a number : ")
    num = int(input())
    
    result = Count(num)
    
    print("Frequency of less than 6 is : ",result)
    
if __name__ == "__main__":
    main()