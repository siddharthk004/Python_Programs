
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 


def main():
    list = []
    
    print("Enter the size of the list : ")
    size = int(input())
    
    print("Enter element : ")
    for i in range(size):
        list.append(int(input()))
        
    diff = size/2
    diff = int(diff)
    
    print("Difference is : ",diff)

if __name__ == "__main__":
    main()