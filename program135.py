
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

class stack:
    def __init__(self):
        pass
    
    def push(list,top):
        try:
            print("Enter the value : ")
            value = int(input())
            top += 1
            list.append(value)
        except Exception:
            print("Invalid input ;")
        return list,top 
            
    def pop(list,top):
        value = list[top]
        print("poping successfully : ",value)
        top -= 1
        return top
    
    def isEmpty(top):
        if top != -1:
            return True
        else:
            return False
    
    def isFull(size,top):
        if top >= size:
            return True
        else:
            return False
        
    
    def display(list,top):
        for i in range(-1,top,1):
            print(i+1," : ",list[i])
        print("\n\n")
            
def main():
    list = []
    try:
        print("Enter the size of the list")
        size = int(input())
        size -= 1
    except Exception:
        print("invalid exception")
    
    top = -1
    no = 1
    
    while(no):
        print("1 : Push")
        print("2 : pop")
        print("3 : display")
        print("4 : Exit")
        try:
            number = int(input())
            if number == 1:
                if stack.isFull(top,size):
                    list,top = stack.push(list,top)
                else:
                    print("Stack is full")
            
            elif number == 2:
                if stack.isEmpty(top):
                    top = stack.pop(list,top)
                else:
                    print("stack is empty")
                    
            elif number == 3:
                if stack.isEmpty(top):
                    stack.display(list,top) 
                else:
                    print("Stack is empty")
                    
            elif number == 4:
                print("Thank you")
                no = 0
                exit
            
            else:
                print("Invalid position")
        
        except Exception:
            print("Invalid input")
        
    
if __name__ == "__main__":
    main()