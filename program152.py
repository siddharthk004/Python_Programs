
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    # my_list = [4,5,6,7,0,1,2]
    my_list = [11,15,26,38,9,10]
    
    print("Enter sum : ")
    sum = int(input())
    s = 1
    for i in range(len(my_list)):
        for j in range(s,len(my_list)):
            suX = my_list[i] + my_list[j]
            if suX == sum:
                print(my_list[i]," : ",my_list[j])                
        s += 1   
    
if __name__ == "__main__":
    main()