
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 



def divide(no1,no2):
    ans = 0
    
    if no2 == 0:
        return -1
    
    ans = no1 / no2
    return ans

def main():
    value1 = 15
    value2 = 5
    result = 0
    
    result = divide(value1,value2)
    
    print("division is : ",result)
    
if __name__ == "__main__":
    main()