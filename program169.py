
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    print("Enter first Input : ")
    data1 = input()
    
    print("Enter second Input : ")
    data2 = input()
    
    demo1 = tuple(data1)
    demo2 = tuple(data2)
    
    flag = False
    
    if len(demo1) == len(demo2):
        for i in range(len(demo1)):
            if demo1[i] in demo2:
                continue
            else:
                flag = True
                break
        if flag == True:
            print("False")
        else:
            print("True")
    else:
        print("Wrong")
if __name__ == "__main__":
    main()
    