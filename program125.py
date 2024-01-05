
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def pattern(num1,num2):
    for i in range(1,num1):
        for j in range(1,num2):
            if i == j or i == 1 or j == 1 or i == num1-1 or j == num2-1:
                print(j,end=" ")
            else:
                print(" ",end=" ")
        print()
    
def main():
    
    print("Enter row : ")
    number = int(input())
    print("Enter col : ")
    col = int(input())
    
    pattern(number,col)
    
if __name__ == "__main__":
    main()