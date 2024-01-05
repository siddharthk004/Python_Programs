
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 


def CHKEqual(no1,no2):
    if no1 == no2:
        return True
    else:
        return False


def main():
    print("Please enter a first number : ")
    num1 = int(input())
    
    print("Please enter a second number : ")
    num2 = int(input())
    
    bret = CHKEqual(num1,num2)
    
    if bret == True:
        print(" Equal ")
    else:
        print(" Not Equal ")

if __name__ == "__main__":
    main()