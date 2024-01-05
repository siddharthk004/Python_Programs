
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def table(no):
    for i in range(1,11):
        sum = no * i
        print(" ",sum," ",end="")
def main():
    print("Enter a number : ")
    num = int(input())
    
    table(num)
    
if __name__ == "__main__":
    main()