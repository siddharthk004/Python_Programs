
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Pattern(no1):
    for i in range(no1,0,-1):
        print(i," # ",end="")
    
def main():
    
    print("Enter length  : ")
    num = int(input()) 
    
    Pattern(num)
    
if __name__ == "__main__":
    main()