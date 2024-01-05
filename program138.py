
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    
    list = []
    try:
        print("Enter the size of the list : ")
        size = int(input())
            
        for i in range(size):
            value = int(input())
            list.append(value)
            
        max = 0
        min = 999
        
        for i in range(size):
            if list[i] > max:
                max = list[i]
                
            if list[i] < min:
                min = list[i]
            
        
        print("Smallest value is : ",min)
        print("largest value is : ",max)
        
    except Exception:
        print("Invalid input") 
if __name__ == "__main__":
    main()