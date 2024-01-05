
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    my_list = [-1,0,1,2,-1,-4]
    # my_list = [0,1,1]
    # my_list = [0,0,0]
    
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            for k in range(len(my_list)):
                if i != j and i != k and j != k:
                    if my_list[i] + my_list[j] + my_list[k] == 0:
                        print(my_list[i]," : ",my_list[j]," : ",my_list[k])
                
if __name__ == "__main__":
    main()