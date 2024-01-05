
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    my_list = [1,8,6,2,5,4,8,3,7]
    # my_list = [0,23,32,32,3]
    
    print("Enter 2 number sum : ")
    k = int(input())
    flag = False
    
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i]+my_list[j] == k:
                print(my_list[i]," : ",my_list[j])
                flag = True
    if flag == False:
        print("No any combination was found")
    
if __name__ == "__main__":
    main()