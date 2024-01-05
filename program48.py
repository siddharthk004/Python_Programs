
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def CountEven(no):
    temp1 = 0
    temp2 = 0
    
    for i in range(len(no)):
        if no[i] % 2 == 0:
            temp1 += 1
        else:
            temp2 += 1
    return temp1-temp2
               
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    for i in range(num):
        value = int(input())
        listx.append(value)       
        
    ret = CountEven(listx)
    
    print("difference  of even and odd frequency is : ",ret)
    
if __name__ == "__main__":
    main()