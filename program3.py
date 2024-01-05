
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 



def display(no):
    while no != 0:
        print(" * ",end="")
        no = no - 1

def main():
    
    print("Enter a number : ")
    num = int(input())
    
    display(num)
    
if __name__ == "__main__":
    main()