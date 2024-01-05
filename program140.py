
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def sum(list,size):
    add = 0
    for i in range(size):
        add += list[i]
    return add

def main():
    list = []
    
    print("Enter the size of the list : ")
    size = int(input())
    
    print("Enter element : ")
    for i in range(size):
        list.append(int(input()))
    
    print("Sum is : ",sum(list,size))
if __name__ == "__main__":
    main()