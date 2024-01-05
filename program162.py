
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    my_list = [1,2,3,4]
    r = 3
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            for k in range(i+2,len(my_list)):
                print(my_list[i], my_list[j], my_list[k])
    
if __name__ == "__main__":
    main()