
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def minimum(no1):
    min = 999
    for i in range(len(no1)):
        if no1[i] < min:
            min = no1[i]
    return min
   
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    print("Enter numbers : ")
    for i in range(num):
        value = int(input())
        listx.append(value)       
        
    
    ret = minimum(listx)
    
    print("minimum elements is : ",ret)
    
if __name__ == "__main__":
    main()