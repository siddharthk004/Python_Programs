
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

class stack:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.Head = None

def main():
    print("inplementation of stack using linked list")
    
    no = 1
    top = -1
    temp = 0
    
    while(no):
        print("1 : push")
        print("2 : pop")
        print("3 : display")
        print("4 : Exit")
        
        try:
            num = int(input())
            if num >= 1 and num <= 4:
                if num == 1:
                    print("Enter data : ")
                    try:
                        data = int(input())
                        if top == -1:
                            LinkedList.Head = stack(data)
                            temp = LinkedList.Head
                            top += 1
                        else:
                            node = stack(data)
                            temp.next = node
                            temp = temp.next
                            top += 1
                    except Exception:
                        print("invalid input")
                        
                elif num == 2:
                    if top == -1:
                        print("stack is empty")
                    else:
                        tempx = LinkedList.Head
                        for i in range(top-1):
                            tempx = tempx.next
                        print("pop element successfully")
                        print(tempx.data)
                        tempx.next = None
                        top -= 1
                
                elif num == 3:
                    if top == -1:
                        print("Stack is empty ")
                    else:
                        tempx = LinkedList.Head
                        for i in range(-1,top,1):
                            print(tempx.data," => ",end="")
                            tempx = tempx.next
                
                else:
                    print("thank you")
                    exit
                    no = 0
            
            else:
                print("invalid input")
        except Exception:
            print("invalid input")

if __name__ == "__main__":
    main()