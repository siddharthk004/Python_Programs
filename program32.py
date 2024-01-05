
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def DisplayDigit(no):
    if no < 0:
        no = -no
    
    while no != 0:
        temp = no%10
        no = no/10
        no = int(no)
        print(" ",temp," ")
        
def main():
    print("Enter a number : ")
    num = int(input())
    
    DisplayDigit(num)
    
if __name__ == "__main__":
    main()
