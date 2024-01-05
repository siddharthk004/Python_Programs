
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 


def display(no1):
    for i in range(no1,0,-1):
        print(" -",i," ",end="")
    
    for i in range(0,no1+1):
        print(" ",i," ",end="")

def main():
    print("Enter a number : ")
    num = int(input())
    
    display(num)

if __name__ == "__main__":
    main()