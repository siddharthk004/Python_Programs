
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 



def display(no):
    for i in range(no):
        print(" * ",end="")

def main():
    
    print("Enter a number : ")
    num = int(input())
    
    display(num)
    
if __name__ == "__main__":
    main()