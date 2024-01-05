
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

class node:
    def __init__(self,no):
        self.data = no
        self.next = None

def main():
    print("______linked list implementation______")
    def __init__(self):
        self.head = None
    
    main.head = node(1)
    first = node(2)
    second = node(3)
    third = node(4)
    fourth = node(5)
    
    main.head.next = first
    first.next = second
    second.next = third
    third.next = fourth
    
    temp = main.head
    
    while(temp):
        print(temp.data," => ",end="")
        temp = temp.next
    
if __name__ == "__main__":
    main()    