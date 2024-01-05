
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def TouristBill(no1):
    if no1 <= 100:
        return no1*25
    elif no1 > 100:
        return no1*15
    
def main():
    
    print("Enter KM  : ")
    num = int(input())      
    
    ret = TouristBill(num)
    
    print("Your total amount is : ",ret)
    
if __name__ == "__main__":
    main()