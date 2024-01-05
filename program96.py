
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def ChkChar(ch):
    if ch >= 'A' and ch <= 'Z':
        return True
    elif ch >= 'a' and ch <= 'z':
        return True
    else:
        return False
            
def main():
    
    print("Enter input  : ")
    char = input() 
    
    flag = ChkChar(char)
    
    if flag == True:
        print(" It is Character ")
    else:
        print(" It is not Character ")
    
if __name__ == "__main__":
    main()