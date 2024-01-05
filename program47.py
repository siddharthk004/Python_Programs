
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def CountEven(no):
    temp = 0
    
    for i in range(len(no)):
        if no[i] % 2 == 0:
            temp += 1
    return temp
               
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    for i in range(num):
        value = int(input())
        listx.append(value)       
        
    ret = CountEven(listx)
    
    print("result is : ",ret)
    
if __name__ == "__main__":
    main()