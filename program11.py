
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 



def cheakevenodd(no1):
    if no1 % 2 == 0:
        return True
    else:
        return False

def main():
    
    print("Enter a number : ")
    num = int(input())
    
    value = cheakevenodd(num)
    
    if value == True:
        print(" Even number ")
    else:
        print(" Odd number ")
    
if __name__ == "__main__":
    main()
