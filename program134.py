
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self):
        self.Head = None

def main():
    print("---- Linked list Node Insert ----")
    no = 1
    count = 0
    
    while(no):
        print("1 : Insert at first")
        print("2 : insert at middle")
        print("3 : insert at end")
        
        print("4 : delete at first")
        print("5 : delete at middle")
        print("6 : delete at end")
        
        print("7 : Display")
        print("8 : Exit")
        number = int(input())
        
        if number >= 1 and number < 8:
            if number == 1:
                print("Enter data : ")
                data = int(input())
                
                if count == 0:
                    LinkedList.Head = node(data)
                    count += 1
                else:
                    Temp = node(data)
                    Temp.next = LinkedList.Head.next
                    Temp.prev = LinkedList.Head
                    LinkedList.Head.next = Temp
                print("\n\n")
                
            elif number == 2:
                print("Enter data : ")
                data = int(input())
                print("Enter location : ")
                loc = int(input())
                countX = 0
                
                Temp = LinkedList.Head
                while(Temp.next != None):
                    countX += 1
                    Temp = Temp.next
                
                if countX < loc:
                    print("Invalid location")
                else:
                    Temp = LinkedList.Head
                    if loc == 1:
                        LinkedList.Head = node(data)
                    else:
                        for i in range(loc-1):
                            Temp = Temp.next
                        Temp1 = node(data)
                        Temp1.next = Temp.next
                        Temp.next.prev = Temp1
                        Temp1.prev = Temp
                        Temp.next = Temp1 
                print("\n\n")                    
                                
            elif number == 3:
                print("Enter data : ")
                data = int(input())
                
                if LinkedList.Head == None:
                    LinkedList.Head = node(data)
                else:
                    Temp = LinkedList.Head
                    while(Temp.next != None):
                        Temp = Temp.next
                    Temp.next = node(data) 
                    Temp.next.prev = Temp
                    
                print("\n\n")
            
            elif number == 4:
                LinkedList.Head.data = None
                print("\n\n")
            
            elif number == 5:
                print("Enter location : ")
                loc = int(input())
                
                count = 0
                Temp = LinkedList.Head
                while(Temp != None):
                    count += 1
                    Temp = Temp.next
                    
                if count < loc:
                    print("invalid input ")
                else:
                    Temp = LinkedList.Head
                    for i in range(loc):
                        Temp = Temp.next
                    Temp.data = None
                print("\n\n")
                
            elif number == 6:
                if LinkedList.Head.next == None:
                    LinkedList.Head.data = None
                else:
                    Temp = LinkedList.Head
                    while(Temp.next != None):
                        Temp = Temp.next
                    Temp.data = None
                print("\n\n")
                    
            elif number == 7:
                Temp = LinkedList.Head
                while(Temp != None):
                    print("| ",Temp.data," | => ",end="")
                    Temp = Temp.next
                print("\n\n")
                
        else:
            print("thank you : ")
            no = 0
            exit
    
if __name__ == "__main__":
    main()