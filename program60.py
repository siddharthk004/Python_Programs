
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def DigitsSum(no1):
    temp = 0
    sum = 0
    
    for i in range(len(no1)):
        while no1[i] != 0:
            temp = no1[i] % 10
            sum += temp
            no1[i] = no1[i]/10
            no1[i] = int(no1[i])
        if sum != 0:
            print(" ",sum," ",end="")
            sum = 0
            
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    print("Enter numbers : ")
    for i in range(num):
        value = int(input())
        listx.append(value)       
    
    DigitsSum(listx)
    
if __name__ == "__main__":
    main()