
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Pattern(no1,no2):

    for i in range(1,no1+1):
        for j in range(no2,0,-1):
            if j >= i:
                print(" * ",end=" ")
            else:
                print(" # ",end=" ")

        print()
            
def main():
    
    print("Enter Row  : ")
    row = int(input()) 
    
    print("Enter col  : ")
    col = int(input()) 
    
    Pattern(row,col)
    
if __name__ == "__main__":
    main()