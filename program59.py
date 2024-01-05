
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Digits(no1):
    temp = 0
    value = 0
    
    for i in range(len(no1)):
        value = no1[i]
        
        while no1[i] != 0:
            no1[i] = no1[i]/10
            no1[i] = int(no1[i])
            temp += 1
            if temp == 3 and no1[i] == 0:
                print(" ",value," ",end="")
                
        if no1[i] == 0:
            temp = 0
            
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    print("Enter numbers : ")
    for i in range(num):
        value = int(input())
        listx.append(value)       
    
    Digits(listx)
    
if __name__ == "__main__":
    main()