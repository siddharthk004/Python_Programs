
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Pattern(no1,no2):
    for i in range(1,no1+1):
        for j in range(1,no2+1):
            print(" ",chr(64+i),end=" ")
        print()
            
def main():
    
    print("Enter Row  : ")
    row = int(input()) 
    
    print("Enter col  : ")
    col = int(input()) 
    
    Pattern(row,col)
    
if __name__ == "__main__":
    main()