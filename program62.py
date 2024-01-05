
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def IncomeTax(no1):
    if no1 <= 500000:
        return no1
    elif no1 > 500000 and no1 <= 1000000:
        return (no1*0.1)
    elif no1 > 1000000 and no1 <= 2000000:
        return (no1*0.2)
    elif no1 > 2000000:
        return (no1*0.3)
    
def main():
    
    print("Enter Bill Amount : ")
    num = int(input())      
    
    ret = IncomeTax(num)
    
    print("Your total amount is : ",ret)
    
if __name__ == "__main__":
    main()