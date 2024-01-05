
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Cheak(no):
    temp1 = 0
    temp2 = 0
    flag = False
    
    for i in range(len(no)):
        if no[i] == 11:
            flag =  True
    if flag == True:
        return True
    else:
        return False
               
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    for i in range(num):
        value = int(input())
        listx.append(value)       
        
    ret = Cheak(listx)
    
    if ret == True:
        print(" 11 is present ")
    else:
        print(" 11 is not present ")
        
if __name__ == "__main__":
    main()