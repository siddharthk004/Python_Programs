
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
        print("4 : Display")
        print("5 : Exit")
        number = int(input())
        
        if number >= 1 and number <= 4:
            if number == 1:
                print("Enter data : ")
                data = int(input())
                
                if count == 0:
                    LinkedList.Head = node(data)
                    count += 1
                else:
                    Temp = node(data)
                    Temp.next = LinkedList.Head.next
                    LinkedList.Head.next = Temp

                Temp = LinkedList.Head
                while(Temp != None):
                    print("| ",Temp.data," |=> ",end="")
                    Temp = Temp.next
                print()
                print()
                
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
                        for i in range(loc):
                            Temp = Temp.next
                        Temp1 = node(data)
                        Temp1.next = Temp.next
                        Temp.next = Temp1    
                                       
                Temp = LinkedList.Head                
                while(Temp != None):
                    print("| ",Temp.data," |=> ",end="")
                    Temp = Temp.next
                print()
                print()                    
                                
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
                                         
                Temp = LinkedList.Head                
                while(Temp != None):
                    print("| ",Temp.data," |=> ",end="")
                    Temp = Temp.next
                print()
                print()
            
            elif number == 4:
                Temp = LinkedList.Head
                while(Temp != None):
                    print("| ",Temp.data," |=> ",end="")
                    Temp = Temp.next
                print()
                print()
                
        else:
            print("Wrong input : ")
            no = 0
            exit
    
if __name__ == "__main__":
    main()