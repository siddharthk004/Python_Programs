
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 



def Factrev(no1):
    for i in range(no1,0,-1):
        if no1 % i == 0:
            print(" ",i," ",end="")

def main():
    print("Enter a number : ")
    num = int(input())
    
    Factrev(num)

if __name__ == "__main__":
    main()
