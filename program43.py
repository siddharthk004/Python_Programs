
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def display(no):
    temp = 0
    even = odd = 0
    
    for i in range(len(no)):
        if no[i] % 5 == 0:
            print(" ",no[i]," ",end="")
               
def main():
    listx = []
    
    print("Enter a frequency : ")
    num = int(input())
    
    for i in range(num):
        value = int(input())
        listx.append(value)       
        
    display(listx)
    
if __name__ == "__main__":
    main()