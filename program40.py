
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def MultDigit(no):
    temp = 0
    mult = 1
    
    if no < 0:
        no = -no
    
    while no != 0:
        temp = no%10
        no = no/10
        no = int(no)
        if temp != 0:
            mult = mult*temp
        
    return mult
        
def main():
    print("Enter a number : ")
    num = int(input())
    
    result = MultDigit(num)
    
    print("multiplication is : ",result)
    
if __name__ == "__main__":
    main()