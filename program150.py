
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    my_list = [1,2,-2,3,2,-1,3,5]
    # my_list = [2,3,-2,4]
    # my_list = [-2,0,-1]
    arr = []
    
    flag = 0
    mult = 1
    for i in range(len(my_list)):
        if my_list[i] >= 0:
            mult *= my_list[i]
        else:
            flag = 1
            
        if flag == 1:
            print(mult)
            arr.append(mult)
            mult = 1
            flag = 0
    
    ans = 0
    for i in range(len(arr)):
        if arr[i] > ans:
            ans = arr[i]
    
    if ans == 1:
        ans = 0
    print(ans)

if __name__ == "__main__":
    main()