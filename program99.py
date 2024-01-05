
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def ChkChar(ch):
    if ch >= 'a' and ch <= 'z':
        return True
    else:
        return False
            
def main():
    
    print("Enter input  : ")
    char = input() 
    
    flag = ChkChar(char)
    
    if flag == True:
        print(" It is Small letter ")
    else:
        print(" It is not Small letter ")
    
if __name__ == "__main__":
    main()