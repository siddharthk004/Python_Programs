
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def CalculateBill(no1):
    if no1 <= 500 :
        return no1
    elif no1 > 500 and no1 <= 1500:
        return no1 - (no1*0.1)
    elif no1 > 1500:
        return no1 - (no1*0.15)
    
def main():
    
    print("Enter Bill Amount : ")
    num = int(input())      
    
    ret = CalculateBill(num)
    
    print("Your total amount is : ",ret)
    
if __name__ == "__main__":
    main()