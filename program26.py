
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Multipledisplay(no1):
    sum = 0
    for i in range(5):
        sum = sum + no1
        print(" ",sum," ",end="")
    
def main():
    print("Enter a number : ")
    num = int(input())
    
    Multipledisplay(num)

if __name__ == "__main__":
    main()