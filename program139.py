
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def reverse(list,size):
    temp = size-1
    for i in range(size):
        tempx = list[i]
        list[i] = list[temp]
        list[temp] = tempx
        
        if temp == i:
            break
        
        temp -= 1
        
    return list

def main():
    list = []
    print("Enter the size : ")
    size = int(input())
    
    print("enter element")
    for i in range(size):
        value = int(input())
        list.append(value)
    
    print("Before Reverse list is : ")
    print(list)
    
    list = reverse(list,size)
        
    print("After Reverse list is : ")
    print(list)

if __name__ == "__main__":
    main()