
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    print("Enter a input : ")
    data = input()

    tupleX = ""

    for i in range(len(data)):
        if data[i] in tupleX:
            continue
        else:
            tupleX += data[i]
    
    print(tupleX)
            
if __name__ == "__main__":
    main()