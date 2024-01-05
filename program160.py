
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    print("Enter first number : ")
    a = int(input())
    
    print("Enter Second number : ")
    b = int(input())
    
    if a <= b:
        for i in range(a,b+1,1):
            if i%2 == 0 or i%5 == 0:
                print(i,end=" ")
    
if __name__ == "__main__":
    main()