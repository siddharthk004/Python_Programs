
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    my_list = [54, 546, 548, 60]
    if len(my_list) == 1:
        print(my_list[0])
    
    for i in range(len(my_list)):
        my_list[i] = str(my_list[i])
    
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[j]+my_list[i] > my_list[i]+my_list[j]:
                my_list[i],my_list[j] = my_list[j],my_list[i]
    
    Result = ''.join(my_list)
    
    if Result == '0'*len(my_list):
        print("o")
    else:
        print(Result)        
    
if __name__ == "__main__":
    main()