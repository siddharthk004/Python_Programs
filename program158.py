
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    # my_list = [1,2,3,4,5,4,3,2,1]
    my_list = [1,4,5,1]
    
    demo = my_list[::-1]
    count = 0
    
    
    for i in range(int(len(my_list)/2)):
        if my_list[i] != demo[i]:
            count += 1
        else:
            continue
    if count != 0:
        print("there are need ",count," time to merged")
    else:
        print("Array is palindrome")
        
if __name__ == "__main__":
    main()