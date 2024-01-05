
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 


def main():
    list = []
    temp = -1
    try:
        print("Enter the size of the list : ")
        size = int(input())
        
        try:
            print("Enter elements : ")
            for i in range(size):
                list.append(int(input()))
            
            print("Enter searching element : ")
            search = int(input())
            
            for i in range(size):
                if list[i] == search:
                    print("Element found at index : ",temp+1)
                else:
                    temp += 1
        except Exception:
            print("Invalid Input")    
        
    except Exception:
        print("invalid input")
        
if __name__ == "__main__":
    main()