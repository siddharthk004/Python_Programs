
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def SchoolFees(no1):
    if no1 == 1:
        return 8900
    elif no1 == 2:
        return 12790
    elif no1 == 3:
        return 21000
    elif no1 == 4:
        return 23450
    else:
        print(" -- Invalid Class -- ")
        return 0
    
def main():
    
    print("Enter your class : ")
    num = int(input())      
    
    ret = SchoolFees(num)
    
    print("Your total amount is : ",ret)
    
if __name__ == "__main__":
    main()