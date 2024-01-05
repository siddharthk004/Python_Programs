
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 



def display(no1,no2):
    for i in range(no2):
        print(no1," ",end="")

def main():
    
    print("Enter a number : ")
    num = int(input())
    
    print("Enter frequency : ")
    loop = int(input())
    
    display(num,loop)
    
if __name__ == "__main__":
    main()
