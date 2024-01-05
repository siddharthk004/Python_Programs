
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    list = []
    
    print("Enter the total element size : ")
    size = int(input())
    
    for i in range(size):
        print("Enter value : ")
        num = int(input())
        list.append(num)
    
    for i in range(size):
        print(i," : ",list[i])
        
if __name__ == "__main__":
    main()