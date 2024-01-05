
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def countDiff(no):
    temp = 0
    even = odd = 0
    
    for i in range(len(no)):
        if no[i] % 2 == 0:
            even = even + no[i]
        else:
            even = even + no[i]
    return even-odd
        
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    for i in range(num):
        value = int(input())
        listx.append(value)       
        
    result = countDiff(listx)
    
    print("Difference between even and odd number is : ",result)
    
if __name__ == "__main__":
    main()