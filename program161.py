
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    # my_list = [2, 7, 6, 1, 4, 5]
    my_list = [-2, 2, -5, 12, -11, -1, 7]
    k = 3
    maxl = 0
    for i in range(len(my_list)):
        sum1 = 0
        for j in range(i,len(my_list)):
            sum1 += my_list[j]
            if sum1 % k == 0:
                maxl = max(maxl, j - i + 1)
    print(maxl)
    
if __name__ == "__main__":
    main()