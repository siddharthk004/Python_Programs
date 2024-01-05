
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Range(no1):
    mult = 1
    for i in range(len(no1)):
        if no1[i] % 2 != 0:
            mult = mult*no1[i]
    return mult
   
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    print("Enter numbers : ")
    for i in range(num):
        value = int(input())
        listx.append(value)       
        
    
    ret = Range(listx)
    
    print("Product of all elements is : ",ret)
    
if __name__ == "__main__":
    main()