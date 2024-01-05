
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 


def main():
    list = []
    print("Enter the size of the list : ")
    size = int(input())
    
    print("Enter element : ")
    for i in range(size):
        list.append(int(input()))
                    
    print(list)
    
    list = list[::-1]
    
    temp = list[int(size/2)]
    list[int(size/2)] = list[int(size/2)+1]
    list[int(size/2)+1] = temp
    
    print(list)

if __name__ == "__main__":
    main()