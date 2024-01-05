
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 


def duplicate(list,size):
    temp = size-1
    for i in range(size):
        if temp == i:
            break
        elif list[temp] == list[i]:
            return True
        temp -= 1
        
    return False

def main():
    list = []
    print("Enter size of the list : ")
    size = int(input())
    
    for i in range(size):
        list.append(int(input()))
    
    flag = duplicate(list,size)

    if flag == True:
        print("duplicate are present")
    else:
        print("duplicate are not present")

if __name__ == "__main__":
    main()