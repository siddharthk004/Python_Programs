
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 



def nonFact(no1):
    for i in range(1,no1):
        if no1 % i == 0:
            pass
        else:
            print(" ",i," ",end="")

def main():
    print("Enter a number : ")
    num = int(input())
    
    nonFact(num)

if __name__ == "__main__":
    main()
