
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    # my_list = [3,4,5,1,2]
    my_list = [4,5,6,7,0,1,2]
    
    temp = 0
    s = 1
    for i in range(len(my_list)):
        for j in range(s,len(my_list)):
            if my_list[i] > my_list[j]:
                temp = my_list[j]
                my_list[j] = my_list[i]
                my_list[i] = temp
        s += 1
    print(my_list[0])    
    
if __name__ == "__main__":
    main()