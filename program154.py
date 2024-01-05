
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    # my_list = [1,8,6,2,5,4,8,3,7]
    area = 0
    my_list = [1,1]
    
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            areaX = (j-i)*min(my_list[i],my_list[j])
            area = max(area,areaX)
    print(area)
    
if __name__ == "__main__":
    main()