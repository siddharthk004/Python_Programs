
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 


def Pattern(no1):
    if no1 < 0:
        no1 = no1+no1
        
    for i in range(no1):
        print(" $  * ",end="")

def main():
    print("Enter a number : ")
    num = int(input())
    
    Pattern(num)

if __name__ == "__main__":
    main()