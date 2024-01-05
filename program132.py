
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
    
    print("Element before inserting new value ")
    for i in range(size):
        print(i," : ",list[i])
        
    print("Enter value : ")
    Value = int(input())
    list.append(Value)
    
    print("Element After inserting new value ")
    for i in range(size+1):
        print(i," : ",list[i])
        
    print("Enter value at position: ")
    Value = int(input())
    print("Enter position : ")
    pos = int(input())
    
    if pos <= size:
        list.insert(Value,pos)
    
    print("Element After inserting new value ")
    for i in range(size+1):
        print(i," : ",list[i])
    
        
if __name__ == "__main__":
    main()