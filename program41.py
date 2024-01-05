
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def countDiff(no):
    temp = 0
    even = odd = 0
    
    if no < 0:
        no = -no
    
    while no != 0:
        temp = no%10
        no = no/10
        no = int(no)
        if temp % 2 == 0:
            even = even + temp
        else:
            odd = odd + temp
        
    return even-odd
        
def main():
    print("Enter a number : ")
    num = int(input())
    
    result = countDiff(num)
    
    print("Difference between even and odd number is : ",result)
    
if __name__ == "__main__":
    main()