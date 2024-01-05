
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def ChkChar(ch):
    if ch >= '0' and ch <= '9':
        return True
    else:
        return False
            
def main():
    
    print("Enter input  : ")
    char = input() 
    
    flag = ChkChar(char)
    
    if flag == True:
        print(" It is Digit ")
    else:
        print(" It is not Digit ")
    
if __name__ == "__main__":
    main()