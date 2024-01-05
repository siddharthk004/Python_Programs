
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

class arrayX:
    def create(size,list):
        for i in range(size):
            print("Enter value : ")
            value = int(input())
            list.append(value)
        return list

    def display(size,list):
        print("Elements are : \n")
        
        for i in range(size):
            print(i," : ",list[i])

    def insert(list,size):
        print("Enter value : ")
        Value = int(input())
        list.append(Value)
        size += 1
        return list,size
    
    def insertpos(size,list):
        print("Enter element : ")
        value = int(input())
        
        print("Enter position : ")
        pos = int(input())
        
        if size > pos:
            list.append(value)
            size += 1
        else:
            print("position was wrong ")
        
        return list,size
    
    def search(search,list,size):
        for i in range(size):
            if list[i] == search:
                return True
        return False
    
    def update(list,size):
        print("Enter a position to update : ")
        pos = int(input())
        
        if pos < size:
            print("Enter value : ")
            value = int(input())
            list.insert(value,pos)
            size += 1
        else:
            print("Position is wrong")
        return list,size

def main():
    list = []
    
    print("Enter the total element size : ")
    size = int(input())
    list = arrayX.create(size,list)
    
    arrayX.display(size,list)
    
    print("insert a value at the end : ")
    list,size = arrayX.insert(list,size)
    arrayX.display(size,list)
    
    print("insert a value at the position : ")
    list,size = arrayX.insertpos(size,list)
    arrayX.display(size,list)
    
    print("Search an element : ")
    search = int(input())
    
    flag = arrayX.search(search,list,size)
    if flag == True:
        print("element is present ")
    else:
        print("element is not present")
    
    print("upadate a value : ")
    list,size= arrayX.update(list,size)
    arrayX.display(size,list)
    
if __name__ == "__main__":
    main()