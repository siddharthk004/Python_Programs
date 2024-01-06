
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

# Bubble Sort

def Bubble(my_list):
    num = my_list[0]
    X = len(my_list)
    for i in range(X):
        for j in range(X):
            if j != X-1:
                if my_list[j] > my_list[j+1]:
                    my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
        X -= 1
    return my_list
            


def main():
    my_list = [6,2,8,4,10]
    
    my_list = Bubble(my_list)

    print(my_list)
    
if __name__ == "__main__":
    main()
    