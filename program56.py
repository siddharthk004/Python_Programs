
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Maximum(no1):
    max = 0
    for i in range(len(no1)):
        if no1[i] > max:
            max = no1[i]
    return max
   
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    print("Enter numbers : ")
    for i in range(num):
        value = int(input())
        listx.append(value)       
        
    
    ret = Maximum(listx)
    
    print("maximum elements is : ",ret)
    
if __name__ == "__main__":
    main()
    