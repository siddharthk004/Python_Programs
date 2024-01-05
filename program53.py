
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def LastOcc(no1,no2):
    count = 0    
    temp = 0
    flag = False
    
    for i in range(len(no1)):
        if no1[i] == no2:
            temp = count+1
            flag = True
        else:
            count += 1
    
    if flag == True:
        return temp+1
    else:
        return 0
               
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
    
    ret = LastOcc(listx,numchk)
    
    print("Last Occurance is : ",ret)
        
if __name__ == "__main__":
    main()