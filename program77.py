
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Pattern(no1,no2):
    for i in range(1,no1+1):
        for j in range(1,no2+1):
            if i%2 != 0:
                print(" ",chr(64+j),end=" ")
            else:
                print(" ",chr(96+j),end=" ")
        print()
            
def main():
    
    print("Enter Row  : ")
    row = int(input()) 
    
    print("Enter col  : ")
    col = int(input()) 
    
    Pattern(row,col)
    
if __name__ == "__main__":
    main()