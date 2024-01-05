
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def pattern(num1,num2):
    for i in range(num1):
        for j in range(num2-1,-1,-1):
            if i == j:
                print(" #",end=" ")
            else:
                print(" *",end=" ")
        print()
    
def main():
    
    print("Enter row : ")
    number = int(input())
    print("Enter col : ")
    col = int(input())
    
    pattern(number,col)
    
if __name__ == "__main__":
    main()