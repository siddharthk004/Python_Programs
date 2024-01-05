
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Pattern(no1):
    temp = 65
    for i in range(no1):
        print(chr(temp)," ",end="")
        temp += 1
    
def main():
    
    print("Enter length  : ")
    num = int(input()) 
    
    if num <= 0 and num > 26:     
        print("Wrong length of letter")
    else:
        Pattern(num)
    
if __name__ == "__main__":
    main()