
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

# Selection Sort

def Selection(my_list):
    num = my_list[0]
    X = len(my_list)
    for i in range(X):
        for j in range(i+1,X,1):
            if my_list[i] > my_list[j]:
                my_list[i],my_list[j] = my_list[j],my_list[i]
    return my_list
            


def main():
    my_list = [6,2,8,4,10]
    
    my_list = Selection(my_list)

    print(my_list)
    
if __name__ == "__main__":
    main()
    