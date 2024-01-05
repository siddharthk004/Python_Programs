
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Cheak(no):
    count = 0    
    for i in range(len(no)):
        if no[i] == 11:
            count += 1
    return count
               
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    for i in range(num):
        value = int(input())
        listx.append(value)       
        
    ret = Cheak(listx)
    
    print("Frequency of 11 is : ",ret)
        
if __name__ == "__main__":
    main()