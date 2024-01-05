
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

class Queue:
    def __init__(self):
        pass
    
    def Enqueue(list,data,Rear):
        Rear += 1
        list.append(data)
        return list,Rear
    
    def Dequeue(list,Front,rear):
        print("\n\ndelete : ",list[Front])
        del list[Front]
        if rear != 0:
            rear -= 1
        return list,Front,rear   
    
    def display(list,front,rear):
        print("\nfront is : ",front)
        print("rear is : ",rear,"\n")

        for i in range(rear):
            print(" ",i," : ",list[i])
            
    
def main():
    front = 0
    rear = 0
    list = []
    
    no = 1
    while(no):
        print("\n\n1 : Enqueue")
        print("2 : Dequeue")
        print("3 : Display")
        print("4 : Exit")

    
        num = int(input())
        
        if num >= 1 and num <= 4:
            if num == 1:
                print("Enter data : ")
                
                data = int(input())
                list,rear = Queue.Enqueue(list,data,rear)
            
                
            elif num == 2:
                list,front,rear = Queue.Dequeue(list,front,rear)
                
            elif num == 3:
                Queue.display(list,front,rear)
            
            else:
                print("thank you")
                no = 0
                exit
            
        else:
            print("invalid input")
            
if __name__ == "__main__":
    main()