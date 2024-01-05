
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    # my_list = [1,1,8,6,2,5,4,4,4,4,8,3,7]
    my_list = [ 88,554,43,21,56,231,241,32,41,65,34,38,454,4,15]

    print("Enter a number to find that number smallest element : ")
    k = int(input())
       
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i] > my_list[j]:
                temp = my_list[j]
                my_list[j] = my_list[i]
                my_list[i] = temp
    # print(my_list)
    min = my_list[0]
    if k > 0  and k <= len(my_list):
        for i in range(len(my_list)):
            if min < my_list[i]:
                min = my_list[i]
                k -= 1
            if k == 1:
                print("Kth smallest element is : ",min)
                break
    else:
        print("kth smallest position was wrong")
       
        
if __name__ == "__main__":
    main()