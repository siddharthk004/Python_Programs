
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def odddisplay(no1):
    for i in range(no1):
        if i % 2 != 0:
            print(" ",i," ")
    
def main():
    print("Enter a number : ")
    num = int(input())
    
    odddisplay(num)

if __name__ == "__main__":
    main()