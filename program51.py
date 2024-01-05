
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Frequency(no1,no2):
    count = 0    
    flag = False
    
    for i in range(len(no1)):
        if no1[i] == no2:
            flag = True
    
    if flag == True:
        return True
    else:
        return False
               
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    print("Enter numbers : ")
    for i in range(num):
        value = int(input())
        listx.append(value)       
        
    print("Enter a number to cheak their existance : ")
    numchk = int(input())
    
    ret = Frequency(listx,numchk)
    if ret == True:
        print(numchk," is present")
    else:
        print(numchk," is not present")
        
if __name__ == "__main__":
    main()