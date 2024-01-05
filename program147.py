
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 


def main():
    list = [1,3,2,5,3,6,7,8,9]
    print(list)
    
    first,second,flag,key = 0,0,0,False
    
    for i in range(len(list)):
        if list[i] > first:
            key = False
            first = list[i]
            
            if flag == 2:
                flag,second,key = 0,first,True
            
            if flag == 1:
                flag = 2
            
            if flag == 0 and key == False:
                flag = 1
            
    print("\n\nFirst large is : ",first)
    print("\nSecond large is : ",second)

if __name__ == "__main__":
    main()