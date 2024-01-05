
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def CheakZero(no):
    temp = 0
    if no < 0:
        no = -no
    
    flag = False
    
    while no != 0:
        temp = no%10
        no = no/10
        no = int(no)
        if temp == 0:
            flag = True
    if temp == 0:
        flag = True
        
    if flag == True:
        return True
    else:
        return False
        
def main():
    print("Enter a number : ")
    num = int(input())
    
    result = CheakZero(num)
    if result == True:
        print("It contains Zero")
    else:
        print("There is no zero")
    
if __name__ == "__main__":
    main()
