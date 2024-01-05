
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

class tempX:
    def __init__(self):
        self.next = None

class tempX1:
    def __init__(self):
        self.next = None

class node:
    def __init__(self,no):
        self.data = no
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

def main():
    print("______linked list implementation______")
    count = 0
    no = 1
    while(no):
        print("1 : Add node")
        print("2 : delete node")
        print("3 : delete data")
        print("4 : display node")
        print("5 : Exit")
        num = int(input())
        if num >= 0 and num < 5:   
            if num == 5:
                no==0
                exit
                
            elif num == 1:
                print("Enter node data : ")
                nodedata = int(input())
                
                if count == 0:
                    linkedlist.head = node(nodedata)
                    temp = linkedlist.head
                    count += 1
                else:
                    temp1 = node(nodedata)
                    temp.next = temp1
                    temp = temp.next
                    count += 1
                print()
                print()    
                                
            # elif num == 2:
            #     print("Enter the node number to delete the node")
            #     nodenum = int(input())
            #     flag = False    
            #     tempX1 = 0 
            #     tempX = None
                
            #     tempX = linkedlist.head
            #     for i in range(count):
            #         tempX = tempX.next
            #         if nodenum == 1:
            #             flag = True
            #             tempX = None
                        
            #         elif i == nodenum:
            #             flag = True
            #             tempX1 = tempX.next
            #             tempX1 = tempX1.next
                        
            #             tempX.next = tempX1.next
                        
            #     if flag == True:
            #         print("Node delete Successfully")
            #     else:
            #         print("your node number is invalid")
            #     print()
            #     print()
                        
            elif num == 3:
                print("Enter Data to clear that data from the linkedlist")
                dataX = int(input())
                flag = False
                tempX = linkedlist.head
                for i in range(count):
                    if tempX.data == dataX:
                        tempX.data = None
                        flag = True
                    tempX = tempX.next
                if flag == True:
                    print("Node data delete Successfully")
                else:
                    print("your node data is invalid")
                print()
                print()
                       
            elif num == 4:
                if count == 0:
                    print("linked list is empty")
                else:
                    print("Display all nodes")
                    tempX = linkedlist.head
                    for i in range(count):
                        print("| ",tempX.data," | => ",end="")
                        tempX = tempX.next
                print()
                print()
        else:
            print("Wrong input")
            no = 0            
            exit
            
if __name__ == "__main__":
    main()    