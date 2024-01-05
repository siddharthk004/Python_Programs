
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Pattern(no1,no2):
    num = 0
    for i in range(no1):
        for j in range(no2):
            
            if i % 2 == 0:
                num += 2
                print(" ",num,end=" ")
            else:
                num += 1
                print(" ",num,end=" ")

        num = 0
        print()
            
def main():
    
    print("Enter Row  : ")
    row = int(input()) 
    
    print("Enter col  : ")
    col = int(input()) 
    
    Pattern(row,col)
    
if __name__ == "__main__":
    main()