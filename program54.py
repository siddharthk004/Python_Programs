
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Range(no1,no2,no3):
    
    for i in range(len(no1)):
        if no1[i] >= no2 and no1[i] <= no3:
            print(" ",no1[i]," ",end="")
               
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    print("Enter numbers : ")
    for i in range(num):
        value = int(input())
        listx.append(value)       
        
    print("Enter a start number : ")
    numchk1 = int(input())
    print("Enter a end number : ")
    numchk2 = int(input())
    
    Range(listx,numchk1,numchk2)
        
if __name__ == "__main__":
    main()