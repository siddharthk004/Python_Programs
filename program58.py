
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Difference(no1):
    min = 999
    max = 0
    for i in range(len(no1)):
        if no1[i] < min:
            min = no1[i]
        elif no1[i] > max:
            max = no1[i] 
    return max-min
   
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    print("Enter numbers : ")
    for i in range(num):
        value = int(input())
        listx.append(value)       
        
    
    ret = Difference(listx)
    
    print("Difference elements is : ",ret)
    
if __name__ == "__main__":
    main()